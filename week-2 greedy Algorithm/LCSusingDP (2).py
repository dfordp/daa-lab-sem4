#LCS using DP


import time

def LCS(X,Y,m,n):
  if(m==0 or n==0):
    return 0
  elif X[m-1]==Y[n-1]:
    return 1+LCS(X,Y,m-1,n-1)
  else:
    return max(LCS(X,Y,m,n-1),LCS(X,Y,m-1,n))
    

X="AGGTAB"
Y="GYTYAYB"
start=time.time()
x=LCS(X,Y,len(X),len(Y))
end=time.time()
print(x)
print((end-start)*10**3,"ms")
