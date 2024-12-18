"""
Rosalind Code: RNA
By: Shogan
"""

def main():
    # input
    with open("sample_input/rosalind_rna.txt", 'r') as file:
        t = file.read().strip()

    # main logic
    if t.isalpha():
        u = t.upper().replace('T', 'U')
        # output
        print("RNA is \n", u)
    else:
        print("INVALID INPUT FORMAT")

if __name__ == '__main__':
    main()






