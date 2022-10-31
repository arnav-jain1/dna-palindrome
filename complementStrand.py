

def complement():
    f = open("dna.txt", "r")
    strand = f.read()
    f.close()
    f = open("dna.txt", "a")
    compStrand = ''
    for char in strand:
        if char == 'a':
            compStrand += 't'
        elif char == 't':
            compStrand += 'a'
        elif char == 'g':
            compStrand += 'c'
        elif char == 'c':
            compStrand += 'g'
    f.write(compStrand)
    f.close()


def main():
    complement()


main()
