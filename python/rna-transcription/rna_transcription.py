def to_rna(dna_strand):
    dict = {'G': 'C', 'C': 'G', 'T': 'A', 'A': 'U'}
    rna = []
    for c in dna_strand:
        rna.append(dict[c])
    return ''.join(rna)
