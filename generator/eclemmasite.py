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
site.item('demoplain.html', File('content/demoplain.html'))
site.item('installation.html', Page('content/installation.html'))
site.item('download.html', Page('content/download.html'))
site.item('installation1x.html', Page('content/installation1x.html'))
site.item('images/topic.gif', File('content/images/topic.gif'))
site.item('images/container.gif', File('content/images/container.gif'))
site.item('images/extern.gif', File('content/images/extern.gif'))
site.item('images/class.jpg', File('content/images/class.jpg'))
site.item('images/eclemma110_80.gif', File('content/images/eclemma110_80.gif'))
site.item('images/eclipsecon.jpg', File('content/images/eclipsecon.jpg'))
site.item('images/smallscreen.gif', File('content/images/smallscreen.gif'))
site.item('images/award.jpg', File('content/images/award.jpg'))
site.item('images/tjsn.jpg', File('content/images/tjsn.jpg'))
site.item('images/friendslogo.jpg', File('content/images/friendslogo.jpg'))
site.item('images/screen.png', File('content/images/screen.png'))
site.item('images/glass.gif', File('content/images/glass.gif'))
site.item('images/ok.gif', File('content/images/ok.gif'))
site.item('images/progress.gif', File('content/images/progress.gif'))
site.item('images/install.png', File('content/images/install.png'))
site.item('images/jacoco.png', File('content/images/jacoco.png'))
site.item('images/info.gif', File('content/images/info.gif'))
site.item('images/warning.gif', File('content/images/warning.gif'))
site.item('images/jacocoreport.png', File('content/images/jacocoreport.png'))
site.item('images/cloudbees.png', File('content/images/cloudbees.png'))
site.item('images/sonarqube.png', File('content/images/sonarqube.png'))

site.item('userdoc/index.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/userguide.html'))
site.item('userdoc/launching.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/launching.html'))
site.item('userdoc/coverageview.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/coverageview.html'))
site.item('userdoc/annotations.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/annotations.html'))
site.item('userdoc/coverageproperties.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/coverageproperties.html'))
site.item('userdoc/decorators.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/decorators.html'))
site.item('userdoc/sessions.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/sessions.html'))
site.item('userdoc/importexport.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/importexport.html'))
site.item('userdoc/keyboard.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/keyboard.html'))
site.item('userdoc/preferences.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/preferences.html'))

site.item('userdoc/images/annotations.png', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/annotations.png'))
site.item('userdoc/images/coverageproperties.png', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/coverageproperties.png'))
site.item('userdoc/images/coverageview.png', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/coverageview.png'))
site.item('userdoc/images/coverageviewtools.png', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/coverageviewtools.png'))
site.item('userdoc/images/coverageviewmenu.png', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/coverageviewmenu.png'))
site.item('userdoc/images/launchdialog.png', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/launchdialog.png'))
site.item('userdoc/images/decorators.png', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/decorators.png'))
site.item('userdoc/images/launchtoolbar.gif', File('../eclemma/com.mountainminds.eclemma.doc/pages/images/launchtoolbar.gif'))

site.item('resources.html', Page('content/resources.html'))

site.item('research/index.html', Page('content/research/index.html'))
site.item('research/instrumentingosgi/index.html', Page('content/research/instrumentingosgi/index.html'))
site.item('research/instrumentingosgi/frameworkext.png', File('content/research/instrumentingosgi/frameworkext.png'))
site.item('research/instrumentingosgi/instrumentation.png', File('content/research/instrumentingosgi/instrumentation.png'))

site.item('devdoc/index.html',        Page('content/devdoc/index.html'))
site.item('devdoc/architecture.html', Page('content/devdoc/architecture.html'))
site.item('devdoc/checklist.html',    Page('content/devdoc/checklist.html'))
site.item('devdoc/eclemma20.html',    Page('content/devdoc/eclemma20.html'))
site.item('jacoco/index.html',        Page('content/jacoco/index.html'))

site.item('support.html', Page('content/support.html'))
site.item('faq.html',     Page('../eclemma/com.mountainminds.eclemma.doc/pages/faq.html'))
site.item('changes.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/changes.html'))
site.item('license.html', Page('../eclemma/com.mountainminds.eclemma.doc/pages/license.html'))
site.item('contact.html', Page('content/contact.html'))

# Site Structure

site.nav('Overview', 'index.html')
installation = site.nav('Installation', 'installation.html')
installation.nav('Download', 'download.html')
installation.nav('EclEmma 1.x', 'installation1x.html')

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
devdoc.nav('Architecture',      'devdoc/architecture.html')
devdoc.nav('EclEmma 2.0',       'devdoc/eclemma20.html')
devdoc.nav('Release Checklist', 'devdoc/checklist.html')

research = site.nav('Research', 'research/index.html')
research.nav('Instrumenting OSGi Bundles', 'research/instrumentingosgi/index.html')


site.nav('JaCoCo', 'jacoco/index.html')
site.nav('Change Log', 'changes.html')
site.nav('License', 'license.html')
site.nav('Contact', 'contact.html')


site.generate(sys.argv[1])
