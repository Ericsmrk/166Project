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
    print('State     Money Saved')
    print_table(shop_world, "", '      ')

    print('\n', "State   Money Saved")
    print(" (0,10)", "  ", rounder(Vsw[(0, 10)], 2), '\n')
    print(" (0,9)","  ", rounder(Vsw[(0, 9)], 2), '\n')
    print(" (0,8)", "  ", rounder(Vsw[(0, 8)], 2), '\n')
    print(" (0,7)", "  ", rounder(Vsw[(0, 7)], 2), '\n')
    print(" (0,6)", "  ", rounder(Vsw[(0, 6)], 2), '\n')
    print(" (0,5)", "  ", rounder(Vsw[(0, 5)], 2), '\n')
    print(" (0,4)", "  ", rounder(Vsw[(0, 4)], 2), '\n')
    print(" (0,3)", "  ", rounder(Vsw[(0, 3)], 2), '\n')
    print(" (0,2)", "  ", rounder(Vsw[(0, 2)], 2), '\n')
    print(" (0,1)", "  ", rounder(Vsw[(0, 1)], 2), '\n')
    print(" (0,0)", "  ", rounder(Vsw[(0, 0)], 2), '\n')

    print("Best Policy Found")
    BPsw = best_policy(shopping_world, value_iteration(shopping_world, .01))
    print_table(shopping_world.to_arrows(BPsw), "", '  to COSTCO') #showing the "way"


def Experiment3(midterm_world) :
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
    q_agent = QLearningAgent(midterm_world, Ne=5, Rplus=50, alpha=lambda n: 60. / (59 + n))

#2  (0,2) (1,2)
#1  (0,1) (1,1)
#0  (0,0) (1,0) x

    for i in range(100):
        run_single_trial(q_agent, midterm_world)
        print("---iteration ", i, "---")

        print("(0,0)")
        qvalN00 = q_agent.Q[((0, 0), (0, 1))] #described above what is happening here
        qvalE00 = q_agent.Q[((0, 0), (1, 0))] #described above what is happening here
        print("N: ", qvalN00)
        print("E: ", qvalE00,'\n')

        print("(1,0)")
        qvalN10 = q_agent.Q[((1, 0), (1, 1))] #described above what is happening here
        print("N: ", qvalN10, '\n')

        print("(0,1)")
        qvalN01 = q_agent.Q[((0, 1), (0, 2))] #described above what is happening here
        qvalE01 = q_agent.Q[((0, 1), (1, 1))] #described above what is happening here
        print("N: ", qvalN01)
        print("E: ", qvalE01,'\n')

        print("(1,1)")
        qvalN11 = q_agent.Q[((1, 1), (1, 2))] #described above what is happening here
        print("N: ", qvalN11, '\n')

        print("(0,2)")
        qvalN02 = q_agent.Q[((0, 2), (0, 3))] #described above what is happening here
        qvalE02 = q_agent.Q[((0, 2), (1, 2))] #described above what is happening here
        print("N: ", qvalN02)
        print("E: ", qvalE02,'\n')

        print("(1,2)")
        qvalN12 = q_agent.Q[((1, 2), (1, 3))] #described above what is happening here
        print("N: ", qvalN12, '\n')

    print('\n\n\n\n')


def Experiment4(shopping_world) :
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
    q_agent = QLearningAgent(shopping_world, Ne=5, Rplus=50, alpha=lambda n: 60. / (59 + n))

    for i in range(100):
        run_single_trial(q_agent, shopping_world)
        print("---iteration ", i, "---")

        print("(0,0)")
        qvalN00 = q_agent.Q[((0, 0), (0, 1))] #described above what is happening here
        qvalE00 = q_agent.Q[((0, 0), (1, 0))] #described above what is happening here
        print("N: ", qvalN00)
        print("E: ", qvalE00,'\n')

        print("(1,0)")
        qvalN10 = q_agent.Q[((1, 0), (1, 1))] #described above what is happening here
        print("N: ", qvalN10, '\n')

        print("(0,1)")
        qvalN01 = q_agent.Q[((0, 1), (0, 2))] #described above what is happening here
        qvalE01 = q_agent.Q[((0, 1), (1, 1))] #described above what is happening here
        print("N: ", qvalN01)
        print("E: ", qvalE01,'\n')

        print("(1,1)")
        qvalN11 = q_agent.Q[((1, 1), (1, 2))] #described above what is happening here
        print("N: ", qvalN11, '\n')

        print("(0,2)")
        qvalN02 = q_agent.Q[((0, 2), (0, 3))] #described above what is happening here
        qvalE02 = q_agent.Q[((0, 2), (1, 2))] #described above what is happening here
        print("N: ", qvalN02)
        print("E: ", qvalE02,'\n')

        print("(1,2)")
        qvalN12 = q_agent.Q[((1, 2), (1, 3))] #described above what is happening here
        print("N: ", qvalN12, '\n')

        print("(0,3)")
        qvalN03 = q_agent.Q[((0, 3), (0, 4))] #described above what is happening here
        qvalE03 = q_agent.Q[((0, 3), (1, 3))] #described above what is happening here
        print("N: ", qvalN03)
        print("E: ", qvalE03,'\n')

        print("(1,3)")
        qvalN13 = q_agent.Q[((1, 3), (1, 4))] #described above what is happening here
        print("N: ", qvalN13, '\n')

        print("(0,4)")
        qvalN04 = q_agent.Q[((0, 4), (0, 5))] #described above what is happening here
        qvalE04 = q_agent.Q[((0, 4), (1, 4))] #described above what is happening here
        print("N: ", qvalN04)
        print("E: ", qvalE04,'\n')

        print("(1,4)")
        qvalN14 = q_agent.Q[((1, 4), (1, 5))] #described above what is happening here
        print("N: ", qvalN14, '\n')

        print("(0,5)")
        qvalN05 = q_agent.Q[((0, 5), (0, 6))] #described above what is happening here
        qvalE05 = q_agent.Q[((0, 5), (1, 5))] #described above what is happening here
        print("N: ", qvalN05)
        print("E: ", qvalE05,'\n')

        print("(1,5)")
        qvalN15 = q_agent.Q[((1, 5), (1, 6))] #described above what is happening here
        print("N: ", qvalN15, '\n')

        print("(0,6)")
        qvalN06 = q_agent.Q[((0, 6), (0, 7))] #described above what is happening here
        qvalE06 = q_agent.Q[((0, 6), (1, 6))] #described above what is happening here
        print("N: ", qvalN06)
        print("E: ", qvalE06,'\n')

        print("(1,6)")
        qvalN16 = q_agent.Q[((1, 6), (1, 7))] #described above what is happening here
        print("N: ", qvalN16, '\n')

        print("(0,7)")
        qvalN07 = q_agent.Q[((0, 7), (0, 8))] #described above what is happening here
        qvalE07 = q_agent.Q[((0, 7), (1, 7))] #described above what is happening here
        print("N: ", qvalN07)
        print("E: ", qvalE07,'\n')

        print("(1,7)")
        qvalN17 = q_agent.Q[((1, 7), (1, 8))] #described above what is happening here
        print("N: ", qvalN17, '\n')

        print("(0,8)")
        qvalN08 = q_agent.Q[((0, 8), (0, 9))] #described above what is happening here
        qvalE08 = q_agent.Q[((0, 8), (1, 8))] #described above what is happening here
        print("N: ", qvalN08)
        print("E: ", qvalE08,'\n')

        print("(1,8)")
        qvalN18 = q_agent.Q[((1, 8), (1, 9))] #described above what is happening here
        print("N: ", qvalN18, '\n')

        print("(0,9)")
        qvalN09 = q_agent.Q[((0, 9), (0, 10))] #described above what is happening here
        qvalE09 = q_agent.Q[((0, 9), (1, 9))] #described above what is happening here
        print("N: ", qvalN09)
        print("E: ", qvalE09,'\n')

        print("(1,9)")
        qvalN19 = q_agent.Q[((1, 9), (1, 10))] #described above what is happening here
        print("N: ", qvalN19, '\n')

    print('\n\n\n\n')


#10 [(0,10) (1,10)]
#9  [(0,9) (1,9)]
#8  [(0,8) (1,8)]
#7  [(0,7) (1,7)]
#6  [(0,6) (1,6)]
#5  [(0,5) (1,5)]
#4  [(0,4) (1,4)]
#3  [(0,3) (1,3)]
#2  [(0,2) (1,2)]
#1  [(0,1) (1,1)]
#0  [(0,0) (1,0)]