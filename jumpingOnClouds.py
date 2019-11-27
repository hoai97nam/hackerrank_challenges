"""
Emma is playing a new mobile game that starts with consecutively numbered clouds.
 Some of the clouds are thunderheads and others are cumulus. 
 She can jump on any cumulus cloud having a number that is equal to 
 the number of the current cloud plus  1 or 2. She must avoid the thunderheads. 
 Determine the minimum number of jumps it will take Emma to jump from 
 her starting postion to the last cloud. It is always possible to win the game.

"""
def jumpingOnClouds(c):
    l = len(c)
    jump = []
    for i in range(l-1):
        if i > 0:
            if c[i-1]!=0 and c[i] ==0 and c[i+1] == 0:
                jump.append(1)
            elif c[i] ==0 and c[i+1]==1:
                jump.append(0.5)
            elif c[i] ==1 and c[i+1]==0:
                jump.append(0.5)
            elif c[i] ==1 and c[i+1]==1:
                pass
        else:
            if c[i] ==0 and c[i+1] == 0:
                    jump.append(1)
            elif c[i] ==0 and c[i+1]==1:
                jump.append(0.5)
            elif c[i] ==1 and c[i+1]==0:
                jump.append(0.5)
            elif c[i] ==1 and c[i+1]==1:
                pass       
    return cal(jump) 

def cal(n):
    s = 0
    for i in n:
        s = s + i
    return s
            

if __name__ == '__main__':
    print(jumpingOnClouds([0,0,1,0,0,1,0]))