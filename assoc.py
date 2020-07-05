multoperator = {
  'a': {'a':'b', 'b':'b', 'c':'a'},
  'b': {'a':'c', 'b':'b', 'c':'a'},
  'c': {'a':'a', 'b':'c', 'c':'c'},
}

print("The multiplication table:")

print ("LHS\RHS  a  b  c")
for x in ['a', 'b', 'c']:
  print("  " + x + ":     ", end='')
  for y in ['a', 'b', 'c']:
    print(multoperator[x][y], end='  ')
  print()

    
dict1 = {}
    
def solutions(s):
    list1 = []
    
    n = len(s)
    
    if n == 2:
        
        answer = (multoperator[s[0]][s[1]])
        return answer
    
        
    if s in dict1:
        return dict1[s]

    else:
        for i in range(1,n):
            l = solutions(s[:i])
            r = solutions(s[i:])
            
            for x in l:
                for y in r:
                    list1.append(multoperator[x][y])
               
        dict1[s] = set(list1)    
        return set(list1)
    