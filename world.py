from mdp import *
import random
from datetime import datetime
#here we will define the worlds that we will iterate through with the algorithms
# List[((int,int) (state), String action (R/D), int item #, Float Reward, Float Cost), ...]

# ----------------------------------------------------------------------WORLD DESC.-------------------------------------------------------------------------------------------------
# GridMDP (Grid, terminals, initial, gama)
# grid[reward]
# 0 == 0.001
# east, north

midterm_world = GridMDP(
    [
    #    y
    #    0, 1
        [10, None],    #2  (0,2) (1,2)
        [0.01, -10],   #1  (0,1) (1,1)
        [0.01, 1]      #0  (0,0) (1,0) x
    ],
    terminals=
    [
        # x,y
        (0, 2),
        (1, 1),
        (1, 0)
    ]
)
mid_world = [[10, None], [0.01, -10],[0.01, 1]]

shop_world = [
    # 0,  1 WHEN THE VALUES IN (0, ..) IS HIGHEST, WE GO TO COSTCO
    # and that is how much money we save by going to costco
    [10, 0.001], #10 [(0,10) (1,10)]
    [9, 5],      #9  [(0,9) (1,9)]
    [8, 10],     #8  [(0,8) (1,8)]
    [7, 15],     #7  [(0,7) (1,7)]
    [6, 19],     #6  [(0,6) (1,6)]
    [5, 20],     #5  [(0,5) (1,5)]
    [4, 30],     #4  [(0,4) (1,4)]
    [3, 33],     #3  [(0,3) (1,3)]
    [2, 42],     #2  [(0,2) (1,2)]
    [1, 45],     #1  [(0,1) (1,1)]
    [0.001, 50]  #0  [(0,0) (1,0)]
]
shopping_world = GridMDP(
    [

        # 0,  1 WHEN THE VALUES IN (0, ..) IS HIGHEST, WE GO TO COSTCO
        # and that is how much money we save by going to costco
        [10, 0.001], #10 [(0,10) (1,10)]
        [9, 5],      #9  [(0,9) (1,9)]
        [8, 10],     #8  [(0,8) (1,8)]
        [7, 15],     #7  [(0,7) (1,7)]
        [6, 19],     #6  [(0,6) (1,6)]
        [5, 20],     #5  [(0,5) (1,5)]
        [4, 30],     #4  [(0,4) (1,4)]
        [3, 33],     #3  [(0,3) (1,3)]
        [2, 42],     #2  [(0,2) (1,2)]
        [1, 45],     #1  [(0,1) (1,1)]
        [0.001, 50]  #0  [(0,0) (1,0)]
    ],
    terminals=
    [
    #    x, y
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
        (1,10)
    ]
)
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------

shop_world2 = [
    # 0,  1 WHEN THE VALUES IN (0, ..) IS HIGHEST, WE GO TO COSTCO
    # and that is how much money we save by going to costco
    [10, 0.001], #10 [(0,10) (1,10)]
    [9, 5],      #9  [(0,9) (1,9)]
    [8, 10],     #8  [(0,8) (1,8)]
    [7, 15],     #7  [(0,7) (1,7)]
    [6, 19],     #6  [(0,6) (1,6)]
    [5, 50],     #5  [(0,5) (1,5)]
    [4, 30],     #4  [(0,4) (1,4)]
    [3, 33],     #3  [(0,3) (1,3)]
    [2, 42],     #2  [(0,2) (1,2)]
    [1, 45],     #1  [(0,1) (1,1)]
    [0.001, 40]  #0  [(0,0) (1,0)]
]
shopping_world2 = GridMDP(
    [

        # 0,  1 WHEN THE VALUES IN (0, ..) IS HIGHEST, WE GO TO COSTCO
        # and that is how much money we save by going to costco
        [10, 0.001], #10 [(0,10) (1,10)]
        [9, 5],      #9  [(0,9) (1,9)]
        [8, 10],     #8  [(0,8) (1,8)]
        [7, 15],     #7  [(0,7) (1,7)]
        [6, 19],     #6  [(0,6) (1,6)]
        [5, 50],     #5  [(0,5) (1,5)]
        [4, 30],     #4  [(0,4) (1,4)]
        [3, 33],     #3  [(0,3) (1,3)]
        [2, 42],     #2  [(0,2) (1,2)]
        [1, 45],     #1  [(0,1) (1,1)]
        [0.001, 40]  #0  [(0,0) (1,0)]
    ],
    terminals=
    [
    #    x, y
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
        (1,10)
    ]
)

#------------------------------------VINCE'S NEW MAGICAL WORLDS-----------------------------------------------------------------------



# I AM ATTEMPTING TO ADD SOME RANDOMNESS TO THE REWARD VALUES BY USING THE RANDOM LIBRARY TO GIVE US A
# REWARD AT RANDOM WITHIN A SPECIFIED RANGE. I THINK THIS WILL HELP US NOT GET THE SAME RESULT EVERY SINGLE TIME!

# MY HOPE IS THAT NOW THE AGENT WILL HAVE MORE OF A DECISION TO MAKE. THE RANDOM VALUE OF -5 IS THE SITUATION WHERE WE GO TO THE NEXT
# STORE, BUT DON'T FIND ANY ITEMS WE ARE LOOKING FOR AND HAVE ONLY WASTED TIME AND GAS GOING THERE.  THE MAX VALUES 30,28,26, ETC
# IS THE SITUATION WHERE WE FIND A GREAT DEAL ON A LOT OF ITEMS WE WERE LOOKING FOR!  WE WILL NEED TO OPTIMIZE THE NUMBERS A BIT
# TO FIND THE BEST COMBINATION OF REWARD RANGE OF GROCERY STORES TO COSTCO REWARD.  WE COULD ALSO ADD A RANGE TO COSTCO IF WE WANT
# TO, BUT I THINK THAT IS JUST ADDING ANOTHER DEGREE OF COMPLEXITY FOR US TO FIGURE OUT.
def genShoppingV1():
    random.seed(datetime.now())
    shop_worldV1 = [
    # 0,  1 WHEN THE VALUES IN (0, ..) IS HIGHEST, WE GO TO COSTCO
    # and that is how much money we save by going to costco
    [random.randint(-5,12), 0.001], #10 [(0,10) (1,10)]
    [random.randint(-5,14), 5],      #9  [(0,9) (1,9)]
    [random.randint(-5,16), 10],     #8  [(0,8) (1,8)]
    [random.randint(-5,18), 15],     #7  [(0,7) (1,7)]
    [random.randint(-5,20), 19],     #6  [(0,6) (1,6)]
    [random.randint(-5,22), 20],     #5  [(0,5) (1,5)]
    [random.randint(-5,24), 30],     #4  [(0,4) (1,4)]
    [random.randint(-5,26), 33],     #3  [(0,3) (1,3)]
    [random.randint(-5,28), 42],     #2  [(0,2) (1,2)]
    [random.randint(-5,30), 45],     #1  [(0,1) (1,1)]
    [0.001, 50]                      #0  [(0,0) (1,0)]
    ]
    return shop_worldV1

#I MADE IT SO THAT (0,10) IS ALSO AN EXIT STATE.  NO REASON TO GO TO COSTCO IF WE ALREADY GOT EVERYTHING WE NEED FROM OTHER STORES.
terminalsV2= [
  #  x, y
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
    (1,10),
    (0,10)
]

#FIRST VERSION OF MY RANDOM SHOPPING WORLD
Vshopping_world1 = GridMDP(genShoppingV1(), terminalsV2)
