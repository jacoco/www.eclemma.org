#!/bin/sh

WORKING_DIR="`pwd`/work"
CHECKOUT_DIR=$WORKING_DIR/checkout
RESULT_DIR=$WORKING_DIR/result

GIT_URL_ECLEMMA=https://github.com/eclipse/eclemma.git
CHECKOUT_PATH_ECLEMMA=$CHECKOUT_DIR/eclemma
BRANCH_ECLEMMA=v3.1.3

rm -fr $WORKING_DIR
mkdir $WORKING_DIR

git clone -- $GIT_URL_ECLEMMA $CHECKOUT_PATH_ECLEMMA
git -C $CHECKOUT_PATH_ECLEMMA checkout $BRANCH_ECLEMMA

python generator/eclemmasite.py $RESULT_DIR

