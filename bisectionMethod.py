# Function to find roots of
def f(x):
    return (20*x**3 - 50*x**2 + 3*x + 20) 

# Given values of a and b, interval where function f is defined.
a = 0.0
b = 1.0

# Given tolerance
tolerance = 0.0001

# Printing initial line of output
print("Iteration", "     ", "a", "         ", "b", "        ", "f(c)")
 
# Bisection method function
def bisection(a, b, f, tolerance): 
	iter = 0                    # Iteration counter
	max = 50                    # Ensuring algorithm doesn't run too long
	while iter < max:
		midpt = (a + b)/2       # Calculating mid-point
		func_mid = f(midpt)
		result = print(iter, "          ", '{:.5f}'.format(a), "   ", '{:.5f}'.format(b), "   ", '{:.5f}'.format(func_mid))
		if (abs(b - a) < tolerance):
			break
		iter += 1
		if f(a) * func_mid > 0: # Checking for signs (+ or -)
			a = midpt
		else:
			b = midpt
	return result
	
bisection(a, b, f, tolerance)
