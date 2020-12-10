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

q_agent = QLearningAgent(midterm_world, Ne=5, Rplus=2, alpha = lambda n: 60. / (59 + n))
#^^^ get agent with world
#vvv directions
n = (0, 1)
s = (0,-1)
w = (-1, 0)
e = (1, 0)
dir= {(0, 1): "North ", (0,-1): "South ", (-1, 0): "West ", (1, 0): "East "}
states = [(0,0),(0,1),(1,0),(1,1),(2,0)] # list states here
iterations = 200 # run q learn how many times
list = [x for x in range(iterations + 1) if x % 50 == 0] # get every item div/??? in list

for i in range(iterations + 1):
    run_single_trial(q_agent, midterm_world)
    for l in list:
        if l == i:
            count = 0
            for state in states:
                print("\nExecuting trial ", l)
                #STATE(0,0)
                ds = q_agent.actions_in_state(states[count])
                print("In state",state,"can go: ")
                if ds == [None]:
                    print("None available.")
                else:
                    for d in ds:
                        print(dir[d])
                print("Q-Values of:")#for some reason this won't run by using count
                print("N: ", rounder(q_agent.Q[(states[count], n)], 4))
                print("S: ", rounder(q_agent.Q[(states[count], s)], 4))
                print("E: ", rounder(q_agent.Q[(states[count], e)], 4))
                print("W: ", rounder(q_agent.Q[(states[count], w)], 4))
                count = count + 1
                #print(count)
print(q_agent.Q,"\n")
print("\n\n\n")
