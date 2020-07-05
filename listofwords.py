
wordfile = open("words.txt")
wordset = {word.strip() for word in wordfile.readlines()}


def isListOfWords(s):
    #write a O(N^2) algorithm to determine whether the string can be broken into a list of words
    #You can start by writing an exponential algorithm and then using dynamic programming to 
    #  improve the runtime complexity
    
    TheDict = [False] * (len(s) + 1) #Creates a dictionary and sets everything to false
    TheDict[0] = True 
    for i in range(len(s)): #one for loop which would take O(n) time
        for j in range(i, len(s)): #second for loop taking O(n) time
            if TheDict[i] and s[i: j+1] in wordset: #checks if the substring is in the wordset and if the substring is already checked
                TheDict[j+1] = True
                    
    return TheDict[-1]

assert(isListOfWords("alistofwords"))
assert(isListOfWords("anotherlistofwords"))
assert(isListOfWords("stableapathydropon"))
assert(not isListOfWords("retouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappointx"))
assert(not isListOfWords("xretouchesreissueshockshopbedrollsunspotassailsinstilledintersectionpipitreappoint"))

