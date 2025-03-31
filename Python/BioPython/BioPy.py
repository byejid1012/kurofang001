from Bio.Seq import Seq

# Create a DNA sequence
dna_sequence = Seq("ATGCGTACGTTAGC")

# Transcribe DNA to RNA
rna_sequence = dna_sequence.transcribe()
print("RNA Sequence:", rna_sequence)

# Translate RNA to Protein
protein_sequence = rna_sequence.translate()
print("Protein Sequence:", protein_sequence)

# Reverse complement of DNA
reverse_complement = dna_sequence.reverse_complement()
print("Reverse Complement:", reverse_complement)

# Calculate GC content
gc_content = (dna_sequence.count("G") + dna_sequence.count("C")) / len(dna_sequence) * 100
print("GC Content (%):", gc_content)        

