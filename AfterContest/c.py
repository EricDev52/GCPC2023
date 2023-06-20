import sys

def inp(cf=int, vpl=1, s=" "):
    if vpl == 1: return cf(sys.stdin.readline().strip("\n"))
    else: return list(map(cf, sys.stdin.readline().strip("\n").split(s)))

planetsCount, trainsCount, holesCount = inp(int, 3)
wormHoles = inp(int, 2)
trains = []
for t in range(trainsCount):
    trains.append(inp(int, 2))

def getMinTrains(origin : int, target : int, history=None) -> int:
    if history is None: history = [origin]
    if origin == target:
        return len(history)-1
    possibilities = []
    for t in trains:
        if t[0] == origin and t[1] not in history: possibilities.append(t[1])
        elif t[1] == origin and t[0] not in history: possibilities.append(t[0])
    minTrains = float("inf")
    for p in possibilities:
        trainsCount = getMinTrains(p, target, history+[p])
        if trainsCount < minTrains: minTrains = trainsCount
    return minTrains

fastest = getMinTrains(1, planetsCount)
for inHole in wormHoles:
    toHoleCount = getMinTrains(1, inHole)
    countSum = 0
    holes = wormHoles.copy()
    holes.remove(inHole)
    for outHole in holes:
        countSum += toHoleCount + getMinTrains(outHole, planetsCount)
    countSum /= len(holes)
    if countSum < fastest: fastest = countSum

from fractions import Fraction
f = str(Fraction(fastest))
if "/" not in f: f += "/1"
print(f)