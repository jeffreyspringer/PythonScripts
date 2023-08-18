seq1 = input("What is the first set text? ") 
seq2 = input("What is the second set of text? ")

zip_seqs = zip(seq1, seq2)
#print(list(zip_seqs))

enum_seqs = enumerate(zip_seqs)
#print(list(enum_seqs))

counter = 0

for i, (a,b) in enum_seqs:
    if a!= b:
        print(f'Wrong index: {i}')
        counter += 1
        
print(f'Number wrong: {counter}')