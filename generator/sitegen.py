"""Simple Generator for EclEmma's site at SourceForge

$LastChangedDate$
$Revision$
"""
import os, os.path, sys
import genshi, genshi.input, genshi.template


templateloader = genshi.template.TemplateLoader(['./templates'])
        
PAGE = templateloader.load('page.html')

def _rellink(base, href):
    base = base.split('/')
    href = href.split('/')
    while len(base) > 1 and len(href) > 1 and base[0] == href[0]:
        base = base[1:]
        href = href[1:]
    while len(base) > 1:
        base = base[1:]
        href = ['..'] + href
    return '/'.join(href)

def _joinpaths(base, path):
    base = base.split('/')[:-1]
    for seg in path.split('/'):
        if seg == '..' and len(base) > 0:
            base = base[:-1]
        else:
            base.append(seg)
    return '/'.join(base)
    
class OutputItem(object):

    def __init__(self, src):
        self.src = src
       
    def create(self, site, path):
        pass
        
    def verify_hrefs(self, content, path, allpaths):
        pass

class File(OutputItem):
    def __init__(self, src):
        OutputItem.__init__(self, src)

    def create(self, site, path):
        f = open(self.src, 'r+b')
        content = f.read()
        f.close()
        return content
        
class Page(OutputItem):
    def __init__(self, src):
        OutputItem.__init__(self, src)

    def create(self, site, path):
        content = genshi.Stream(list(genshi.input.XMLParser(file(self.src))))
        def cond(c, a, b):
            if c:
                return a
            else:
                return b
        ctx = genshi.template.Context()
        ctx.push(dict(
          content = content,
          path = path,
          cond = cond,
          menuitems = site.rootnode.children,
          rellink = lambda link: _rellink(path, link),
          meta = lambda name: tuple(content.select('head/meta[@name="%s"]' % name))[0][1][1].get('content')
        ))
        page = genshi.Stream(list(PAGE.generate(ctx)))
        self._verifyrefs(page, site, path)
        return page.render('xhtml')
        
    def _verifyrefs(self, page, site, path):
        paths = site.local_paths()
        for (kind, data, pos) in page:
            if kind == genshi.input.START:
                ref = data[1].get('href')
                if not ref: ref = data[1].get('src')
                if ref and ref[0] != '#' and ref.find('http://') != 0 and ref.find('https://') != 0:
                    ref = _joinpaths(path, ref)
                    if ref not in paths:
                        raise str('Invalid reference %s in %s' % (ref, path))

class NavigationNode(object):

    def __init__(self, label, href=None):
        self.label = label
        self.href = href
        self.children = []
        
    def is_parent(self, href):
        if self.href == href:
            return 1
        for c in self.children:
            if c.is_parent(href):
                return 1


class Site(object):

    def __init__(self):
        self.items = {}
        self.rootnode = NavigationNode('<ROOT>')

    def item(self, path, src):
        if path in self.items:
            raise 'Item %s is already defined' % path
        self.items[path] = src
        
    def nav(self, label, href=None, parent=None):
        if href is not None and href not in self.items:
            raise 'Item %s is not defined' % href
        n = NavigationNode(label, href)
        if parent:
            parent.children.append(n)
        else:
            self.rootnode.children.append(n)
        return n

    def local_paths(self):
        return self.items.keys()

    def generate(self, basedir):
        bytesum = 0
        items = self.items.items()
        items.sort()
        for (path, item) in items:
            outpath = os.path.normpath(os.path.join(basedir, path))
            try:
                os.makedirs(os.path.dirname(outpath))
            except:
                pass
            f = open(outpath, 'w+b')
            content = item.create(self, path)
            f.write(content)
            f.close()
            bytesum += len(content)
            print '%6d bytes %s' % (len(content), path)

        print '===================================================='
        print '%6d bytes for %d files' % (bytesum, len(self.items))
            
            