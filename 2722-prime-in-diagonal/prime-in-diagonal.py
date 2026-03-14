class Solution(object):
    def diagonalPrime(self, nums):
        n=len(nums)
        max_prime=0
        for i in range(n):
            a=nums[i][i]
            b=nums[i][n-i-1]
            if self.isPrime(a):
                max_prime=max(max_prime,a)
            if self.isPrime(b):
                max_prime=max(max_prime,b)
        return max_prime
    def isPrime(self,n):
        if n<=1:
            return False
        for i in range(2,int(n**0.5)+1):
            if n%i==0:
                return False
        return True 
        
        