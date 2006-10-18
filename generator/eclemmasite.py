"""EclEmma's site structure at SourceForge

$LastChangedDate: $
$Revision: $
"""

import sys
from sitegen import * 

site = Site()

# Site Content

site.item('book.css', File('content/book.css'))
site.item('index.html', Page('content/index.html'))
site.item('installation.html', Page('content/installation.html'))
site.item('images/eclemma110_80.gif', File('content/images/eclemma110_80.gif'))
site.item('images/smallscreen.gif', File('content/images/smallscreen.gif'))
site.item('images/screen.png', File('content/images/screen.png'))
site.item('images/glass.gif', File('content/images/glass.gif'))
site.item('images/ok.gif', File('content/images/ok.gif'))
site.item('images/progress.gif', File('content/images/progress.gif'))

site.item('userdoc/index.html',        Page('../com.mountainminds.eclemma.doc/pages/userguide.html'))
site.item('userdoc/launching.html',    Page('../com.mountainminds.eclemma.doc/pages/launching.html'))
site.item('userdoc/coverageview.html', Page('../com.mountainminds.eclemma.doc/pages/coverageview.html'))
site.item('userdoc/annotations.html',  Page('../com.mountainminds.eclemma.doc/pages/annotations.html'))
site.item('userdoc/sessions.html',     Page('../com.mountainminds.eclemma.doc/pages/sessions.html'))
site.item('userdoc/importexport.html', Page('../com.mountainminds.eclemma.doc/pages/importexport.html'))

site.item('userdoc/images/annotations.png', File('../com.mountainminds.eclemma.doc/pages/images/annotations.png'))
site.item('userdoc/images/coverageview.png', File('../com.mountainminds.eclemma.doc/pages/images/coverageview.png'))
site.item('userdoc/images/coverageviewtools.gif', File('../com.mountainminds.eclemma.doc/pages/images/coverageviewtools.gif'))
site.item('userdoc/images/launchdialog.png', File('../com.mountainminds.eclemma.doc/pages/images/launchdialog.png'))
site.item('userdoc/images/launchtoolbar.gif', File('../com.mountainminds.eclemma.doc/pages/images/launchtoolbar.gif'))
site.item('userdoc/images/importdialog.png', File('../com.mountainminds.eclemma.doc/pages/images/importdialog.png'))
site.item('userdoc/images/exportdialog.png', File('../com.mountainminds.eclemma.doc/pages/images/exportdialog.png'))

site.item('devdoc/index.html',         Page('content/devdoc/index.html'))
site.item('devdoc/repository.html',    Page('content/devdoc/repository.html'))
site.item('devdoc/architecture.html',  Page('content/devdoc/architecture.html'))
site.item('devdoc/todos.html',         Page('content/devdoc/todos.html'))
site.item('devdoc/checklist.html',     Page('content/devdoc/checklist.html'))

site.item('support.html', Page('content/support.html'))
site.item('changes.html', Page('../com.mountainminds.eclemma.doc/pages/changes.html'))
site.item('license.html', Page('../com.mountainminds.eclemma.doc/pages/license.html'))
site.item('contact.html', Page('content/contact.html'))

# Site Structure

site.nav('Overview', 'index.html')
site.nav('Download and Installation', 'installation.html')

userdoc = site.nav('User Documentation', 'userdoc/index.html')
site.nav('Launching in Coverage Mode', 'userdoc/launching.html', userdoc)
site.nav('Using the Coverage View',    'userdoc/coverageview.html', userdoc)
site.nav('Source Code Annotations',    'userdoc/annotations.html', userdoc)
site.nav('Managing Coverage Sessions', 'userdoc/sessions.html', userdoc)
site.nav('Session Import and Export',  'userdoc/importexport.html', userdoc)

devdoc = site.nav('Developer Documentation', 'devdoc/index.html')
site.nav('Source Repository', 'devdoc/repository.html', devdoc)
site.nav('Architecture',      'devdoc/architecture.html', devdoc)
site.nav('Open Issues',       'devdoc/todos.html', devdoc)
site.nav('Release Checklist', 'devdoc/checklist.html', devdoc)

site.nav('Support', 'support.html')
site.nav('Change Log', 'changes.html')
site.nav('License', 'license.html')
site.nav('Contact', 'contact.html')


site.generate(sys.argv[1])
