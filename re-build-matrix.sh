#!/bin/bash
git clone https://github.com/mozilla/shumway.git
git clone https://github.com/strk/gnash.git
git clone https://github.com/lightspark/lightspark.git
git clone https://github.com/ruffle-rs/ruffle.git
git clone https://github.com/awayfl/playerglobal.git
git clone https://github.com/awayfl/avm2.git
python buildtable.py
cp flash-matrix.json source/public/flash-matrix.json
git add flash-matrix.json
git add flash-matrix.json source/public/flash-matrix.json
rm -rf ruffle
rm -rf lightspark
rm -rf playerglobal
rm -rf avm2
rm -rf shumway
rm -rf gnash
