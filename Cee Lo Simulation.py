
# cee lo simulation
import random
from tqdm import tqdm

dice = [1,2,3,4,5,6]

winner = []

for i in tqdm(range(10000000)):

    # get a valid roll
    while True:
        roll_1 = sorted(random.choices(dice,k=3))        
        if roll_1[0]!=roll_1[1]!=roll_1[2] and roll_1 not in [[1,2,3],[4,5,6]]: continue
        else: break

    # check for auto win
    if roll_1 in [[4,5,6],[1,1,6],[2,2,6],[3,3,6],[4,4,6],[5,5,6],[6,6,6]]:
        winner.append('bank')
        continue

    # check for auto loss
    if roll_1 in [[1,2,3],[1,1,1],[2,2,1],[3,3,1],[4,4,1],[5,5,1],[6,6,1]]:
        winner.append('player')
        continue
    
    if len(set(roll_1))==1:
        roll_1_point = roll_1[0]
    else:
        roll_1_point = [i for i in roll_1 if roll_1.count(i)==1][0]
    

    # get a valid player 2 roll
    while True:
        roll_2 = sorted(random.choices(dice,k=3))        
        if roll_2[0]!=roll_2[1]!=roll_2[2] and roll_2 not in [[1,2,3],[4,5,6]]: continue
        else: break

    # check for auto win
    if roll_2 in [[4,5,6],[1,1,6],[2,2,6],[3,3,6],[4,4,6],[5,5,6],[6,6,6]]:
        winner.append('player')
        continue

    # check for auto loss
    if roll_2 in [[1,2,3],[1,1,1],[2,2,1],[3,3,1],[4,4,1],[5,5,1],[6,6,1]]:
        winner.append('bank')
        continue

    # score the points
    if len(set(roll_2))==1:
        roll_2_point = roll_1[0]
    else:
        roll_2_point = [i for i in roll_2 if roll_2.count(i)==1][0]

    # get the winner
    if roll_2_point>roll_1_point:
        winner.append('player')
    else:
        winner.append('bank')


print(sum([1 for i in winner if i=='bank'])/len(winner))        












