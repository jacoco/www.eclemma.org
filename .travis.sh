#!/bin/bash

set -euo pipefail

# Prevent accidental execution outside of Travis:
if [ -z "${TRAVIS+false}" ]
then
  echo "TRAVIS environment variable is not set"
  exit 1
fi

WORKING_DIR="`pwd`/work"
RESULT_DIR=$WORKING_DIR/result

./render.sh

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
git commit -q -m "Automatic deployment"

if [[ ${TRAVIS_PULL_REQUEST} == 'false' && ${TRAVIS_BRANCH} == 'master' ]]
then
  git push --force "https://${GH_TOKEN}@github.com/jacoco/jacoco.github.io" master > /dev/null 2>&1

  echo "www.jacoco.org" > CNAME && git add CNAME && git commit -q --amend --reuse-message=HEAD
  git push --force "https://${GH_TOKEN}@github.com/jacoco/jacoco.org" master:gh-pages > /dev/null 2>&1

  echo "www.eclemma.org" > CNAME && git add CNAME && git commit -q --amend --reuse-message=HEAD
  git push --force "https://${GH_TOKEN}@github.com/jacoco/eclemma.org" master:gh-pages > /dev/null 2>&1

  echo "www.eclemma.com" > CNAME && git add CNAME && git commit -q --amend --reuse-message=HEAD
  git push --force "https://${GH_TOKEN}@github.com/jacoco/eclemma.com" master:gh-pages > /dev/null 2>&1
fi
