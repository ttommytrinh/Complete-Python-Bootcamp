'''
Write some code that simulates flipping a single coin however many times the user decides. 
The code should record the outcomes and count the number of tails and heads.
'''

import random

class Coin():

    def __init__(self):
        self.heads = 0
        self.tails = 1
        self.flip_recorder_number = []
        self.flip_recorder_list = []
        
    def coin_flip_recorder(self,number):
        for x in range(number):
            self.flip_recorder_number.append(random.randint(0,1))
        for y in self.flip_recorder_number:
            if y == 0:
                self.flip_recorder_list.append("Heads")
            else:
                self.flip_recorder_list.append("Tails")
        return(self.flip_recorder_list)
    
    def tally(self):
        head_tally = 0
        tail_tally = 0
        for x in self.flip_recorder_number:
            if x == 0:
                head_tally += 1
            else:
                tail_tally += 1
        return(f"# of heads: {head_tally}. # of tails: {tail_tally}.")
