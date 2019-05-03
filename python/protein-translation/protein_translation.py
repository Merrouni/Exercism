def proteins(strand):
    dict = {'AUG': 'Methionine', 'UUU': 'Phenylalanine', 'UUC': 'Phenylalanine'
            , 'UUA': 'Leucine', 'UUG': 'Leucine', 'UCU': 'Serine', 'UCC': 'Serine'
            , 'UCA': 'Serine', 'UCG': 'Serine', 'UAU': 'Tyrosine', 'UAC': 'Tyrosine'
            , 'UGU': 'Cysteine', 'UGC': 'Cysteine', 'UGG': 'Tryptophan', 'UAA': 'STOP'
            , 'UAG': 'STOP', 'UGA': 'STOP'}
    if (len(strand) % 3 != 0):
        raise Exception("the strand is not complete !!!")

    proteins = []
    codonsNb = int(len(strand) / 3)
    
    for i in range(0,codonsNb):
        key = strand[i*3:(i+1)*3]
        protein = dict[key]
        if protein == 'STOP':
            return proteins
        else:
            proteins.append(protein)
    return proteins
