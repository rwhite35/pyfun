#
# Phunktions - a phunkadelic encapsulation of logic
# author: ronwhite562@gmail.com
# v1.0, 20240526
#
# orders a random list of numbers without using sort() method.
# takes input values and append() or insert() each into a list of ascending 
# numbers - relative to the current output - and in constant time O(1)!
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
        # NOTE: outputs length is 0 at start with no defined size or boundary.
        # meaning, the `middle`(or central tendency) value can be negative 
        # for 0...2 loops, those iterations are contrived simple averages.
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
    # takes list and returns closest value to search number. 
    # return value will be higher or lower than search term.
    array = np.asarray(out)
    idx = (np.abs(array - snum)).argmin()
    return array[idx]


# orders disorderly lists of numbers, similar to sort()
# :return: List[] in ascending order [3,4,...,72]
#
def placeNextNumber(input) -> list:
    i,lo,hi = 0,0,0
    out = []

    # seed range to start with an arbitrary lo, hi
    ranger = Ranger()
    ranger.lmh = ranger.computeLMH(1,10,out)

    for nn in input:
        # print("placing input val ",nn)

        if nn > ranger.lmh[2]:
            out.append(nn) # new upper boundary
            lo = ranger.lmh[0]
            hi = nn

        elif nn > ranger.lmh[1]:
            e = findNearestNum(out,nn)
            x = 1 if len(out) <= 1 else out.index(e) + 1 if e < nn else out.index(e)
            out.insert(x,nn) # inserted in upper range
            lo = out[0]
            hi = out[-1]

        elif nn > ranger.lmh[0] and nn < ranger.lmh[1]:
            e = findNearestNum(out,nn)
            x = 0 if len(out) <= 1 else out.index(e) + 1 if e < nn else out.index(e)
            out.insert(x,nn) # inserted in lower range
            lo = ranger.lmh[0]
            hi = ranger.lmh[2]
        
        else:
            pn = out[0]
            x = 0 if nn < pn else out.index(ranger.lmh[0])
            out.insert(x,nn) # a new lower low
            lo = nn if nn < pn else ranger.lmh[0]
            hi = ranger.lmh[2]

        # print("placed! ",i)
        # print(out)
        i += 1
        ranger.lhm = ranger.computeLMH(lo,hi,out)

    return out


output = placeNextNumber(input)
print("chaos or order? ",output) # order, boo...
        