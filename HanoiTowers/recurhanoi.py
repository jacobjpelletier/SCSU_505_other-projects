# Import time module for sleep()
import time


# describing towers of Hanoi
print('''\nWHAT IS THE HOWERS OF HANOI GAME?:\n
      It is a puzzle where the object is to move all of the disks to the right
      most peg. You may only move one disk at a time and you must never allow
      a larger disk to rest on a smaller disk.\nINFO FROM:
      http://haubergs.com/hanoi.''')

# user enters how many disks
while True:
    disks = input('\nEnter, from 1-12, the number of disks you want use in the'
                  ' game.\n\nEnter selection here: ')
    try:
        disks = int(disks)
        if disks > 0:
            break
        else:
            print('\nInteger must be more than 0.')
    except:
        print('\nEnter a valid integer.')

A = 'pillar A'
B = 'pillar B'
C = 'pillar C'
step = 0


def hanoiRecursion(disks, A, C, B):
    global step
    if disks > 0:
        hanoiRecursion(disks-1, A, B, C)
        time.sleep(3)
        step += 1
        print('\nRound '+str(step)+'\nMove smallest disk between '+A+' to '+C)
        # A,C,B = B,C,A
        hanoiRecursion(disks-1, B, C, A)
    return('\nEnd')


print(hanoiRecursion(disks, A, C, B))
