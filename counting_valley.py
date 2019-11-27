"""
Gary is an avid hiker. He tracks his hikes meticulously,
 paying close attention to small details like topography. 
During his last hike he took exactly  steps. For every step he took,
 he noted if it was an uphill, U, or a downhill, D step. 
 Gary's hikes start and end at sea level and each step up or down 
 represents a  unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, 
starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, 
starting with a step down from sea level and ending with a step up to sea level.

Given Gary's sequence of up and down steps during his last hike, 
find and print the number of valleys he walked through.
"""
import math

def countingValleys(n, s):
    altitude = 0
    hill = []
    for i in range(n-1):
        if s[i]=='D':
            altitude -=1
        elif s[i]=='U':
            altitude +=1
        if altitude < 0:
            hill.append(-1)
        elif altitude > 0:
            hill.append(1)
        else:
            hill.append(0)
    # checking(hill) 
    return checking(hill)
    # print(hill)

def checking(s):
    state = 0
    for i in range(len(s)-1):
        if s[i] != s[i+1] and s[i+1] == 0:
            state +=1
    print(state)


if __name__ == '__main__':
    countingValleys(8, ['D','D','U','U','D','D','U','D'])