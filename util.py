#!/usr/bin/env python

import string
import demoji
import re

try:
    stop_words = set(line.strip() for line in open('stop-words.txt'))
except:
    stop_words = ["a","o","as","os","e","do","da","de","dos","das","na","no","nas","nos"]

def remove_emojis(string):
    return demoji.replace(string)

def remove_links(string):
    return re.sub(r'\b(?:(?:https?|ftp)://)?\w[\w-]*(?:\.[\w-]+)+\S*', '', string)

def remove_symbols(string):
    return re.sub(r"[,.;:?!&$*'\"“()\[\]…•%¨°]+", ' ', string)

def f_stop_words(item):
	return item.lower() not in stop_words

def clean(string):
    
    string = remove_emojis(string)
    string = remove_links(string)
    string = remove_symbols(string)
    
    return re.sub(' +', ' ', string.lower()) # lowercase and remove extra spaces

def tokenize(phrase):

    phrase = remove_emojis(phrase)
    phrase = remove_links(phrase)
    phrase = remove_symbols(phrase)

    words = sorted(phrase.split(' '))
    words = [x.lower() for x in words]
    words = list(filter(f_stop_words, words))
    words = list(filter(None, words))

    return words