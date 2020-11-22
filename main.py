from world import *
from CustomMDP import *
#from Transitions import *
from mdp import * #pythonMaster.

# for state in world1:
#     print(state)

#sample transition matrix
t = {
    'leisure': {
                    'facebook': {'leisure':0.9, 'class1':0.1},
                    'quit': {'leisure':0.1, 'class1':0.9},
                    'study': {},
                    'sleep': {},
                    'pub': {}
               },
    'class1': {
                    'study': {'class2':0.6, 'leisure':0.4},
                    'facebook': {'class2':0.4, 'leisure':0.6},
                    'quit': {},
                    'sleep': {},
                    'pub': {}
              },
    'class2': {
                    'study': {'class3':0.5, 'end':0.5},
                    'sleep': {'end':0.5, 'class3':0.5},
                    'facebook': {},
                    'quit': {},
                    'pub': {},
              },
    'class3': {
                    'study': {'end':0.6, 'class1':0.08, 'class2':0.16, 'class3':0.16},
                    'pub': {'end':0.4, 'class1':0.12, 'class2':0.24, 'class3':0.24},
                    'facebook': {},
                    'quit': {},
                    'sleep': {}
              },
    'end': {}
}

t1 = {}
#sample rewards
rewards = {
    'class1': 4,
    'class2': 6,
    'class3': 10,
    'leisure': -1,
    'end': 0
}

terminals = ['end']

init = 'class1'

#original#our_mdp = CustomMDP(init, terminals, t, rewards, gamma=.9)
our_mdp = CustomMDP(init, terminals, t, rewards, gamma=.9) #(t, rewards, terminals, init, gamma=.9)

print(our_mdp.reward.keys())
print(our_mdp.states)
print(our_mdp.transitions.keys())
print("mem:", our_mdp.check_consistency())

#value_iteration(our_mdp)
