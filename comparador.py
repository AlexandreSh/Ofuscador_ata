file1 = "nomes_gen.txt"
file2 = "assinantes_gen.txt"

# Carrega os dois arquivos
with open(file1, 'r') as f1:
    names_file1 = set(line.strip() for line in f1)

with open(file2, 'r') as f2:
    names_file2 = set(line.strip() for line in f2)

# nomes no primeiro arquivo que não estão no segundo
names_in_file1_not_in_file2 = names_file1 - names_file2

# nomes no segundo arquivo que não estão no primeiro
names_in_file2_not_in_file1 = names_file2 - names_file1

# Imprime
print("Nomes em '{}', que não estão presentes em '{}':".format(file1, file2))
for name in names_in_file1_not_in_file2:
    print(name)

print("\nNomes em '{}', que não estão presentes em '{}':".format(file2, file1))
for name in names_in_file2_not_in_file1:
    print(name)
