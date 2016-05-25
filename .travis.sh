#!/bin/bash

set -euo pipefail

# Prevent accidental execution outside of Travis:
if [ -z "${TRAVIS+false}" ]
then
  echo "TRAVIS environment variable is not set"
  exit 1
fi

WORKING_DIR="`pwd`/work"
CHECKOUT_DIR=$WORKING_DIR/checkout
RESULT_DIR=$WORKING_DIR/result

GIT_URL1=https://github.com/jacoco/www.eclemma.org.git
CHECKOUT_PATH1=$CHECKOUT_DIR/www.eclemma.org
BRANCH1=master

GIT_URL2=https://github.com/jacoco/eclemma.git
CHECKOUT_PATH2=$CHECKOUT_DIR/eclemma
BRANCH2=v2.3.2

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


TEMP=/tmp/jacoco-snapshot
mkdir $TEMP
wget -O $TEMP/download.zip "https://oss.sonatype.org/service/local/artifact/maven/redirect?r=snapshots&g=org.jacoco&a=jacoco&e=zip&v=LATEST"
unzip $TEMP/download.zip -d $TEMP

TARGET=$RESULT_DIR/jacoco/trunk
mkdir $TARGET
cp $TEMP/index.html $TARGET
cp -r $TEMP/doc $TARGET/doc
cp -r $TEMP/test $TARGET/test
cp -r $TEMP/coverage $TARGET/coverage


cd $RESULT_DIR

# https://help.github.com/articles/files-that-start-with-an-underscore-are-missing/
touch .nojekyll

git init
git add .
git commit -m "Automatic deployment"

if [[ ${TRAVIS_PULL_REQUEST} == 'false' && ${TRAVIS_BRANCH} == 'master' ]]
then
  git push --force "https://${GH_TOKEN}@github.com/jacoco/jacoco.github.io" master > /dev/null 2>&1
fi
