#File name: plots.py
#Author username(s): jaltarr, howellma
#Date: 09/25/2017


def tribble_table(initial_pop , n_days):
    '''The function prints out the list of population and the corresponding days. 
    Parameters: initial_pop = (inital population)
                n_days = (number of days)
    '''
    print("{0:<5} | {1:<5}".format('day','Population'))
    print("{0:<5} | {1:<5}".format(0,initial_pop))
    for day in range(1,n_days+1):
        initial_pop = initial_pop + initial_pop//10
        print("{0:<5} | {1:<5}".format(day,int(initial_pop)))
def main():
    tribble_table(200,10)
main()