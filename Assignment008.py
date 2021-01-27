import numpy as np
import matplotlib.pyplot as plt
import math


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB



#vertices
D = np.array([0,0])
E = np.array([5,0])
F = np.array([0,3])


#Generating all lines
x_DE = line_gen(D,E)
x_EF = line_gen(E,F)
x_FD = line_gen(F,D)


#Plotting all lines
plt.plot(x_DE[0,:],x_DE[1,:],label='$DE$')
plt.plot(x_EF[0,:],x_EF[1,:],label='$EF$')
plt.plot(x_FD[0,:],x_FD[1,:],label='$FD$')


plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 - 0.1), D[1] * (1) , 'D')
plt.plot(E[0], E[1], 'o')
plt.text(E[0] * (1 ), E[1] * (1+0.1) , 'E')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 - 0.3), F[1] * (1 - 0.1) , 'F')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid()
plt.axis('equal')
plt.plot()
plt.show()