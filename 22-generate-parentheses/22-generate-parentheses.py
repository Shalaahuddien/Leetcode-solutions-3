class Solution:
    def rec(self, n, ans, temp, op, cl):
        if(cl==n and op==n):
            ans.append(temp)
            return
        elif(op==0 or op==cl):
            self.rec(n, ans, temp+"(", op+1, cl)
        elif(op==n):
            self.rec(n, ans, temp+")", op, cl+1)
        else:
            self.rec(n, ans, temp+"(", op+1, cl)
            self.rec(n, ans, temp+")", op, cl+1)
        
        
        
    def generateParenthesis(self, n: int) -> List[str]:
        ans=[]
        self.rec(n, ans, "", 0, 0)
        return ans