def repetição(seq):
    rep_max = 1
    rep_atual = 1
    for i in range(1,len(seq)):
        if seq[i]==seq[i-1]:
            rep_atual +=1
        else:
            rep_atual = 1
        rep_max = max(rep_max, rep_atual)
    return rep_max


dna = input()
print(repetição(dna))

