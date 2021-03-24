import sys
from mdp import *
from utils import *
from reinforcement_learning import *
from world import *

from mdp import sequential_decision_environment
# for i in range(len(states)):
#     ds = q_agent.actions_in_state(states[i])
#     print(ds)
# print(q_agent.Q,"\n")
# print_table(q_agent.actions_in_state((0,0)))

q_agent = QLearningAgent(midterm_world, Ne=5, Rplus=2, alpha=lambda n: 60. / (59 + n))
#^^^ get agent with world
#vvv directions
n = (0, 1)
s = (0,-1)
w = (-1, 0)
e = (1, 0)
dir= {(0, 1): "North ", (0,-1): "South ", (-1, 0): "West ", (1, 0): "East "}
states = [(0,0),(0,1),(1,0),(1,1),(2,1)] # list states here
#print_table(states)
iterations = 200 # run q learn how many times
list = [x for x in range(iterations + 1) if x % 50 == 0] # get every item div/??? in list

for i in range(iterations + 1):
    run_single_trial(q_agent, midterm_world)
    for l in list: # only printing results every 50 iterations
        if l == i:
            print("\nExecuting trial ", l)

            #STATE(0,0)
            ds = q_agent.actions_in_state(states[0])
            print("In state", states[0], "can go: ")
            if ds == [None]:    #was throwing error
                print("None available.")
            else:
                for d in ds:
                    print(dir[d])
            print("Q-Values of:")#change list to next in states
            print("N: ", rounder(q_agent.Q[(states[0], n)], 4))
            print("S: ", rounder(q_agent.Q[(states[0], s)], 4))
            print("E: ", rounder(q_agent.Q[(states[0], e)], 4))
            print("W: ", rounder(q_agent.Q[(states[0], w)], 4))

            #STATE(0,1)
            ds = q_agent.actions_in_state(states[1])
            print("In state", states[1], "can go: ")
            if ds == [None]:    #was throwing error
                print("None available.")
            else:
                for d in ds:
                    print(dir[d])
            print("Q-Values of:")#change list to next in states
            print("N: ", rounder(q_agent.Q[(states[1], n)], 4))
            print("S: ", rounder(q_agent.Q[(states[1], s)], 4))
            print("E: ", rounder(q_agent.Q[(states[1], e)], 4))
            print("W: ", rounder(q_agent.Q[(states[1], w)], 4))

            #STATE(0,0)
            ds = q_agent.actions_in_state(states[0])
            print("In state", states[0], "can go: ")
            if ds == [None]:    #was throwing error
                print("None available.")
            else:
                for d in ds:
                    print(dir[d])
            print("Q-Values of:")#change list to next in states
            print("N: ", rounder(q_agent.Q[(states[0], n)], 4))
            print("S: ", rounder(q_agent.Q[(states[0], s)], 4))
            print("E: ", rounder(q_agent.Q[(states[0], e)], 4))
            print("W: ", rounder(q_agent.Q[(states[0], w)], 4))
            #STATE(0,0)
            ds = q_agent.actions_in_state(states[4])
            print("In state", states[4], "can go: ")
            if ds == [None]:    #was throwing error
                print("None available.")
            else:
                for d in ds:
                    print(dir[d])
            print("Q-Values of:")#change list to next in states
            print("N: ", rounder(q_agent.Q[(states[4], n)], 4))
            print("S: ", rounder(q_agent.Q[(states[4], s)], 4))
            print("E: ", rounder(q_agent.Q[(states[4], e)], 4))
            print("W: ", rounder(q_agent.Q[(states[4], w)], 4))

            #STATE(2,0)
            ds = q_agent.actions_in_state(states[4])
            print("In state", states[4], "can go: ")
            if ds == [None]:    #was throwing error
                print("None available.")
            else:
                for d in ds:
                    print(dir[d])
            print("Q-Values of:")#change list to next in states
            print("N: ", rounder(q_agent.Q[(states[4], n)], 4))
            print("S: ", rounder(q_agent.Q[(states[4], s)], 4))
            print("E: ", rounder(q_agent.Q[(states[4], e)], 4))
            print("W: ", rounder(q_agent.Q[(states[4], w)], 4))
print("\n\n\n")
