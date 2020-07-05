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
    print(subsets([1,2]))
    

if __name__ == '__main__':
    main()
