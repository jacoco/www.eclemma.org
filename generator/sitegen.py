"""Simple Generator for EclEmma's site at SourceForge

$LastChangedDate$
$Revision$
"""
import os, os.path, sys, urlparse
import itertools
import genshi, genshi.input, genshi.template
import gitlog

templateloader = genshi.template.TemplateLoader(['./templates'])
        
PAGE = templateloader.load('page.html', encoding='utf-8')

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
    
class LinkCheckFilter(object):

    ATTRIBUTES = ('src', 'href')
    IGNORE_PREFIXES = ('#', 'http://', 'https://')

    def __init__(self, path, localpaths):
        self.path = path
        self.localpaths = localpaths

    def __call__(self, stream):
        for kind, data, pos in stream:
            if kind == genshi.Stream.START:
                attrs = data[1]
                for ref in filter(lambda v: v, map(lambda n: attrs.get(n), self.ATTRIBUTES)):
                    if not filter(lambda p: ref.startswith(p), self.IGNORE_PREFIXES):
                        if urlparse.urljoin(self.path, ref) not in self.localpaths:
                            raise Exception('Invalid reference %s in %s' % (ref, self.path))
            yield kind, data, pos


class OutputItem(object):

    def __init__(self, src):
        self.src = src
       
    def create(self, site, path):
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
          properties = gitlog.get_log_info(self.src)
        ))
        page = PAGE.generate(ctx)
        page |= LinkCheckFilter(path, site.localpaths())
        return page.render('xhtml', encoding='utf-8')
        

class NavigationNode(object):

    def __init__(self, label, href=None):
        self.label = label
        self.href = href
        self.children = []
        
    def nav(self, label, href=None):
        n = NavigationNode(label, href)
        self.children.append(n)
        return n
        
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
        
    def nav(self, label, href=None):
        n = NavigationNode(label, href)
        self.rootnode.children.append(n)
        return n

    def localpaths(self):
        return self.items.keys()

    def generate(self, basedir):
        bytesum = 0
        items = self.items.items()
        items.sort()
        for (path, item) in items:
            print '[DEBUG] %s' % (path)
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
            
            