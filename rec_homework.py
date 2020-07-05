"""
Make sure to fill in the following information before submitting your
assignment. Your grade may be affected if you leave it blank!
For usernames, make sure to use your Whitman usernames (i.e. exleyas). 
File name: sierpinski.py
Author username(s): harristr jaltarnr
Date: Dec. 4, 2017
"""

import turtle
import math


def sierpinski(tr, p1, p2, p3, depth):
    '''
    Draws a Sierpinski triangle with corners at p1, p2, and p3.

    Preconditions:
       tr is a turtle object to use to draw with
       p1 is a tuple that is the first corner of the triangle
       p2 is a tuple that is the second corner of the triangle
       p3 is a tuple that is the third corner of the triangle
       depth is an int that is the recursion depth
   
    Postconditions: None
    '''
    
    assert isinstance(tr, turtle.Turtle), 'tr must be a turtle object'
    assert isinstance(p1, tuple) and len(p1) == 2, 'p1 must be a tuple with 2 elements'
    assert isinstance(p2, tuple) and len(p2) == 2, 'p2 must be a tuple with 2 elements'
    assert isinstance(p3, tuple) and len(p3) == 2, 'p3 must be a tuple with 2 elements'
    assert isinstance(depth, int) and depth >= 0, 'depth must be a non-negative int'
        
    if depth == 0:
        tr.goto(p2)
        tr.down()
        tr.goto(p3)
        tr.goto(p1)
        tr.goto(p2)
        tr.up()
    
    else:        
        sierpinski(tr, p1, ((p2[0] + p1[0]) / 2, (p2[1] + p1[1]) / 2), ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2), depth - 1)   #Draw first sub-triangle
        
        tr.goto(((p2[0] + p1[0]) / 2, (p2[1] + p1[1]) / 2)) #Move to mid of p1 and p2
        
        sierpinski(tr, ((p2[0] + p1[0]) / 2, (p2[1] + p1[1]) / 2), p2, ((p3[0] + p2[0]) / 2, (p3[1] + p2[1]) / 2), depth - 1)   #Draw second sub-triangle
        
        tr.goto(((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)) #Move to mid of p1 and p3
        #tr.pendown()
        
        sierpinski(tr, ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2), ((p3[0] + p2[0]) / 2, (p3[1] + p2[1]) / 2), p3,  depth - 1)  #Draw third sub-triangle
        
        tr.goto((p1))   #Move to initial position
        #tr.pendown()
    

def subsets(aset):
    '''Recursive function that returns a list of all subsets of aset

    Preconditions:
        aset is a list

    Postconditions:
        returns a list of lists
    '''
    if aset == []:
        return [[]]
    sublist = subsets(aset[1:])
    for y in sublist:
        sublist = sublist + [[aset[0]] + y]
    return sublist

def main():
    """
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    sierpinski(t, (-100, -60), (0, 100), (100, -60), 4)
    sc = t.getscreen()
    sc.exitonclick()"""
    
    print(subsets([1, 2, 3,4,5]))

if __name__ == '__main__':
    main()
