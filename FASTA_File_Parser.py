from Bio import SeqIO
from Bio.SeqUtils import gc_fraction

fasta_file = "sequences.fasta"

with open(fasta_file, "r") as handle:
    for record in SeqIO.parse(handle, "fasta"):
        length = len(record)
        gc = round(gc_fraction(record.seq) * 100, 2)
        print(f"ID: {record.id} | Length: {length} bp | GC: {gc}%")
