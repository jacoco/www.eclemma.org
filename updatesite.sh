#!/bin/sh

WORKING_DIR="`pwd`/work"
CHECKOUT_DIR=$WORKING_DIR/checkout
RESULT_DIR=$WORKING_DIR/result

SVN_URL1=https://eclemma.svn.sourceforge.net/svnroot/eclemma/eclemmasite
SVN_URL2=https://eclemma.svn.sourceforge.net/svnroot/eclemma/eclemma/tags/v1.5.3/com.mountainminds.eclemma.doc
SVN_URL3=https://eclemma.svn.sourceforge.net/svnroot/eclemma/eclemma/trunk/com.mountainminds.eclemma.updatesite

CHECKOUT_PATH1=$CHECKOUT_DIR/eclemmasite
CHECKOUT_PATH2=$CHECKOUT_DIR/com.mountainminds.eclemma.doc
CHECKOUT_PATH3=$CHECKOUT_DIR/com.mountainminds.eclemma.updatesite

TARGET=mtnminds,eclemma@web.sourceforge.net:/home/groups/e/ec/eclemma/htdocs/

rm -fr $WORKING_DIR
mkdir $WORKING_DIR

svn export --force $SVN_URL1 $CHECKOUT_PATH1
svn export --force $SVN_URL2 $CHECKOUT_PATH2
svn export --force $SVN_URL3 $CHECKOUT_PATH3


cd $CHECKOUT_PATH1
python generator/eclemmasite.py $RESULT_DIR


scp -r $RESULT_DIR/* $TARGET
