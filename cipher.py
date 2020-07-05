""""
File name: cipher.py
Author username(s): jaltarnr, nyaticmb
Date: 10/11/2017
"""
def encode(textfilename, key):
    """This function uses the caeser cipher method to encrypt text inside a file. 
    Parameters: textfilename = the name of the file, key = the key you want to use.
    Return value : encoded message"""
    file = open(textfilename,"r")
    c = ""
        
       
        
    count = 0
    countspace = 0
    for line in file:
            
        for i in range(0, len(line)):
            
            keyindex= (count + i - countspace) % len(key)
            x = key[keyindex]
            if ord(line[i]) > 96:
            
                
                
            
                y = ord(line[i]) - 97 + ord(x) - 97
                
                y = y%26 + 97
                
                u = chr(y) 
                c = c + u
            else:
                c = c + chr(32)
                countspace = countspace + 1
        count = count + len(line)  
            
    return c

    
def decode(textfilename, key):
    """This function uses the caeser cipher method to decrypt text inside a file. 
    Parameters: textfilename = the name of the file, key = the key you want to use.
    Return value : decoded message"""
    file = open(textfilename,"r")
    c = ""
        
       
        
    count = 0
    countspace = 0
    for line in file:
    
        for i in range(0, len(line)):
            
            keyindex= (count + i - countspace) % len(key)
            x = key[keyindex]
            if ord(line[i]) > 96:
            
                
                
            
                y = ord(line[i]) + 97 - ord(x) - 97
                
                y = y%26 + 97
                
                u = chr(y) 
                c = c + u
            else:
                c = c + chr(32)
                countspace = countspace + 1
        count = count + len(line) 
            
    return c
    
    
    
    
    

        
def encode_space(textfilename, key):
    """This function uses the caeser cipher method to encrypt text inside a file. 
    Parameters: textfilename = the name of the file, key = the key you want to use.
    Return value : encoded message"""
    file = open(textfilename,"r")
    c = ""
        
       
        
    count = 0
    
    for line in file:
            
        for i in range(0, len(line)):
            
            keyindex= (count + i ) % len(key)
            x = key[keyindex]
            
            y = ord(line[i]) - 97 + ord(x) - 97
            y = y%28 + 97
            u = chr(y) 
            c = c + u
                
        count = count + len(line)  
            
    return c
def decode_space(textfilename, key):
    """This function uses the caeser cipher method to decrypt text inside a file. 
    Parameters: textfilename = the name of the file, key = the key you want to use.
    Return value : decoded message"""
    file = open(textfilename,"r")
    c = ""
        
       
        
    count = 0
    countspace = 0
    for line in file:
    
        for i in range(0, len(line)):
            
            keyindex= (count + i - countspace) % len(key)
            x = key[keyindex]
            y = ord(line[i]) + 97 - ord(x) - 97
                
            y = y%28 + 97
                
            u = chr(y) 
            c = c + u       
        count = count + len(line) 
            
    return c
def main():
    answer = input("Would you like to (e)ncode or (d)ecode?")
    if answer == "e":
        a1 = input("What is your filename?")
        a2 = input("What is your key?")
        print(encode(a1,a2))
    elif answer == "d":
        a1 = input("What is your filename?")
        a2 = input("What is your key?")
        print(decode(a1,a2))
if __name__ == '__main__':
    main()
