#
# Phunktions - a phunkadelic encapsulation of logic
# author: ronwhite562@gmail.com
# v1.0, 20240526
#
# orders a random list of input numbers without using sort() method.
# takes input and append() or insert() each number into an output list, 
# realtive to the range of current output numbers, and in constant time O(1)!
#
# usage: output = placeNextNumber(input)
# prints [3, 4, 5, 7, 13, 18, 20, 32, 72]
#
# - see NumPy (https://numpy.org)
import numpy as np

input = [20,4,18,32,7,13,3,72,5]
output =[]

class Ranger():
    lmh = [0,0,0]

    def computeLMH(self,lo,hi,out) -> list:
        # NOTE: out' list length is 0 at start with no defined size or boundary.
        # each of input' vals increments outs list, however, 0 thru 2 `middle` value
        # (or central tendency) can be negatives, so those iterations are simple averages.
        outCnt = len(out)
        ave = (lo - hi) / 2 if outCnt < 3 else round(sum(out)/len(out))
        av = round(ave * -1) if ave < 0 else ave
        ct = hi - av if ave < 0 else ave

        self.lmh[0] = 1 if lo == 0 else lo
        self.lmh[1] = ct
        self.lmh[2] = hi

        # print("computeLMH returns lms",self.lmh)
        return self.lmh


def findNearestNum(out,snum):
    # takes list and returns closest value search number. 
    # value can be higher or lower than search.
    array = np.asarray(out)
    idx = (np.abs(array - snum)).argmin()
    return array[idx]


# same as sort(), ie order from disordered.
# :Return: List[] in asending order, ex. [3,4,5...,72]
#
def placeNextNumber(input) -> list:
    i,lo,hi = 0,0,0
    out = []

    ranger = Ranger()
    ranger.lmh = ranger.computeLMH(1,10,out)

    for nn in input:
        # print("START: ",i)

        if nn > ranger.lmh[2]:
            out.append(nn) # new upper boundary
            lo = ranger.lmh[0]
            hi = nn

        elif nn > ranger.lmh[1]:
            e = findNearestNum(out,nn)
            x = 1 if len(out) <= 1 else out.index(e) + 1 if e < nn else out.index(e)
            out.insert(x,nn) # in upper range
            lo = out[0]
            hi = out[-1]

        elif nn > ranger.lmh[0] and nn < ranger.lmh[1]:
            e = findNearestNum(out,nn)
            x = 0 if len(out) <= 1 else out.index(e) + 1 if e < nn else out.index(e)
            out.insert(x,nn) # in lower range
            lo = ranger.lmh[0]
            hi = ranger.lmh[2]
        
        else:
            pn = out[0]
            x = 0 if nn < pn else out.index(ranger.lmh[0])
            out.insert(x,nn) # a new low
            lo = nn if nn < pn else ranger.lmh[0]
            hi = ranger.lmh[2]

        # print(out)
        # print("DONE: ",i)
        i += 1

        ranger.lhm = ranger.computeLMH(lo,hi,out)

    return out


output = placeNextNumber(input)
print("choas or order? ",output) # order, boo...
        