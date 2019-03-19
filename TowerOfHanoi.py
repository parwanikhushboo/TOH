def TOH(n,A,B,C): 
    if n == 1: 
        print ("Move disk 1 from rod "+A+" to rod "+B)
        return
    TOH(n-1,A,C,B) 
    print ("Move disk "+str(n)+" from rod "+A+" to rod "+B)
    TOH(n-1,C,B,A)


n=int(input('Enter the number of discs'))
TOH(n,"A","B","C")  
