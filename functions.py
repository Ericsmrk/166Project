from mdp import *
from utils import *
from reinforcement_learning import *


def Experiment1(mid_world, midterm_world) :
    print("Original Midterm World", '\n')
    print_table(mid_world, "")
    print('\n')

    value_iteration2(midterm_world, .01)
    print('\n')

def Experiment2 (shop_world, shopping_world):
    Vsw = value_iteration(shopping_world, .01)
    # print('State     Money Saved')
    print(' \n Shopping World \n Rewards of each state at the beginning.')
    print_table(shop_world, "", '      ')

    print('\n', "State   Money Saved")
    print(" (0,10)", " ", rounder(Vsw[(0, 10)], 2), "  Hit all 10 stores, NO COSTCO\n")
    print(" (0,9)","  ", rounder(Vsw[(0, 9)], 2), "  Went to 9 stores then COSTCO\n")
    print(" (0,8)", "  ", rounder(Vsw[(0, 8)], 2), "  Went to 8 stores then COSTCO\n")
    print(" (0,7)", "  ", rounder(Vsw[(0, 7)], 2), "  Went to 7 stores then COSTCO\n")
    print(" (0,6)", "  ", rounder(Vsw[(0, 6)], 2), "  Went to 6 stores then COSTCO\n")
    print(" (0,5)", "  ", rounder(Vsw[(0, 5)], 2), "  Went to 5 stores then COSTCO\n")
    print(" (0,4)", "  ", rounder(Vsw[(0, 4)], 2), "  Went to 4 stores then COSTCO\n")
    print(" (0,3)", "  ", rounder(Vsw[(0, 3)], 2), "  Went to 3 stores then COSTCO\n")
    print(" (0,2)", "  ", rounder(Vsw[(0, 2)], 2), "  Went to 2 stores then COSTCO\n")
    print(" (0,1)", "  ", rounder(Vsw[(0, 1)], 2), "  Went to 1 store then COSTCO\n")
    print(" (0,0)", "  ", rounder(Vsw[(0, 0)], 2), "  Went to directly to COSTCO\n")

    print("Best Policy Found")
    BPsw_1 = best_policy(shopping_world, Vsw)
    print_table(shopping_world.to_arrows(BPsw_1), "", '  to COSTCO') #showing the "way"

def Experiment3 (shop_world2, shopping_world2):
    Vsw = value_iteration(shopping_world2, .01)
    # print('State     Money Saved')
    print(' \n Shopping World \n Rewards of each state at the beginning.')
    print_table(shop_world2, "", '      ')

    print('\n', "State   Money Saved")
    print(" (0,10)", " ", rounder(Vsw[(0, 10)], 2), "  Hit all 10 stores, NO COSTCO\n")
    print(" (0,9)","  ", rounder(Vsw[(0, 9)], 2), "  Went to 9 stores then COSTCO\n")
    print(" (0,8)", "  ", rounder(Vsw[(0, 8)], 2), "  Went to 8 stores then COSTCO\n")
    print(" (0,7)", "  ", rounder(Vsw[(0, 7)], 2), "  Went to 7 stores then COSTCO\n")
    print(" (0,6)", "  ", rounder(Vsw[(0, 6)], 2), "  Went to 6 stores then COSTCO\n")
    print(" (0,5)", "  ", rounder(Vsw[(0, 5)], 2), "  Went to 5 stores then COSTCO\n")
    print(" (0,4)", "  ", rounder(Vsw[(0, 4)], 2), "  Went to 4 stores then COSTCO\n")
    print(" (0,3)", "  ", rounder(Vsw[(0, 3)], 2), "  Went to 3 stores then COSTCO\n")
    print(" (0,2)", "  ", rounder(Vsw[(0, 2)], 2), "  Went to 2 stores then COSTCO\n")
    print(" (0,1)", "  ", rounder(Vsw[(0, 1)], 2), "  Went to 1 store then COSTCO\n")
    print(" (0,0)", "  ", rounder(Vsw[(0, 0)], 2), "  Went to directly to COSTCO\n")

    print("Best Policy Found")
    BPsw_1 = best_policy(shopping_world2, Vsw)
    print_table(shopping_world2.to_arrows(BPsw_1), "", '  to COSTCO') #showing the "way"

def Experiment4 (Vshop_world, Vshopping_world1):
    Vsw = value_iteration(Vshopping_world1, .01)
    # print('State     Money Saved')
    print(' \n Shopping World \n Rewards of each state at the beginning.')
    print_table(Vshop_world, "", '      ')

    print('\n', "State   Money Saved")
    print(" (0,10)", " ", rounder(Vsw[(0, 10)], 2), "  Hit all 10 stores, NO COSTCO\n")
    print(" (0,9)","  ", rounder(Vsw[(0, 9)], 2), "  Went to 9 stores then COSTCO\n")
    print(" (0,8)", "  ", rounder(Vsw[(0, 8)], 2), "  Went to 8 stores then COSTCO\n")
    print(" (0,7)", "  ", rounder(Vsw[(0, 7)], 2), "  Went to 7 stores then COSTCO\n")
    print(" (0,6)", "  ", rounder(Vsw[(0, 6)], 2), "  Went to 6 stores then COSTCO\n")
    print(" (0,5)", "  ", rounder(Vsw[(0, 5)], 2), "  Went to 5 stores then COSTCO\n")
    print(" (0,4)", "  ", rounder(Vsw[(0, 4)], 2), "  Went to 4 stores then COSTCO\n")
    print(" (0,3)", "  ", rounder(Vsw[(0, 3)], 2), "  Went to 3 stores then COSTCO\n")
    print(" (0,2)", "  ", rounder(Vsw[(0, 2)], 2), "  Went to 2 stores then COSTCO\n")
    print(" (0,1)", "  ", rounder(Vsw[(0, 1)], 2), "  Went to 1 store then COSTCO\n")
    print(" (0,0)", "  ", rounder(Vsw[(0, 0)], 2), "  Went to directly to COSTCO\n")

    print("Best Policy Found")
    BPsw_1 = best_policy(Vshopping_world1, Vsw)
    print_table(Vshopping_world1.to_arrows(BPsw_1), "", '  to COSTCO') #showing the "way"

def Experiment5(midterm_world) :

    q_agent = QLearningAgent(midterm_world, Ne=5, Rplus=2, alpha = lambda n: 60. / (59 + n))
    #^^^ get agent with world
    #vvv directions
    n = (0, 1)
    s = (0,-1)
    w = (-1, 0)
    e = (1, 0)
    dir= {(0, 1): "North ", (0,-1): "South ", (-1, 0): "West ", (1, 0): "East "}
    states = [(0,0),(0,1),(1,0),(1,1),(0,2)] # list states here
    iterations = 200# 1000 # run q learn how many times
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
    #print(q_agent.Q,"\n")
    print("\n\n\n")
