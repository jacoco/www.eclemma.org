#!/bin/sh

WORKING_DIR="`pwd`/work"
CHECKOUT_DIR=$WORKING_DIR/checkout
RESULT_DIR=$WORKING_DIR/result

GIT_URL1=https://github.com/jacoco/www.eclemma.org.git
CHECKOUT_PATH1=$CHECKOUT_DIR/www.eclemma.org
BRANCH1=master

GIT_URL2=https://github.com/jacoco/eclemma.git
CHECKOUT_PATH2=$CHECKOUT_DIR/eclemma
BRANCH2=v2.3.2

TARGET=mtnminds,eclemma@web.sourceforge.net:/home/groups/e/ec/eclemma/htdocs/

rm -fr $WORKING_DIR
mkdir $WORKING_DIR

git clone -- $GIT_URL1 $CHECKOUT_PATH1
cd $CHECKOUT_PATH1
git checkout $BRANCH1

git clone -- $GIT_URL2 $CHECKOUT_PATH2
cd $CHECKOUT_PATH2
git checkout $BRANCH2


cd $CHECKOUT_PATH1
python generator/eclemmasite.py $RESULT_DIR


scp -r $RESULT_DIR/* $TARGET
