#Trying an example
from mdp import *
# from CustomMDP import *

sample_sequential_decision_environment = GridMDP([[-0.04, -0.04, -0.04, +1],
                                           [-0.04, None, -0.04, -1],
                                           [-0.04, -0.04, -0.04, -0.04]],
                                          terminals=[(3, 2), (3, 1)])


print('\n\n\n\n')
# runs valIt with sample
V = value_iteration(sample_sequential_decision_environment, .01)
print("Value Iteration: ", V)

print('\n\n\n\n')

P = policy_iteration(sample_sequential_decision_environment)
print("Policy Iteration: ", P)

print('\n\n\n\n')
