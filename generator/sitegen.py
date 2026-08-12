"""Simple Generator for www.eclemma.org
"""
import os, os.path, sys
import itertools
import genshi, genshi.input, genshi.template
import gitlog

from urllib.parse import urljoin

templateloader = genshi.template.TemplateLoader(['./templates'])
        
PAGE = templateloader.load('page.html', encoding='UTF-8')

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
                        if urljoin(self.path, ref) not in self.localpaths:
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
        with open(self.src, 'r+b') as f:
            return f.read()
        
class Page(OutputItem):
    def __init__(self, src):
        OutputItem.__init__(self, src)

    def create(self, site, path):
        with open(self.src, encoding='ISO-8859-1') as f:
            content = genshi.XML(f.read())
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
        return page.render('xhtml', encoding='UTF-8')
        

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
        for (path, item) in sorted(self.items.items()):
            outpath = os.path.normpath(os.path.join(basedir, path))
            try:
                os.makedirs(os.path.dirname(outpath))
            except:
                pass
            content = item.create(self, path)
            with open(outpath, 'w+b') as f:
                f.write(content)
            bytesum += len(content)
            print('%6d bytes %s' % (len(content), path))

        print('====================================================')
        print('%6d bytes for %d files' % (bytesum, len(self.items)))
