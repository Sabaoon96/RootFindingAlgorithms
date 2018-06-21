from math import exp, log

# Function to find roots of
def f(x):
	# return 20*x**3 - 50*x**2 + 3*x + 20 	
	# return log(x) - 1 + exp(-x)
	return exp(0.5*x) - exp(0.6*x) + 4 	 
	
# Derivation of function	
def df(x):
	# return 60*x**2 - 100*x + 3 	
	# return (1/x) - exp(-x)) 
	return 0.5*exp(0.5*x) - 0.6*exp(0.6*x) 	


def main():
	# Given parameters	
	initial = 0
	tolerance = 0.0001

	# Initialising iteration counter
	value = 0

	# Using to compute |x_{i} − x_{i−1}|
	next = initial - (f(initial) / df(initial))
	diff = abs(next - initial)

	# Printing initial two lines of output
	print("Iteration    " + "Xi         " + "f(Xi)")
	print("0           ", '{:.5f}'.format(initial), "  ", '{:.5f}'.format(f(initial))) #Formatting floats to 5 decimal places

	while not (diff <= tolerance):
		value += 1
		next = initial - (f(initial) / df(initial))
		diff = abs(next - initial)
		initial = next
		if not (diff <= tolerance):
			print(value, "          ", '{:.5f}'.format(next), "  ", '{:.5f}'.format(f(next)))
main()
	