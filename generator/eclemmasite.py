"""EclEmma's site structure at SourceForge

$LastChangedDate$
$Revision$
"""

import sys
from sitegen import * 

site = Site()

# Site Content

site.item('book.css', File('content/book.css'))
site.item('favicon.ico', File('content/favicon.ico'))
site.item('index.html', Page('content/index.html'))
site.item('demo.html', Page('content/demo.html'))
site.item('demoplain.html', File('content/demoplain.html'))
site.item('installation.html', Page('content/installation.html'))
site.item('images/topic.gif', File('content/images/topic.gif'))
site.item('images/book_cleancode.jpg', File('content/images/book_cleancode.jpg'));
site.item('images/book_effectivejava.jpg', File('content/images/book_effectivejava.jpg'));
site.item('images/book_javapowertools.jpg', File('content/images/book_javapowertools.jpg'));
site.item('images/container.gif', File('content/images/container.gif'))
site.item('images/extern.gif', File('content/images/extern.gif'))
site.item('images/eclipsecon2009.gif', File('content/images/eclipsecon2009.gif'))
site.item('images/class.jpg', File('content/images/class.jpg'))
site.item('images/eclemma110_80.gif', File('content/images/eclemma110_80.gif'))
site.item('images/smallscreen.gif', File('content/images/smallscreen.gif'))
site.item('images/award.jpg', File('content/images/award.jpg'))
site.item('images/friendslogo.jpg', File('content/images/friendslogo.jpg'))
site.item('images/screen.png', File('content/images/screen.png'))
site.item('images/glass.gif', File('content/images/glass.gif'))
site.item('images/ok.gif', File('content/images/ok.gif'))
site.item('images/progress.gif', File('content/images/progress.gif'))
site.item('images/addsite.gif', File('content/images/addsite.gif'))
site.item('images/newupdatesite.gif', File('content/images/newupdatesite.gif'))
site.item('images/yoxos.png', File('content/images/yoxos.png'))

site.item('userdoc/index.html', Page('../com.mountainminds.eclemma.doc/pages/userguide.html'))
site.item('userdoc/launching.html', Page('../com.mountainminds.eclemma.doc/pages/launching.html'))
site.item('userdoc/coverageview.html', Page('../com.mountainminds.eclemma.doc/pages/coverageview.html'))
site.item('userdoc/annotations.html', Page('../com.mountainminds.eclemma.doc/pages/annotations.html'))
site.item('userdoc/coverageproperties.html',  Page('../com.mountainminds.eclemma.doc/pages/coverageproperties.html'))
site.item('userdoc/decorators.html', Page('../com.mountainminds.eclemma.doc/pages/decorators.html'))
site.item('userdoc/sessions.html', Page('../com.mountainminds.eclemma.doc/pages/sessions.html'))
site.item('userdoc/importexport.html', Page('../com.mountainminds.eclemma.doc/pages/importexport.html'))
site.item('userdoc/keyboard.html', Page('../com.mountainminds.eclemma.doc/pages/keyboard.html'))
site.item('userdoc/preferences.html', Page('../com.mountainminds.eclemma.doc/pages/preferences.html'))

site.item('userdoc/images/annotations.png', File('../com.mountainminds.eclemma.doc/pages/images/annotations.png'))
site.item('userdoc/images/coverageproperties.png', File('../com.mountainminds.eclemma.doc/pages/images/coverageproperties.png'))
site.item('userdoc/images/coverageview.png', File('../com.mountainminds.eclemma.doc/pages/images/coverageview.png'))
site.item('userdoc/images/coverageviewtools.png', File('../com.mountainminds.eclemma.doc/pages/images/coverageviewtools.png'))
site.item('userdoc/images/coverageviewmenu.png', File('../com.mountainminds.eclemma.doc/pages/images/coverageviewmenu.png'))
site.item('userdoc/images/launchdialog.png', File('../com.mountainminds.eclemma.doc/pages/images/launchdialog.png'))
site.item('userdoc/images/decorators.png', File('../com.mountainminds.eclemma.doc/pages/images/decorators.png'))
site.item('userdoc/images/launchtoolbar.gif', File('../com.mountainminds.eclemma.doc/pages/images/launchtoolbar.gif'))
site.item('userdoc/images/importdialog.png', File('../com.mountainminds.eclemma.doc/pages/images/importdialog.png'))
site.item('userdoc/images/exportdialog.png', File('../com.mountainminds.eclemma.doc/pages/images/exportdialog.png'))

site.item('resources.html', Page('content/resources.html'))

site.item('research/index.html', Page('content/research/index.html'))
site.item('research/instrumentingosgi/index.html', Page('content/research/instrumentingosgi/index.html'))
site.item('research/instrumentingosgi/frameworkext.png', File('content/research/instrumentingosgi/frameworkext.png'))
site.item('research/instrumentingosgi/instrumentation.png', File('content/research/instrumentingosgi/instrumentation.png'))
#site.item('research/codecoveragecornercases/index.html', Page('content/research/codecoveragecornercases/index.html'))
#site.item('research/codecoveragecornercases/CodeCoverageCornerCases.java', File('content/research/codecoveragecornercases/CodeCoverageCornerCases.java'))
#site.item('research/codecoveragecornercases/cobertura.html', File('content/research/codecoveragecornercases/cobertura.html'))
#site.item('research/codecoveragecornercases/coverlipse.xml', File('content/research/codecoveragecornercases/coverlipse.xml'))
#site.item('research/codecoveragecornercases/emma.html', File('content/research/codecoveragecornercases/emma.html'))
#site.item('research/codecoveragecornercases/cobertura-css/main.css', File('content/research/codecoveragecornercases/cobertura-css/main.css'))
#site.item('research/codecoveragecornercases/cobertura-css/source-viewer.css', File('content/research/codecoveragecornercases/cobertura-css/source-viewer.css'))

site.item('devdoc/index.html',        Page('content/devdoc/index.html'))
site.item('devdoc/repository.html',   Page('content/devdoc/repository.html'))
site.item('devdoc/architecture.html', Page('content/devdoc/architecture.html'))
site.item('devdoc/todos.html',        Page('content/devdoc/todos.html'))
site.item('devdoc/checklist.html',    Page('content/devdoc/checklist.html'))

site.item('support.html', Page('content/support.html'))
site.item('faq.html',     Page('../com.mountainminds.eclemma.doc/pages/faq.html'))
site.item('changes.html', Page('../com.mountainminds.eclemma.doc/pages/changes.html'))
site.item('license.html', Page('../com.mountainminds.eclemma.doc/pages/license.html'))
site.item('contact.html', Page('content/contact.html'))

site.item('site.xml', File('../com.mountainminds.eclemma.updatesite/site.xml'))

# Site Structure

site.nav('Overview', 'index.html')
site.nav('Screencam Demo', 'demo.html')
site.nav('Installation', 'installation.html')

userdoc = site.nav('User Guide', 'userdoc/index.html')
userdoc.nav('Launching in Coverage Mode', 'userdoc/launching.html')
userdoc.nav('Using the Coverage View',    'userdoc/coverageview.html')
userdoc.nav('Source Code Annotations',    'userdoc/annotations.html')
userdoc.nav('Coverage Properties',        'userdoc/coverageproperties.html')
userdoc.nav('Decorators',                 'userdoc/decorators.html')
userdoc.nav('Managing Coverage Sessions', 'userdoc/sessions.html')
userdoc.nav('Session Import and Export',  'userdoc/importexport.html')
userdoc.nav('Keyboard Usage',             'userdoc/keyboard.html')
userdoc.nav('Preferences',                'userdoc/preferences.html')

support = site.nav('Support', 'support.html')
support.nav('Frequently Asked Questions', 'faq.html')

site.nav('Resources', 'resources.html')

devdoc = site.nav('Developer Information', 'devdoc/index.html')
devdoc.nav('Source Repository', 'devdoc/repository.html')
devdoc.nav('Architecture',      'devdoc/architecture.html')
devdoc.nav('Open Issues',       'devdoc/todos.html')
devdoc.nav('Release Checklist', 'devdoc/checklist.html')

research = site.nav('Research', 'research/index.html')
research.nav('Instrumenting OSGi Bundles', 'research/instrumentingosgi/index.html')

site.nav('Change Log', 'changes.html')
site.nav('License', 'license.html')
site.nav('Contact', 'contact.html')


site.generate(sys.argv[1])
