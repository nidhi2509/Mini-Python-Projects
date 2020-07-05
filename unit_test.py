"""
Make sure to fill in the following information before submitting your
assignment. Your grade may be affected if you leave it blank!
For usernames, make sure to use your Whitman usernames (i.e. exleyas). 
File name: unit_test.py
Author username(s): lepejirs, jaltarnr
Date: 10/25/17
"""



def get_int(text):
    '''
    Returns the first numeric value within the string, or -1 if none
    exists. Only search for digits 0, 1, 2, 3, 4, 5, 6, 7, 8, 9. Do not
    consider minus sign (-) and decimal points (.) as part of the
    numeric value.

    Preconditions: text is a string
    Postconditions: returns an int
    '''
    assert isinstance(text,str), "The text should be a string."
    
    c = ""
    
    for i in text:
        if 47 < ord(i) < 58:
            c = c + i
        elif c != "":
            return int(c)
        elif c == "":
            continue
    if c == "":
        return -1
    return int(c)

def test_get_int():
    # common cases
    assert get_int('hello 10 hello') == 10
    assert get_int('12 hello') == 12
    assert get_int('hihi 21') == 21
    assert get_int('hello hello') == -1
    assert get_int('a14671825b') == 14671825

    # boundary cases
    assert get_int('') == -1
    assert get_int('12 hello 34') == 12
    assert get_int('9') == 9
    assert get_int('-8') == 8
    assert get_int('2.4') == 2
    assert get_int(' 56 78 9134') == 56

    # corner cases
    assert get_int('sasgjakghakjlhga\nsajglh\n\n\n\n\nagjkljghs3bdfdafbfb') == 3

def test_get_float():
    # common cases
    assert get_float('hello 100.5 hello') == 100.5
    assert get_float('-12 hello') == -12
    assert get_float('hihi -21.5 friday') == -21.5
    assert get_float('h-e.llo .h-1e0.llo') == -1
    assert get_float('a146.71825b') == 146.71825

    # boundary cases
    assert get_float('aaaaaaaaaaaaaaaaaaaaaaaahasdfasdfasdf') == None
    assert get_float('') == None
    assert get_float('-12.743439 hello 34') == -12.743439
    assert get_float('adfhassfuhae;.---.adsfga..-8') == -8
    assert get_float('2.-as-d-f-.sad-.fa.-sdf difjaspf4') == 2
    assert get_float(' hi 56.56 78 9134 jello') == 56.56

    # corner cases
    assert get_float('sasgjakghakjlhga\nsajglh\n\n\n\n\nagjkljghs-3.6bdfdafbfb') == -3.6 
    