from collections import Counter

def count_nucleotides(dna_sequence):
    sequence = dna_sequence.upper()
    counts = Counter(sequence)
    return {base: counts.get(base, 0) for base in ['A', 'C', 'G', 'T']}

dna = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"
result = count_nucleotides(dna)

for base, count in result.items():
    print(f"{base}: {count}")
