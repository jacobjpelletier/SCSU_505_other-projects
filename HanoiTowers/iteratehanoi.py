#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  7 18:15:15 2018
@author: jacobpelletier
"""

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


# Initial inputs of program
diskdict = {}
step = 0

# creates initial disk dictionary based on user input of disks
for disk in range(1, disks+1):
    diskdict[('disk'+str(disk))] = disk

# 3 pillars, A is the starting pillar.
reversekeys = list(reversed(sorted(diskdict.keys())))
reversevalues = list(reversed(sorted(diskdict.values())))
pillarA = dict(zip(reversekeys, reversevalues))
pillarB = {}
pillarC = {}

# creates initial disk dictionary based on user input of disks
for disk in range(1, disks+1):
    diskdict[('disk'+str(disk))] = disk


def printround(step):
        return('\nRound '+str(step)+'.')


def aandb(pillarA, pillarB):
    if pillarB == {}:
            pillarB[list(pillarA.keys())[-1]] = list(pillarA.values())[-1]
            del pillarA[list(pillarA.keys())[-1]]
            return('\nMove '+str(list(pillarB.keys())[-1])+' from pillar A'
                   ' to pillar B.')
    elif pillarA == {}:
        pillarA[list(pillarB.keys())[-1]] = list(pillarB.values())[-1]
        del pillarB[list(pillarB.keys())[-1]]
        return('\nMove '+str(list(pillarA.keys())[-1])+' from pillar B to'
               ' pillar A.')
    else:
        if (list(pillarA.values())[-1] < list(pillarB.values())[-1]):
            pillarB[list(pillarA.keys())[-1]] = list(pillarA.values())[-1]
            del pillarA[list(pillarA.keys())[-1]]
            return('\nMove '+str(list(pillarB.keys())[-1])+' from pillar '
                   'A to pillar B.')
        else:
            pillarA[list(pillarB.keys())[-1]] = list(pillarB.values())[-1]
            del pillarB[list(pillarB.keys())[-1]]
            return('\nMove '+str(list(pillarA.keys())[-1])+' from pillar '
                   'B to pillar A.')


def aandc(pillarA, pillarC):
    if pillarC == {}:
        pillarC[list(pillarA.keys())[-1]] = list(pillarA.values())[-1]
        del pillarA[list(pillarA.keys())[-1]]
        return('\nMove '+str(list(pillarC.keys())[-1])+' from pillar A'
               ' to pillar C.')
    elif pillarA == {}:
        pillarA[list(pillarC.keys())[-1]] = list(pillarC.values())[-1]
        del pillarC[list(pillarC.keys())[-1]]
        return('\nMove '+str(list(pillarA.keys())[-1])+' from pillar C '
               'to pillar A.')
    else:
        if (list(pillarA.values())[-1] < list(pillarC.values())[-1]):
            pillarC[list(pillarA.keys())[-1]] = list(pillarA.values())[-1]
            del pillarA[list(pillarA.keys())[-1]]
            return('\nMove '+str(list(pillarC.keys())[-1])+' from pillar '
                   'A to pillar C.')
        else:
            pillarA[list(pillarC.keys())[-1]] = list(pillarC.values())[-1]
            del pillarC[list(pillarC.keys())[-1]]
            return('\nMove '+str(list(pillarA.keys())[-1])+' from pillar '
                   ' C to pillar A.')


def bandc(pillarB, pillarC):
    if pillarC == {}:
        pillarC[list(pillarB.keys())[-1]] = list(pillarB.values())[-1]
        del pillarB[list(pillarB.keys())[-1]]
        return('\nMove '+str(list(pillarC.keys())[-1])+' from pillar B to'
               ' pillar C.')
    elif pillarB == {}:
        pillarB[list(pillarC.keys())[-1]] = list(pillarC.values())[-1]
        del pillarC[list(pillarC.keys())[-1]]
        return('\nMove '+str(list(pillarB.keys())[-1])+' from pillar C to'
               ' pillar B.')
    else:
        if (list(pillarB.values())[-1] < list(pillarC.values())[-1]):
            pillarC[list(pillarB.keys())[-1]] = list(pillarB.values())[-1]
            del pillarB[list(pillarB.keys())[-1]]
            return('\nMove '+str(list(pillarC.keys())[-1])+' from pillar B'
                   ' to pillar C.')
        else:
            pillarB[list(pillarC.keys())[-1]] = list(pillarC.values())[-1]
            del pillarC[list(pillarC.keys())[-1]]
            return('\nMove '+str(list(pillarB.keys())[-1])+' from pillar C'
                   ' to pillar B.')


def lastforodd(pillarA, pillarB, pillarC):
    if pillarB == {} and len(pillarA) == 1:
        pillarC[list(pillarA.keys())[-1]] = list(pillarA.values())[-1]
        del pillarA[list(pillarA.keys())[-1]]
        return('\nMove '+str(list(pillarC.keys())[-1])+' from pillar A to '
               'pillar C.')


# if disks == 1
if disks == 1:
    step += 1
    print(printround(step), '\nMove disk1 from pillarA to pillarC')
    time.sleep(3)

else:

    while len(pillarC) < disks:

        # logic for when disks are even
        if disks % 2 == 0:
            step += 1
            print(printround(step), aandb(pillarA, pillarB))
            time.sleep(3)
            step += 1
            print(printround(step), aandc(pillarA, pillarC))
            time.sleep(3)
            step += 1
            print(printround(step), bandc(pillarB, pillarC))
            time.sleep(3)

        # logic for when disks are odd
        elif disks % 2 != 0:
            step += 1
            print(printround(step), aandc(pillarA, pillarC))
            time.sleep(3)
            step += 1
            print(printround(step), aandb(pillarA, pillarB))
            time.sleep(3)
            step += 1
            print(printround(step), bandc(pillarB, pillarC))
            time.sleep(3)
            # moving last disk when disks are odd, go to last pillar rather
            # than next empty pillar
            if (((2**disks)-1)-step) <= 1:
                step += 1
                print(printround(step), lastforodd(pillarA, pillarB, pillarC))
                time.sleep(3)
