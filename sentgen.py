""" 
File name: list_potpourri.py 
Author username(s): haidarbm, jaltarnr
Date:11/1/17 
"""

import random

def weighted_select(dictionary):
    total = 0
    for a,b, in dictionary.items():
        total = total + b
    x = random.uniform(0,total)
    for a,b in dictionary.items():
        if x < b:
            return a
        else:
            x = x - b
def bigram_count(string):
    freq = 0
    lst=string.split()
    maindict={}
    for wi in range(1,len(lst)):
        if lst[wi-1] not in maindict:
            maindict[lst[wi -1]] = {}
        if lst[wi] in maindict[lst[wi-1]]:
            maindict[lst[wi-1]][lst[wi]] += 1
        else:
            maindict[lst[wi-1]][lst[wi]] = 1
            
    return maindict

def random_sentence(dictionary,starting_word,length_sen):
    sentence = starting_word
    for i in range(length_sen-1):
        to_pass = dictionary.get(starting_word)
        starting_word = weighted_select(to_pass)
        sentence = sentence + " " + starting_word
    return sentence

        
def read_file(filename):
    file = filename.open(filename,'r')
    c = file.read()
    file.close()
    return c
def main():
    file_name = input('Enter a file name to create a bigram count from:')
    s = read_file(file_name)
    big = bigram_count(s)
    starting_word=input('Enter a starting word:')
    sen = random_sentence(big,starting_word,15)
    return sen
    