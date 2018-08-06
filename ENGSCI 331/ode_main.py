# imports
import numpy as np
from matplotlib import pyplot as plt
from ode_functions import*

#####################################################################################################

# # Define a function to calc derivatives for y(x)=-cos(x) => y'(x)=sin(x)
# def fsin(x,y): return np.sin(x)

# # Set up initial conditions, and solve using our numerical method of choice
# x0=0
# y0=-1
# x1=3
# h=0.1
# xvalues,yvalues = euler_solve(fsin, x0, y0, x1, h)
# # xvalues,yvalues = improved_euler_solve(fsin, x0, y0, x1, h)
# # xvalues,yvalues = runge_kutta_solve(fsin, x0, y0, x1, h)

# # Create a plot with sub-plots
# f,(ax1, ax2) = plt.subplots(1,2)
# f.set_size_inches([16,5])

# # add our first plot comparing our numerical results with the true y(x)
# # See https://matplotlib.org/api/_as_gen/matplotlib.pyplot.plot.html for plot options
# ax1.plot(xvalues,list(-np.cos(x) for x in xvalues), 'r--', label = "ytrue") # plot true y
# ax1.plot(xvalues,yvalues, 'bx-', label = "y", linestyle = 'None') # plot y
# ax1.legend(loc=0) # place legend: 0='best', 1=top-right, 2=top-left, etc
# ax1.set_xlabel('x')
# ax1.set_ylabel('y')
# ax1.set_title('Numerical and Exact Solutions for y(x)=-cos(x)')

# #####################################################################################################

# # Define a function to calc derivatives for y(x)=sin(ax)/a => y'(x)=cos(ax), y''(x)=-a*sin(ax)
# # y''+a^2 y = 0 when in system form: 
# # y[0] = y, y[1]=y', so (y[0])'=y[1], (y[1])'=-4*y[0]
# # Note: 'a' will be passed into this function when it is called
# def fsample(x,y,a): return np.array( [y[1], -a*a*y[0]] )

# # Define initial conditions appropriate for our fsample() function, final x, and step size
# a = 2
# x0 = 0
# y0 = np.array( [np.sin(a*x0)/a, np.cos(a*x0)] )
# x1=3
# h=0.1

# # Solve using our numeric method of choice
# xvalues,yvalues = euler_solve(fsample, x0, y0, x1, h, a)
# # xvalues,yvalues = improved_euler_solve(fsample, x0, y0, x1, h, a)
# # xvalues,yvalues = runge_kutta_solve(fsample, x0, y0, x1, h, a)

# # Create the second plot showing the real function, and our numerical function and derivative estimates
# ax2.plot(xvalues,list(np.sin(a*x)/a for x in xvalues), 'r--', label = "ytrue") # plot true y
# ax2.plot(xvalues,list(y[0] for y in yvalues), 'bx-', label = "y[0]", linestyle = 'None') # plot y[0]
# ax2.plot(xvalues,list(y[1] for y in yvalues), 'g--', label = "y[1]") # plot y[1]
# ax2.legend(loc=0) # place legend: 0=best, 1=top-right, 2=top-left, etc
# ax2.set_xlabel('x')
# ax2.set_ylabel('y')
# ax2.set_title('Numerical and Exact Solutions for y(x)=sin(ax)/a')

# #plt.show()
# # uncomment this command (and comment the show command) to save a copy of your figure
# # plt.savefig('lab2_task1_euler.png', dpi = 300)


# # define initial conditions
# # estimate vertical position and velocity over interval t = 0s to t = 50s



# # Plots:
# # Vertical position vs time (positive x is down)
# # Vertical velocity vs time (positive velocity is down) (ax1.invert_yaxis())
# # Phase plot with position, x, on x axis, and velocity, v, on y axis.

# def bungee_jumper_derivative(t, y, L, g, m, cd, k, gamma) :
# 	x = y[0]
# 	if x >= L :
# 		return np.array( [y[1], g - np.sign(y[1])*(cd/m)*y[1]**2 - (k/m)*(y[0]-L) - (gamma/m)*y[1]] )
# 	else:
# 		return np.array( [y[1], g - np.sign(y[1])*(cd/m)*y[1]**2] )

# t0 = 0
# t1 = 50
# h = 0.1
# y0 = np.array( [0,0] )

# L = 30 # units: m
# g = 9.81 # m/s^2
# m = 68.1 # kg
# cd = 0.25 # kg/m
# k = 40 # N/m
# gamma = 8 # Ns/m

# tvalues,yvalues = runge_kutta_solve(bungee_jumper_derivative, t0, y0, t1, h, L, g, m, cd, k, gamma)

# # Create a plot with three sub-plots
# f2,(ax3, ax4) = plt.subplots(1,2)
# f2.set_size_inches([16,5])

# # Second plot
# ax3.plot(tvalues,list(y[0] for y in yvalues), 'bx-', label = "y[0]", linestyle = 'None') # plot y[0]
# ax3.plot(tvalues,list(y[1] for y in yvalues), 'g--', label = "y[1]") # plot y[1]
# ax3.legend(loc=0) # place legend: 0=best, 1=top-right, 2=top-left, etc
# ax3.set_xlabel('t')
# ax3.set_ylabel('y')
# ax3.set_title('Numerical Solutions')

# print(type(tvalues))
# print(type(yvalues))

# yvalues = np.transpose(yvalues)

# # positionVec = list(y[0] for y in yvalues)
# # velocityVec = list(y[0] for y in yvalues)
# ax4.plot(yvalues[0], yvalues[1], 'g--') # plot y[1]
# # ax4.legend(loc=0) # place legend: 0=best, 1=top-right, 2=top-left, etc
# # ax4.set_xlabel('x')
# # ax4.set_ylabel('v')
# # ax4.set_title('Numerical and Exact Solutions for y(x)=sin(ax)/a')

# # plt.show()





def fakenews_derivative(t,y,Pw,Pb,Pf,Pt,Pl):
	# y : {H', M', D', S'}
	y[y < 0] = 0

	H = y[0]
	S = y[1]
	M = y[2]
	D = y[3]

	dHdt = Pt*(S+M) - Pw*H*M - Pl*H + Pf*D
	dSdt = Pw*H*M - S*(Pt + Pl + Pb)
	dMdt = Pb*S - M*(Pt + Pl)
	dDdt = Pl*(H + S + M) - Pf*D

	return np.array([dHdt, dSdt, dMdt, dDdt])

Pw = 0.1
Pb = 0.1
Pf = 0
Pt = 0
Pl = 0

t0 = 0
t1 = 100
y0 = np.array( [999,1,0,0] )
h = 0.01

tvalues, yvalues = runge_kutta_solve(fakenews_derivative, t0, y0, t1, h, Pw, Pb, Pf, Pt, Pl)

f1,(ax1,ax2,ax3) = plt.subplots(1,3)
f1.set_size_inches([16,5])

# Create the second plot showing the real function, and our numerical function and derivative estimates
[H,S,M,D] = ax1.plot(tvalues, yvalues)
ax1.legend(['Humans', 'Sensation Seekers', 'Muppets', 'Disengaged'], loc = 0)

Pl = 0.01
t1 = 1000

tvalues2, yvalues2 = runge_kutta_solve(fakenews_derivative, t0, y0, t1, h, Pw, Pb, Pf, Pt, Pl)
[H,S,M,D] = ax2.plot(tvalues2, yvalues2)
ax2.legend(['Humans', 'Sensation Seekers', 'Muppets', 'Disengaged'], loc = 0)

Pl = 0
Pt = 0.1
t1 = 50
tvalues3, yvalues3 = runge_kutta_solve(fakenews_derivative, t0, y0, t1, h, Pw, Pb, Pf, Pt, Pl)
[H,S,M,D] = ax3.plot(tvalues3, yvalues3)
ax3.legend(['Humans', 'Sensation Seekers', 'Muppets', 'Disengaged'], loc = 0)

plt.show()