# Print numbers from 1 to N without the help of loops
def printNos(self,N):
        if N >0:
            self.printNos(N-1)
            print(N,end=' ')
