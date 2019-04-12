#Sequence Learning Problem
from numpy import array

# generate a sequence of real values between 0 and 1.
def generate_sequence(length=10):
	return array([i/float(length) for i in range(length)])

print(generate_sequence())

#####################################

def generate_sequence(length=5):
	return [i for i in range(length)]

# sequence 1
seq1 = generate_sequence()
seq1[0] = seq1[-1] = seq1[-2]
print(seq1)
# sequence 2
seq1 = generate_sequence()
seq1[0] = seq1[-1]
print(seq1)

## This framing of the problem would be modeled as a many-to-one sequence prediction problem.
## Again, this problem could not be learned by a multilayer Perceptron.

######################################

