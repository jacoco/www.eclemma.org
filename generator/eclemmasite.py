"""EclEmma's site structure at SourceForge

$LastChangedDate: $
$Revision: $
"""

import sys
from sitegen import * 

site = Site()

# Site Content

# (svnbasepath, localbasepath)
SITEBASE = ('eclemmasite/', '')
DOCBASE  = ('eclemma/trunk/com.mountainminds.eclemma.doc/', '../com.mountainminds.eclemma.doc/')
UPDATEBASE = ('eclemma/trunk/com.mountainminds.eclemma.updatesite/', '../com.mountainminds.eclemma.updatesite/')

site.item('book.css', File(SITEBASE, 'content/book.css'))
site.item('index.html', Page(SITEBASE, 'content/index.html'))
site.item('demo.html', Page(SITEBASE, 'content/demo.html'))
site.item('demoplain.html', File(SITEBASE, 'content/demoplain.html'))
site.item('installation.html', Page(SITEBASE, 'content/installation.html'))
site.item('images/eclemma110_80.gif', File(SITEBASE, 'content/images/eclemma110_80.gif'))
site.item('images/smallscreen.gif', File(SITEBASE, 'content/images/smallscreen.gif'))
site.item('images/screen.png', File(SITEBASE, 'content/images/screen.png'))
site.item('images/glass.gif', File(SITEBASE, 'content/images/glass.gif'))
site.item('images/ok.gif', File(SITEBASE, 'content/images/ok.gif'))
site.item('images/progress.gif', File(SITEBASE, 'content/images/progress.gif'))
site.item('images/newupdatesite.gif', File(SITEBASE, 'content/images/newupdatesite.gif'))

site.item('userdoc/index.html',        Page(DOCBASE, 'pages/userguide.html'))
site.item('userdoc/launching.html',    Page(DOCBASE, 'pages/launching.html'))
site.item('userdoc/coverageview.html', Page(DOCBASE, 'pages/coverageview.html'))
site.item('userdoc/annotations.html',  Page(DOCBASE, 'pages/annotations.html'))
site.item('userdoc/sessions.html',     Page(DOCBASE, 'pages/sessions.html'))
site.item('userdoc/importexport.html', Page(DOCBASE, 'pages/importexport.html'))
site.item('userdoc/keyboard.html',     Page(DOCBASE, 'pages/keyboard.html'))

site.item('userdoc/images/annotations.png', File(DOCBASE, 'pages/images/annotations.png'))
site.item('userdoc/images/coverageview.png', File(DOCBASE, 'pages/images/coverageview.png'))
site.item('userdoc/images/coverageviewtools.gif', File(DOCBASE, 'pages/images/coverageviewtools.gif'))
site.item('userdoc/images/launchdialog.png', File(DOCBASE, 'pages/images/launchdialog.png'))
site.item('userdoc/images/launchtoolbar.gif', File(DOCBASE, 'pages/images/launchtoolbar.gif'))
site.item('userdoc/images/importdialog.png', File(DOCBASE, 'pages/images/importdialog.png'))
site.item('userdoc/images/exportdialog.png', File(DOCBASE, 'pages/images/exportdialog.png'))

site.item('resources.html', Page(SITEBASE, 'content/resources.html'))

site.item('devdoc/index.html',        Page(SITEBASE, 'content/devdoc/index.html'))
site.item('devdoc/repository.html',   Page(SITEBASE, 'content/devdoc/repository.html'))
site.item('devdoc/architecture.html', Page(SITEBASE, 'content/devdoc/architecture.html'))
site.item('devdoc/todos.html',        Page(SITEBASE, 'content/devdoc/todos.html'))
site.item('devdoc/checklist.html',    Page(SITEBASE, 'content/devdoc/checklist.html'))

site.item('support.html', Page(SITEBASE, 'content/support.html'))
site.item('faq.html',     Page(DOCBASE,  'pages/faq.html'))
site.item('changes.html', Page(DOCBASE,  'pages/changes.html'))
site.item('license.html', Page(DOCBASE,  'pages/license.html'))
site.item('contact.html', Page(SITEBASE, 'content/contact.html'))

site.item('site.xml', File(UPDATEBASE, 'site.xml'))

# Site Structure

site.nav('Overview', 'index.html')
site.nav('Screencam Demo', 'demo.html')
site.nav('Download and Installation', 'installation.html')

userdoc = site.nav('User Guide', 'userdoc/index.html')
site.nav('Launching in Coverage Mode', 'userdoc/launching.html', userdoc)
site.nav('Using the Coverage View',    'userdoc/coverageview.html', userdoc)
site.nav('Source Code Annotations',    'userdoc/annotations.html', userdoc)
site.nav('Managing Coverage Sessions', 'userdoc/sessions.html', userdoc)
site.nav('Session Import and Export',  'userdoc/importexport.html', userdoc)
site.nav('Keyboard Usage',             'userdoc/keyboard.html', userdoc)

site.nav('Web Resources', 'resources.html')

devdoc = site.nav('Developer Information', 'devdoc/index.html')
site.nav('Source Repository', 'devdoc/repository.html', devdoc)
site.nav('Architecture',      'devdoc/architecture.html', devdoc)
site.nav('Open Issues',       'devdoc/todos.html', devdoc)
site.nav('Release Checklist', 'devdoc/checklist.html', devdoc)

support = site.nav('Support', 'support.html')
site.nav('Frequently Asked Questions', 'faq.html', support)

site.nav('Change Log', 'changes.html')
site.nav('License', 'license.html')
site.nav('Contact', 'contact.html')


site.generate(sys.argv[1])
