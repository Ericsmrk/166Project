#here we will define the worlds that we will iterate through with the algorithms
# List[((int,int) (state), String action (R/D), int item #, Float Reward, Float Cost), ...]

#example of a world. not complete
world1 = [
    ((1,1), "R", 0, 0, 0, 0),   #state 1
    ((1,1), "D", 0, 0, 0, 0),   #state 1
    ((1,2), "R", 0, 0, 0, 0),   #state 2
    ((1,2), "D", 0, 0, 0, 0),   #state 2
    ((2,1), "R", 0, 0, 0, 0),   #state 3
    ((2,1), "D", 0, 0, 0, 0),   #state 3
]