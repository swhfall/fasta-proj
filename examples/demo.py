from fasta import Seq, FastaReader

seq = Seq("test", "ATCGTUAACG")
print(f"Длина: {len(seq)}")
print(f"Тип: {seq.get_alphabet()}")  

print("\n" + "="*50)

reader_one = FastaReader("examples/protein.faa")  
print("Чтение protein.faa:")
count = 0
for sequence in reader_one:
    print(sequence)
    count += 1
    if count >= 2:  
        break

print("\n" + "="*50)

reader_two = FastaReader("examples/GCA_000006945.2_ASM694v2_genomic.fna")  # Исправлен путь
print("Чтение GCA_000006945.2_ASM694v2_genomic.fna:")
count = 0
for sequence in reader_two:
    print(sequence)
    count += 1
    if count >= 2:  
        break
    
