#!/usr/bin/env python
import os
import pprint
import json
import re

with open('flash-specification.json') as specification:
    data = json.load(specification)

    # Setup lightspark location
    dir = './lightspark/src/scripting/'

    # Find all missing constants
    for n in data:
        for className in data[n]:
            for item in data[n][className]['constants']:
                complete = False
                for subdir, dirs, files in os.walk(dir):
                    for file in files:
                        if file.endswith('.cpp'):
                            fileContent = open(os.path.join(subdir, file), "r")
                            lines = fileContent.read()
                            i = re.findall(className + '::sinit' ,lines)
                            if len(i) > 0:
                                m = re.findall('setVariableAtomByQName\(\"(\w+)"', lines)
                                for found in m:
                                    if found == item:
                                        complete = True
                if not complete:
                    print("Missing constant: " + item + ' in flash.' + n + '.' + className)

    # Find all missing properties
    for n in data:
        for className in data[n]:
            for item in data[n][className]['properties']:
                complete = False
                for subdir, dirs, files in os.walk(dir):
                    for file in files:
                        if file.endswith('.cpp'):
                            fileContent = open(os.path.join(subdir, file), "r")
                            lines = fileContent.read()
                            m = re.findall('ASFUNCTIONBODY_(GETTER|GETTER_SETTER)\(\w+.(\s+|)' + item + '\)', lines)
                            if len(m) > 0:
                                complete = True
                            #m = re.findall('ASFUNCTIONBODY_ATOM\(' + className + ',\w+' + item + '\)', lines)
                            #if complete is False  and len(m) > 0:
                            #    complete = True
                                #print('ASFUNCTIONBODY_GETTER\(' + className + '.\s+' + item + '\)')
                if not complete:
                    print("Missing property: " + item + ' in flash.' + n + '.' + className)

    # Find all missing methods
    for n in data:
        for className in data[n]:
            for item in data[n][className]['methods']:
                complete = False
                for subdir, dirs, files in os.walk(dir):
                    for file in files:
                        if file.endswith('.cpp'):
                            fileContent = open(os.path.join(subdir, file), "r")
                            lines = fileContent.read()
                            m = re.findall('ASFUNCTIONBODY_ATOM\(' + className + ',(\s+|)' + item + '\)', lines)
                            if len(m) > 0:
                                complete = True
                            #m = re.findall('ASFUNCTIONBODY_ATOM\(' + className + ',\w+' + item + '\)', lines)
                            #if complete is False  and len(m) > 0:
                            #    complete = True
                                #print('ASFUNCTIONBODY_GETTER\(' + className + '.\s+' + item + '\)')
                if not complete:
                    print("Missing method: " + item + ' in flash.' + n + '.' + className)
