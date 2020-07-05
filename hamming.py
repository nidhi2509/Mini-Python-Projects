"""
Make sure to fill in the following information before submitting your
assignment. Your grade may be affected if you leave it blank!
For usernames, make sure to use your Whitman usernames (i.e. exleyas). 
File name: hamming.py
Author username(s): harristr jaltarnr
Date: Oct. 16, 2017
"""

def hamming(str1, str2):
    """
    Finds the Hamming distance between two strings.
    
    Parameters:
    str1: String input
    str2: String input
    
    Returns: Hamming distance between str1 and str2
    """
    distance = 0    #Initializes Hamming distance
    
    if len(str1) <= len(str2):  #Checks if str1 is shorter or equal to str2 and keeps same if true
        newstr1 = str1
        newstr2 = str2
    
    else:   #Flips which string is first if str1 is longer
        newstr1 = str2
        newstr2 = str1
    
    for char in range(len(newstr1)):    #Adds distance if characters not matching
        if newstr1[char] != newstr2[char]:
            distance += 1
    
    if len(newstr1) != len(newstr2):    #Adds distance if one string is longer
        distance = distance + len(newstr2) - len(newstr1)
    
    return(distance)
    

def main():
    bits1 = open('bits1.txt', 'r')
    bits2 = open('bits2.txt', 'r')
    
    for linefirst in bits1:
        line1 = linefirst
        break
    for linesecond in bits2:
        line2 = linesecond
        break
    
    print(hamming(line1, line2))
    
    bits1.close()
    bits2.close()

if __name__ == '__main__':
    main()
