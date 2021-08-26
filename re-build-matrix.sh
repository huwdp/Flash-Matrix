#!/bin/bash
cd ruffle
git pull
cd ..

cd lightspark
git pull
cd ..

cd playerglobal
git pull
cd ..

cd shumway
git pull
cd ..

cd gnash
git pull
cd ..

python buildtable.py
