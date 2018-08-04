# imports
import numpy as np

# this function is complete, do not modify it
def euler_solve(f, x0, y0, x1, h, *args):
	''' Compute solution to ODE using Euler method
	
		inputs
		------
		f : callable
			derivative function which, for any input x and ya, yb, yc, ... values, returns a tuple of derivative values
		x0 : float
			initial value of independent variable
		y0 : a float, or a numpy array of floats
			array of initial values of solution variables (ya, yb, yc, ...)
		x1 : float
			final value of independent variable
		h : float
			step size
		*args : '*args' optional parameters
			optional parameters to pass to derivative function f()
			
		returns
		-------
		a list, xs, that gives each of the x values where the solution has been estimated
		a list of numpy arrays, where each array is an estimate of the solution (ya, yb, yc, ...) at the corresponding x value
	'''

	# initialise
	n = int(np.ceil((x1-x0)/h))	        # number of Euler steps to take
	xs = [x0+h*i for i in range(n+1)]	# x's we will evaluate function at
	ys = [y0]						    # list to store solution; we will append to this
	
	# iteration
	for k in range(n):
		ys.append( euler_step(f, xs[k], ys[k], h, *args) )

	return xs, ys

# this function is complete, do not modify it
def euler_step(f, xk, yk, h, *args):
	''' Compute a single Euler step.
	
		inputs
		------
		f : callable
			derivative function
		xk : float
			independent variable at beginning of step
		yk : a float, or a numpy array of floats
			solution at beginning of step
		h : float
			step size
		*args : '*args' optional parameters
			optional parameters to pass to derivative function 
			
		returns
		-------
		a float, or a numpy array of floats, giving solution at end of the step
	'''
	return yk + h*f(xk,yk,*args)

################################################################################################################

# **this function is incomplete, you must complete it as part of the lab task**
#def improved_euler_solve
#def improved_euler_step

# **this function is incomplete, you must complete it as part of the lab task**	
def improved_euler_solve(f, x0, y0, x1, h, *args):
	''' Compute solution to ODE using improved Euler method
	
		inputs
		------
		f : callable
			derivative function which, for any input x and ya, yb, yc, ... values, returns a tuple of derivative values
		x0 : float
			initial value of independent variable
		y0 : a float, or a numpy array of floats
			array of initial values of solution variables (ya, yb, yc, ...)
		x1 : float
			final value of independent variable
		h : float
			step size
		*args : '*args'optional parameters
			optional parameters to pass to derivative function f()
	
		returns
		-------
		a list, xs, that gives each of the x values where the solution has been estimated
		a list of numpy arrays, where each array is an estimate of the solution (ya, yb, yc, ...) at the corresponding x value
	'''

	# initialise
	n = int(np.ceil((x1-x0)/h))	        # number of Euler steps to take
	xs = [x0+h*i for i in range(n+1)]	# x's we will evaluate function at
	ys = [y0]						    # list to store solution; we will append to this
	
	# iteration
	for k in range(n):
		ys.append( improved_euler_step(f, xs[k], ys[k], h, *args) )

	return xs, ys
	
		
# **this function is incomplete, you must complete it as part of the lab task**
def improved_euler_step(f, xk, yk, h, *args):
	''' Compute a single improved Euler step.
	
		inputs
		------
		f : callable
			derivative function
		xk : float
			independent variable at beginning of step
		yk : a float, or a numpy array of floats
			solution at beginning of step
		h : float
			step size
		*args : '*args' optional parameters
			optional parameters to pass to derivative function 
			
		returns
		-------
		a float, or a numpy array of floats, giving solution at end of the step
	'''
	
	ye = yk + h*f(xk,yk,*args)
	fi = f(xk,yk,*args)
	fe = f((xk + h),ye,*args)

	return yk + (h/2)*(fi + fe)
	

################################################################################################################

# **this function is incomplete, you must complete it as part of the lab task**
#def improved_euler_solve
#def improved_euler_step

# **this function is incomplete, you must complete it as part of the lab task**	
def runge_kutta_solve(f, x0, y0, x1, h, *args):
	''' Compute solution to ODE using the clasical 4th order Runge Kutta method
	
		inputs
		------
		f : callable
			derivative function which, for any input x and ya, yb, yc, ... values, returns a tuple of derivative values
		x0 : float
			initial value of independent variable
		y0 : a float, or a numpy array of floats
			array of initial values of solution variables (ya, yb, yc, ...)
		x1 : float
			final value of independent variable
		h : float
			step size
		*args : '*args' optional parameters
			optional parameters to pass to derivative function f()
	
		returns
		-------
		a list, xs, that gives each of the x values where the solution has been estimated
		a list of numpy arrays, where each array is an estimate of the solution (ya, yb, yc, ...) at the corresponding x value
	'''
	
	# initialise
	n = int(np.ceil((x1-x0)/h))	        # number of Euler steps to take
	xs = [x0+h*i for i in range(n+1)]	# x's we will evaluate function at
	ys = [y0]						    # list to store solution; we will append to this
	
	# iteration
	for k in range(n):
		ys.append( runge_kutta_step(f, xs[k], ys[k], h, *args) )

	return xs, ys
		
# **this function is incomplete, you must complete it as part of the lab task**
def runge_kutta_step(f, xk, yk, h, *args):
	''' Compute a single Runge Kutter step.
	
		inputs
		------
		f : callable
			derivative function
		xk : float
			independent variable at beginning of step
		yk : a float, or a numpy array of floats
			solution at beginning of step
		h : float
			step size
		*args : '*args' optional parameters
			optional parameters to pass to derivative function 
			
		returns
		-------
		a float, or a numpy array of floats, giving solution at end of the step
	'''
	f0 = f(xk, yk, *args)
	f1 = f((xk + 0.5*h), (yk + 0.5*h*f0), *args)
	f2 = f((xk + 0.5*h), (yk + 0.5*h*f1), *args)
	f3 = f((xk + h), (yk + h*f2), *args)

	return yk + (h/6)*(f0 + 2*f1 + 2*f2 + f3)
