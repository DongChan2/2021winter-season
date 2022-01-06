#Library import
import numpy as np 
import math
import matplotlib.pyplot as plt

def tridiag(a1,b1,c1,c,rhs):
    rhs[1]=rhs[1]-a1[1]*c[0]
    rhs[m-1]=rhs[m-1]-c1[m-1]*c[m]    

    #Thomas Algorithm
    for i in range(2,m):
        r=a1[i]/b1[i-1]
        b1[i]=b1[i]-r*c1[i-1]
        rhs[i]=rhs[i]-r*rhs[i-1]

    rhs[m-1]=rhs[m-1]/b1[m-1]
    for i in range(m-2,0,-1):
        rhs[i]=(rhs[i]-c1[i]*rhs[i+1])/b1[i]
        
    return rhs        
    

#Definitions and initializations of variable arrays

m=100
v=1.0
dt=0.02
dx=1.0
nmax=2500

#Definitions and initializations of variable arrays
x=np.zeros(shape=m+1)
c=np.zeros(shape=m+1)
rhs=np.zeros(shape=m+1)
c0=np.zeros(shape=m+1)
a1=np.zeros(shape=m+1)
b1=np.zeros(shape=m+1)
c1=np.zeros(shape=m+1)
ce=np.zeros(shape=m+1)
#Selection of scheme
print("""if alpha=1 is central scheme, alpha=0 is backward scheme
if theta=0 is Explicit Method, theta=0.5 is Crank-Nicolson implicit, theta=1 is Fully Implicit Method""")      
alpha=float(input("Input alpha: "))
theta=float(input("Input theta: "))
pe=float(input("Input Pe value: "))
if theta>0:
    scheme=1 #fully implicit method,C-N method
else:
    scheme=2 #explicit method   

#when i=1 its distance is at (1*dx)m from origin

for i in range(0,m+1):
    x[i]=i*dx

#Initial Condition
for i in range(0,m+1):
    if i==0:
        c[i]=1.0
    else:
        c[i]=0.0
#save the initial condition

for i in range(0,m+1):
    c0[i]=c[i]

d1=((pe*(1.0-theta)*alpha+2*pe*(1.0-alpha)*(1.0-theta)+2*(1.0-theta))*v)/(2*pe*dx)
e1=(1/dt)-((pe*(1-alpha)+2)*v*(1-theta))/(pe*dx)
f1=((2-alpha*pe)*v*(1-theta))/(2*pe*dx)

#Time integral(Time marching)
for iter in range(1,nmax+1):
    if iter==round(iter/100)*100:
        print("{0}".format(iter))    
   
    if scheme==1:
        for i in range(1,m):
            a1[i]=float((pe*alpha-2*pe-2)*v*theta/(2*pe*dx))
            b1[i]=float((1/dt)+((1-alpha)*v*theta)/dx+(2*v*theta)/(pe*dx))
            c1[i]=float(((alpha*pe-2)*v*theta)/(2*pe*dx))  
            rhs[i]=d1*c[i-1]+e1*c[i]+f1*c[i+1]
            
        rhs=tridiag(a1,b1,c1,c,rhs)
            
            #renewal of concentration at the next time step
        for i in range(1,m):
            c[i]=rhs[i]
        #explicit method   
    elif scheme==2:
        for i in range(1,m):
            b1[i]=float((1/dt)+((1-alpha)*v*theta)/dx+(2*v*theta)/(pe*dx))
            rhs[i]=d1*c[i-1]+e1*c[i]+f1*c[i+1]
            c[i]=rhs[i]/b1[i]
                    
    #renewal of boundary conditions
    c[0]=1.0
    c[m]=c[m-1]

for i in range(0,m+1):
    d=v*dx/pe       
    y1=(x[i]-v*dt*nmax)/(2*math.sqrt(d*dt*nmax))
    y2=(x[i]+v*dt*nmax)/(2*math.sqrt(d*dt*nmax))
    ce[i]=c[0]/2*(math.erfc(y1)+math.exp(v*x[i]/d)*math.erfc(y2))    

 
#Plot of numerical solution
#print plots
plt.figure(figsize=(30,10),dpi=60)
plt.subplot(121)
plt.title('Initial Condition',fontsize=30)
plt.plot(x,c0,'b^',label='Initial Condtion')
plt.legend(fontsize=20)
plt.xlabel("Time",fontsize=30)
plt.ylabel('Concentration',fontsize=30)
plt.xticks(size=20)
plt.yticks(size=20)
plt.axis([0,100,0,1])


plt.subplot(122)
plt.title('Advection-diffusion Equation',fontsize=30)
plt.plot(x,c,'ko',label='Numerical Solution')
plt.plot(x,ce,'r--',label='Exact Solution')
plt.legend(fontsize=20)
plt.xlabel("Time",fontsize=30)
plt.ylabel('Concentration',fontsize=30)

plt.xticks(size=20)
plt.yticks(size=20)
plt.axis([0,100,0,1])
plt.grid(True)
plt.savefig("result.jpg")
plt.show()

 