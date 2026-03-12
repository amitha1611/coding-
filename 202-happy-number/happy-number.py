class Solution(object):
    def isHappy(self, n):
        while n!=1 and n!=4:
            total=0
            while n>0:
                digit=n%10
                total+=digit*digit
                n=n//10
            n=total
        return n==1    
        