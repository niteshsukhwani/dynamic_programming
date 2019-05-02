"""
@author: Nitesh
"""

"""The following function takes 2 strings st1 and st2 as input and 
outputs the longest common subsequence. 
"""
import numpy as np
import re

def Count_LCS(st1,st2):
    n1 = len(st1)
    n2 = len(st2)
    mat = np.zeros((n1+1,n2+1))
    for i in range(n1):
        for j in range(n2):
            if st1[i]==st2[j]:
                mat[i+1,j+1]=1+mat[i,j]
            else:
                mat[i+1,j+1]=max(mat[i,j+1],mat[i+1,j])
    return mat

def lcs(st1, st2):
    s =""
#your code goes here, replace the "pass' with your code pass
    st1 = re.sub(r'\W+', '', st1)
    st2 = re.sub(r'\W+', '', st2)
    mat = Count_LCS(st1,st2)
    lst=[]
    i = len(st1)
    j = len(st2)
    n = mat[i,j]
    while n!=0:
        if mat[i,j]==mat[i-1,j]:
            i-=1
        elif mat[i,j]==mat[i,j-1]:
            j-=1
        else:
            i-=1
            j-=1
            lst.append(st1[i])
        n = mat[i,j]
    lst.reverse()
    s = ''.join(lst)
#The string variable s stores the lcs of strings st1 and st2. 
    return s
