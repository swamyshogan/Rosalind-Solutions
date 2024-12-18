"""
Rosalind Code: REVC
By Shogan
"""

def revc(dna:str):
    # Create the complementary strand
    rcdna = dna[::-1].upper().translate(str.maketrans('ATCG', 'TAGC'))
    
    return rcdna

def main():
    # input
    with open("sample_input/rosalind_revc.txt", 'r') as file:
        s = file.read().strip()

    # output
    print(revc(s))

if __name__=='__main__':
    main()
