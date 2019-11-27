"""
John works at a clothing store. 
He has a large pile of socks that he must pair by color for sale. 
Given an array of integers representing the color of each sock, 
determine how many pairs of socks with matching colors there are.

Function Description:

Complete the sockMerchant function in the editor below. It must return an integer representing the number of matching pairs of socks that are available.

sockMerchant has the following parameter(s):

n: the number of socks in the pile
ar: the colors of each sock

"""
def sockMerchant(n, ar):
    count=[]
    while len(ar)!=0:
        val = ar.pop()
        if not compare(val, count):
            for i in ar:
                if val == i:
                    count.append(i)
                    ar.pop(ar.index(i))
                    break
                else:
                    if len(count)!=0:
                        count.pop()
                        break
                    else:
                        pass
        else:
            pass
    print(len(count))

def compare(n,a2):
    for i in a2:
        if n==i:
            return True
    return False

if __name__ == '__main__':
    sockMerchant(3,[1,1,2])