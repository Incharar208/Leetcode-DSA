#GFG Question
def printFirstNegativeInteger( A, N, K):
    queueArray=[]
    resultArray=[]
    i=j=0
    while j<N:
        if A[j]<0:
            queueArray.append(A[j])
        
        if (j-i+1)<K:
            j=j+1
        elif (j-i+1)==K:
            if len(queueArray)==0:
                resultArray.append(0)
            else:
                resultArray.append(queueArray[0])
                if queueArray[0]==A[i]:
                    queueArray.pop(0)
                    
            j=j+1
            i=i+1
            
    return resultArray        
            
