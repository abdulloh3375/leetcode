
class Solution:
    def fib(self, n: int) -> int:
        
        if n < 2:
            return n
        else:
            return self.fib(n-1) + self.fib(n-2)
        



# *************** or *************************

class Solution:
    def fib(self, n: int) -> int:
       
        if n==0:
            return 0
        index = [-1]*(n+1)
        index[0] = 0
        index[1] = 1
        
        for i in range(2, n+1):
            index[i] = index[i-1] + index[i-2]
       
        return index[n]