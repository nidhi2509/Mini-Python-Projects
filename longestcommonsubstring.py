def lcs(S,T):
   

    
    mydict = [[0]*(len(T)+1) for x in range((len(S))+1)]
    
    longcs = 0
    lcs_set = set()
    for i in range(len(S)):
        for j in range(len(T)):
            if S[i] == T[j]:
                count = mydict[i][j] + 1
                mydict[i+1][j+1] = count
                if count > longcs:
                    lcs_set = set()
                    longcs = count
                    lcs_set.add(S[i-count+1:i+1])
                elif count == longcs:
                    lcs_set.add(S[i-count+1:i+1])

    return lcs_set

