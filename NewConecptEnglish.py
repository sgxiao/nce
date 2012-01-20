#!/usr/bin/env python
import sys
import os, re

"""
check out a word that appear in New Concept English 2 - 4, then return the Lesson number and the sentence that include the word
"""

nce_hash = {}

def nceHashInit():
    title = 'other'
    nce_hash[title] = ''
    f = open('ttt', "r")
    
    nceRe = re.compile('Lesson\s*\d+.*', re.I)
    nceBlankLineRe = re.compile('[^\s]+', re.I)
    for line in f.readlines():
        result = nceRe.search(line)
        if result != None:
            title = result.group(0)
            nce_hash[title] = ''
        else:
            result = nceBlankLineRe.search(line)
            if result != None:
                nce_hash[title] = ''.join([nce_hash[title], line])

def getSentenceFromKeyword(keyword):
    returns = ""
    nceRe = re.compile('([a-zA-Z0-9\ ,-]+\ )(' + keyword + ')(\ [a-zA-Z0-9\ ,-]+\.)')
    for title, article in nce_hash.items():
        result = nceRe.search(nce_hash[title])
        if result != None:
            returns = returns + "\n<%s>\n%s\n" % (title, result.group(0))
            
    return returns

if __name__ == "__main__":
    nceHashInit()
    if len(sys.argv) > 1:
        print getSentenceFromKeyword(sys.argv[1])
    else:
        print getSentenceFromKeyword(sys.stdin.readline().rstrip("\n"))
