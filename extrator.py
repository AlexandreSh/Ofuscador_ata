import subprocess
import unicodedata
import string

# Processa e fatia texto_ofuscado.txt em nomes_gen.txt e assinantes_gen.txt
def process_file():
    with open('texto_ofuscado.txt', 'r') as file:
        lines = file.readlines()

    nomes_lines = []
    assinantes_lines = []
    capturing_nomes = False
    capturing_assinantes = False

    
    # nomes estão nas linhas entre "BACHARÉIS" e "Campo Grande - MS"
    for line in lines:
        if capturing_nomes:
            if line.startswith("Campo Grande - MS"):
                break
            if line.startswith("BACHARÉIS"):
                continue
            # Aplica a limpeza antes de adicionar à lista
            nomes_lines.append(clean_line(line))
        elif line.startswith("BACHARÉIS"):
            capturing_nomes = True

    # assinaturas estão entre "ASSINANTES:"  e "QRCode Assinatura"
    for line in lines:
        stripped_line = line.strip()  # Remove espaços em branco 
        if capturing_assinantes:
            if line.startswith("QRCode Assinatura"):
                break
            assinantes_lines.append(clean_line(line))  # Aplica a limpeza antes de adicionar à lista
        elif line.startswith("ASSINANTES"):
            capturing_assinantes = True

    # Remove linhas vazias (caso ainda existam após a limpeza)
    nomes_lines = [line.strip() for line in nomes_lines if line.strip()]  
    assinantes_lines = [line.strip() for line in assinantes_lines if line.strip()]      

    # Alfabetiza as listas
    #nomes_lines.sort()
    #assinantes_lines.sort()

    # Salva as listas processadas
    with open('nomes_gen.txt', 'w') as nomes_file:
        for line in nomes_lines:
            nomes_file.write(line + '\n')

    with open('assinantes_gen.txt', 'w') as assinantes_file:
        for line in assinantes_lines:
            assinantes_file.write(line + '\n')

    print("'nomes_gen.txt' e 'assinantes_gen.txt' foram criados com sucesso.")

# Função de limpeza
def clean_line(line):
    nfkd = unicodedata.normalize('NFKD', line)
    cleaned = ''.join([c for c in nfkd if c.isalpha() or c in [' ', '\n']])
    return cleaned.title()


# Ofusca os nomes
subprocess.run(["python", "ofuscador.py"])
# Executa o script extrator.py
process_file()
# Chama o script comparador
subprocess.run(["python", "comparador.py"])
