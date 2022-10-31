import time

def findPal(bplength, bplengthMax):
    f = open("dna.txt", 'r')
    f2 = open("dnaResults.txt", 'w')
    strand = f.read()
    loc = {}
    counter = 0
    f2.write("5' - 3' sequence: amount of palindromes: location \n")
    while bplength <= bplengthMax:
        for num in range(0, len(strand)):
            check = strand[num: num + bplength]
            if check == invComplement(check):
                if check in loc:
                    loc[check].append(num)
                else:
                    loc[check] = [num]
                counter += 1
        bplength += 2
    for keys, val in loc.items():
        f2.write(keys + ": " + str(len(val)) + ": " + str(val) + "\n")
    listOfSeq = list(loc.keys())
    longest = listOfSeq[-1]
    f.close()
    f2.close()
    returnVar = (loc, counter, longest)
    return returnVar


def invComplement(str):
    str = str[::-1]
    newStr = ''
    for char in str:
        if char == 'a':
            newStr += 't'
        elif char == 't':
            newStr += 'a'
        elif char == 'g':
            newStr += 'c'
        elif char == 'c':
            newStr += 'g'
    return newStr


def main():
    bplengthMin = int(input("What is the minimum length you want for a palindrome? \n"))
    bplengthMax = int(input("What is the maximum length you want for a palindrome? \n"))
    start = time.time()
    output = findPal(bplengthMin, bplengthMax)
    results = output[0]
    totalpal = output[1]
    longestSeq = output[2]
    end = time.time()
    total = end - start
    print(results)
    print(f"Unique palindromes: {len(results)}\nTotal palindromes: {totalpal}\nLongest palindrome: {longestSeq} ({len(longestSeq)})")
    print(total)

main()

