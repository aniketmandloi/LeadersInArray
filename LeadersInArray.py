class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self, A, N):
        ans=[]
        maxx=A[N-1]
    
        #We start traversing the array from last element.
        for i in range(N-1,-1,-1):
            #Comparing the current element with the maximum element stored. 
            #If current element is greater than max, we add the element.
            if A[i]>=maxx:
                #Updating the maximum element.
                maxx=A[i]
                #Appending the current element.
                ans.append(maxx)
                
        #Reversing the array.
        ans.reverse()
        #returning the answer.
        return ans
