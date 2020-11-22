from world import *
from CustomMDP import *
from Transitions import * 
from mdp import *

# for state in world1:
#     print(state)

our_mdp = CustomMDP(init, terminals, t, rewards, gamma=.9)

print(our_mdp)