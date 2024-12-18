"""
Rosalind Code: GC
By Shogan
"""

def gc_content(dna:str):
    """
    Finds the GC content
    """
    gc = dna.upper().count('C') + dna.upper().count('G') 
    return gc/len(dna)*100 if dna else 0

    #gc_count = sum(1 for base in sequence if base in "GC")
    #return gc_count / len(sequence) * 100 if sequence else 0

def max_gc(filename):
    """
    find the sequence with hightest GC content
    """
    current_sequence = ''
    max_gc = 0
    max_header = None

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
        
            if line.startswith('>'):  # Header line
                if current_sequence:  # Process previous sequence
                    gc = gc_content(current_sequence)
                    if gc > max_gc:
                        max_gc = gc
                        max_header = header
                header = line
                current_sequence = ''
        
            else:  # Sequence line
                current_sequence += line
    
    # Process the last sequence
        if current_sequence:
            gc = gc_content(current_sequence)
            if gc > max_gc:
                max_gc = gc
                max_header = header
    
    return [max_header,max_gc]
            
        
def main():
    """
    Main Logic
    """
    result = max_gc("rosalind_gc.txt")
    print(result[0].removeprefix('>'),'\n',result[1])

if __name__=='__main__':
    main()
