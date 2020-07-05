#File name: montecarlo.py
#Author Username(s): jaltarnr, zhengs
#Date: 10/2/17

import random
def pi_est(n):
    '''Uses sums of squares of points to estimate Pi
    Parameters: Number of times you want to iterate the function
    return value: approximation of pi'''
    hits = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if x**2 + y**2 < 1 :
            hits = hits + 1
        z = hits*4/n
    return z    
    
def flip():
    '''Simluates flipping of a coin
    Return values: Heads or Tails'''
    coin = round(random.random())
    total_count = 0
    head_count = 0
    tail_couns = 0
    if coin == 1:
        head_count = head_count + 1
        total_count = total_count + 1
        return "Heads"
    else:
        total_count = total_count + 1
        head_count = 0
        return "Tails"
    
def six_heads():
    '''Simlates a coin until you get six heads in a row
    Returns total number of times the coin was flipped to get 6 heads in a row'''
    total_count = 0
    head_count = 0
    tail_couns = 0
    while head_count < 6:    
        x = flip()
        if x == "Heads":
            head_count = head_count + 1
            total_count = total_count + 1
        else:
            total_count = total_count + 1
            head_count = 0
    return total_count

def average_six(n):
    '''Simlates n times of get six haeds in a row for coin
    Parameters: number of time you want to iterate the function
    Return calculate the average of the the results of n times of six_heads'''
    mylist = []
    for i in range(n):
        x = six_heads()
        mylist.append(x)
    z = sum(mylist)/n
    return z

def hhh():
    '''Simlates a coin until you get six heads in a row
    Returns total number of times the coin was flipped to get 6 heads in a row'''
    total_count = 0
    head_count = 0
    tail_couns = 0
    while head_count < 3:    
        x = flip()
        if x == "Heads":
            head_count = head_count + 1
            total_count = total_count + 1
        else:
            total_count = total_count + 1
            head_count = 0
    return total_count

def hht():
    total_count = 0
    head_count = 0
    tail_count = 0
    while head_count < 2:    
        x = flip()
        if x == "Heads":
            head_count = head_count + 1
            total_count = total_count + 1
        else:
            total_count = total_count + 1
            head_count = 0
    while tail_count < 1:
        x = flip()
        if x == "Tails":
            tail_count = tail_count + 1
            total_count = total_count + 1
        else:
            total_count = total_count + 1
            tail_count = 0
    return total_count

def simulate_flips(n):
    '''Simlates n times of get three haeds in a row for coin
    Parameters: number of time you want to iterate the function
    Return calculate the average of the the results of n times of hht()'''
    mylist = []
    for i in range(n):
        x = hht()
        mylist.append(x)
    z = sum(mylist)/n
    print(z)
    
    mylist1 = []
    for i in range(n):
        y = hhh()
        mylist1.append(x)
    t = sum(mylist1)/n
    print(t)
    

    
import random
import matplotlib.pyplot as pyplot
'''The followoing program gives a simulation of what is happening in the program pi_est. It takes some time to run when you give it larger values but it's only accurate for larger values. 
The parameters are :
n = number of iterations you want 
return value: a visual representation of pi_est '''
def pi_est_plot(n):
    list1 = []
    list2 = []
    mylist1 = []
    mylist2 = []
    
    for i in range(n):
        x1 = random.uniform(-1.5,1.5)
        y1 = random.uniform(-1.5,1.5)
        mylist1.append(x1)
        mylist2.append(y1)
        x = random.uniform(-1,1)
        y = random.uniform(-1,1)
        pyplot.scatter(x1,y1)
        
        if x**2 + y**2 < 1:

            list1.append(x)
            list2.append(y)
        
    pyplot.axis([-1.5,1.5,-1.5,1.5])
    pyplot.plot(list1,list2)
    pyplot.show()

    
    

    
    

