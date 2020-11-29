#Trying an example
from mdp import *
from reinforcement_learning import *
# from CustomMDP import *

#note: check out the tests folder to see how all given functions are ran
sample_sequential_decision_environment = GridMDP(
    [
        [-0.04, -0.04, -0.04, +1],
        [-0.04, None, -0.04, -1],
        [-0.04, -0.04, -0.04, -0.04]
    ],
    terminals=
    [
        (3, 2), 
        (3, 1)
    ]
)

# GridMDP (Grid, terminals, initial, gama)
# grid[reward]

shopping_world = GridMDP(
    [
        # east, north, west, south
        [0.10, 1],  #11
        [0.9, 2],   #10
        [0.8, 3],   #9
        [0.7, 4],   #8
        [0.6, 5],   #7
        [0.5, 6],   #6
        [0.4, 7],   #5
        [0.3, 8],   #4
        [0.2, 9],   #3
        [0.1, 10],  #2
        [11, 11],   #1
    ],
    terminals=
    [
        (1,0), 
        (1,1), 
        (1,2),
        (1,3), 
        (1,4), 
        (1,5),
        (1,6), 
        (1,7), 
        (1,8),
        (1,9), 
        (1,0)
    ]
)

# runs valIt with sample
V = value_iteration(shopping_world, .01)
print("Value Iteration: ", V, '\n')


P = policy_iteration(shopping_world)
print("Policy Iteration: ", P, print('\n'))



"""QLearner notes
north = (0, 1)
south = (0,-1)
west = (-1, 0)
east = (1, 0)

q_agent.Q[(STATE, ACTION)]
so.. in state (0,1) take action north (0,1)
THAT qvalue (remember 4 for each node) is...
q_agent.Q[((0, 1), (0, 1))]
"""
# Ne was 5 now 2
# q_agent = QLearningAgent(shopping_world, Ne=5, Rplus=2, alpha=lambda n: 60. / (59 + n))

# for i in range(50):
#     run_single_trial(q_agent, shopping_world)
#     Qval = q_agent.Q[((0, 0), (1, 2))] #described above what is happening here
#     # A1 = q_agent.Q[((0, 1), (0, 1))]
#     # A2 = q_agent.Q[((1, 0), (0, -1))]
#     print("Qlearner: ", Qval, print('\n\n'))

