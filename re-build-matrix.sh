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

cp flash-matrix.json source/public/flash-matrix.json

git add ruffle
git add lightspark
git add shumway
git add gnash
git add flash-matrix.json
