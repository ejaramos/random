'''quick script to generate squares for superbowl 2021
'''

import random

def rowss(row_number, sqs):
  idx = row_number*10
  return sqs[idx:idx + 10]

def name_drop(input_number, names):
  return names[input_number%(len(names))]

squares = [x for x in range(0,100)]
random.shuffle(squares)

names = ['p1', 'p2', 'p3', 'p4', 'p5', 'p6']

sq2 = list()

for i in range(0, 10):
  current_row = rowss(i, squares)
  for j in current_row:
    # print(j)
    sq2.append(name_drop(j, names))

for i in range(0,10):
  print(rowss(i, sq2))

team1 = [x for x in range(0,10)]
random.shuffle(team1)
print('TEAM1')
print(team1)

team2 = [x for x in range(0,10)]
random.shuffle(team2)
print('TEAM2')
print(team2)





