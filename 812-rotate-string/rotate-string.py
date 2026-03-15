class Solution(object):
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False
        
        temp = s + s
        return goal in temp
        