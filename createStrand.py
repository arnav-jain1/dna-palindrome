import random
import time

def createBP(size):
    strand = ""
    a = 0
    t = 0
    c = 0
    g = 0
    for num in range(0, size):
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
    size = int(input("How big of a strand do you want to make?\n"))
    f = open("dna.txt", "w")
    start = time.time()
    info = createBP(size)
    strand = info[0]
    info.pop(0)
    f.write(strand)
    end = time.time()
    totalTime = end - start
    print("A: ", info[0], "\nT: ", info[1], "\nG: ", info[2], "\nC: ", info[3])
    f.close()
    print(f"Time to run code: {totalTime}")

main()
