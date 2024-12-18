"""
Rosalind Code: DNA
By: Shogan 
"""

def main():
    # Input
    with open("rosalind_dna.txt", 'r') as file:
        sample = file.read().strip()

    # main logic
    if sample.isalpha():
        A = sample.upper().count('A')
        C = sample.upper().count('C')
        G = sample.upper().count('G')
        T = sample.upper().count('T')
    else:
        print("INVALID INPUT FORMAT")

    # output
    print(A, C, G, T)


if __name__ == '__main__':
    main()