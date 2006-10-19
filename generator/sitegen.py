"""Simple Generator for EclEmma's site at SourceForge

$LastChangedDate: $
$Revision: $
"""
import os, os.path
import re

_REGEX_BODY = re.compile('<body>(.*)</body>', re.DOTALL)
_REGEX_METATAG = re.compile('<meta\s*name="(.*)"\s*content="(.*)">')
_REGEX_TITLE = re.compile('<title>(.*)</title>')
_REGEX_HREF = re.compile(' (href|src)="([^"]*)"')

def _loadpage(src, encoding='iso-8859-1'):
    f = file(src, 'r+b')
    content = unicode(f.read(), encoding)
    f.close()
    page = {}
    page['title'] = _REGEX_TITLE.findall(content)[0]
    page['body'] = _REGEX_BODY.findall(content)[0]
    for (key, value) in _REGEX_METATAG.findall(content):
        page[key] = value
    return page

class Template(object):
    def __init__(self, path, encoding='iso-8859-1'):
        f = file(path, 'r+b')
        self.template = unicode(f.read(), encoding)
        f.close();
        
    def render(self, valuemap):
        return self.template % valuemap
        
PAGE      = Template('templates/page.html')
NAVITEM   = Template('templates/navitem.html')
NAVITEMHI = Template('templates/navitemhi.html')

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
    
def _navigation(root, current):
    return ''.join(map(lambda n: _navigationEntry(n, current), root.children))

def _navigationEntry(node, current, nesting=0):
    n = { 'href': _rellink(current, node.href),
           'label': node.label,
           'indent': nesting * 15 }
    if node.href == current:
        s = NAVITEMHI.render(n)
    else:
        s = NAVITEM.render(n)
    return s + ''.join(map(lambda n: _navigationEntry(n, current, nesting + 1), node.children))
 
    
class OutputItem(object):

    def __init__(self, basepaths, src):
        self.svnbasepath = basepaths[0]
        self.localbasepath = basepaths[1]
        self.src = src
       
    def create(self, rootnode):
        pass
        
    def verify_hrefs(self, content, path, allpaths):
        pass

class File(OutputItem):
    def __init__(self, basepaths, src):
        OutputItem.__init__(self, basepaths, src)

    def create(self, rootnode, current):
        f = open(_joinpaths(self.localbasepath, self.src), 'r+b')
        content = f.read()
        f.close()
        return content
        
class Page(OutputItem):
    def __init__(self, basepaths, src, encoding='iso-8859-1'):
        OutputItem.__init__(self, basepaths, src)
        self.encoding = encoding

    def create(self, rootnode, current):
        p = _loadpage(_joinpaths(self.localbasepath, self.src), self.encoding)
        p['styleref'] = _rellink(current, 'book.css')
        p['navigation'] = _navigation(rootnode, current)
        p['svnpath'] = _joinpaths(self.svnbasepath, self.src)
        return PAGE.render(p)

    def verify_hrefs(self, content, path, allpaths):
        for (ignore, href) in _REGEX_HREF.findall(content):
            if href.find('http://') != 0 and href.find('https://') != 0:
                href = _joinpaths(path, href)
                if href not in allpaths:
                    raise str('Invalid reference %s in %s' % (href, path))

class NavigationNode(object):

    def __init__(self, label, href=None):
        self.label = label
        self.href = href
        self.children = []


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
            content = item.create(self.rootnode, path)
            item.verify_hrefs(content, path, self.items.keys())
            f.write(content)
            f.close()
            bytesum += len(content)
            print '%6d bytes %s' % (len(content), path)

        print '===================================================='
        print '%6d bytes for %d files' % (bytesum, len(self.items))
            
            