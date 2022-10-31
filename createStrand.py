import random
import time
f = open("dna.txt", "w")

def createBP():
    strand = ""
    a = 0
    t = 0
    c = 0
    g = 0
    for num in range(0, 1000000):
        randomNumber = random.randint(0, 3)
        if randomNumber == 0:
            strand += 'a'
            a += 1
        elif randomNumber == 1:
            strand += 't'
            t += 1
        elif randomNumber == 2:
            strand += 'g'
            g += 1
        elif randomNumber == 3:
            strand += 'c'
            c += 1
    info = [strand, a, t, g, c]
    return info


def main():
    start = time.time()
    info = createBP()
    strand = info[0]
    info.pop(0)
    f.write(strand)
    end = time.time()
    totalTime = end - start
    print("A: ", info[0], "\nT: ", info[1], "\nG: ", info[2], "\nC: ", info[3])
    f.close()
    print(f"Time to run code: {totalTime}")
main()
