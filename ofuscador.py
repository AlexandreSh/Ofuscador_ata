import hashlib
import unicodedata
import json

# Dicionário de palavras fictícias para mapeamento
dict_fict = ["processador", "microcontrolador", "transistor", "circuito", "diodo", "resistor", "capacitor", "indutor", "integrado", "bateria", 
             "sofware", "hardware", "eletrônico", "sinal", "voltaje", "corrente", "tensão", "impedância", "algoritmo", "programação", "linguagem", 
             "compilador", "dispositivo", "memória", "dados", "bit", "byte", "módulo", "periférico", "interface", "protótipo", "sensor", "atuador", 
             "controle", "arquitetura", "processamento", "sistemas", "redes", "comunicação", "informação", "transmissão", "modulação", "amplitude", 
             "frequência", "amplificador", "transmissor", "receptor", "microfone", "alto-falante", "led", "display", "digital", "analógico", "máquina", 
             "computador", "controle", "frequencímetro", "osciloscópio", "simulador", "dispositivo", "controlador", "unidade", "porta", "multiplexador", 
             "decodificador", "codificador", "sequenciador", "bus", "fio", "cabo", "condutor", "isolar", "solução", "verificação", "diagnóstico", 
             "interface", "programação", "filtro", "modem", "antena", "circuito", "manipulador", "polarização", "tensão", "sincronismo", "resposta", 
             "processo", "sintetizador", "multiplexação", "emissor", "rede", "adaptador", "controlador", "barramento", "nó", "hub", "switch", "roteador", 
             "gateway", "processador", "porta", "conector", "suporte", "configuração", "montagem", "distribuidor", "lan", "wan", "firewall", "rede", 
             "optical", "termômetro", "distância", "vibração", "lógica", "gate", "código", "binário", "testador", "frequência", "interferência", 
             "rejeição", "erro", "codificação", "controle", "acelerador", "pico", "banco", "rampa", "interruptor", "timer", "espectro", "nucleação", 
             "indutância", "reestruturação", "arquitetura", "interatividade", "compartilhamento", "código", "geração", "resposta", "validação", "energia", 
             "escala", "atenuação", "trabalho", "compressão", "função", "manipulação", "quantização", "desempenho", "entrada", "simulação", "feedback", 
             "mapeamento", "fluxo", "sincronização", "conjunto", "reconfiguração", "decodificação", "servidor", "processo", "transmissão", "recepção", 
             "comutador", "carregador", "gerador", "qualidade", "sistema", "escudo", "imunização", "impulso", "amortecimento", "microondas", "polarizador", 
             "comutação", "atenuador", "correção", "medição", "protocolo", "matriz", "projeção", "relé", "subconjunto"]

# Dicionário para armazenar palavras ofuscadas
obf_dict = {}

def clean_line(line):
    """Limpa a linha removendo caracteres não alfabéticos e convertendo para Title Case."""
    nfkd = unicodedata.normalize('NFKD', line)
    limpo = ''.join([c for c in nfkd if c.isalpha() or c in [' ', '\n']])
    return limpo.title()

def obfuscate_word(word, word_list):
    """Ofusca uma palavra hasheando e mapeando para uma palavra fictícia."""
    # Retorna a mesma saída para a mesma entrada
    if word in obf_dict:
        return obf_dict[word]
    
    # Hasheia a palavra para criar um número único
    word_hash = int(hashlib.sha256(word.encode('utf-8')).hexdigest(), 16)
    
    # Mapeia a palavra para uma palavra fictícia no dicionário
    index = word_hash % len(word_list)
    obfuscated_word = word_list[index]
    
    # Armazena a palavra ofuscada no dicionário para reutilização
    obf_dict[word] = obfuscated_word
    
    return obfuscated_word

def obfuscate_line(line, word_list, is_in_range):
    """Ofusca palavras linha a linha se estiverem nos intervalos definidos, além de ofuscar a primeira e última palavra da linha."""
    if is_in_range:
        # Limpa a linha antes de ofuscar
        line = clean_line(line)
        words = line.split()
        obfuscated_words = []
        
        for i, word in enumerate(words):
            # Ofusca a primeira ou última palavra independentemente do tamanho e palavras com mais de 3 caracteres
            if i == 0 or i == len(words) - 1 or len(word) > 3:
                obfuscated_words.append(obfuscate_word(word, word_list))
            else:
                obfuscated_words.append(word)
        
        return ' '.join(obfuscated_words)
    
    # Não modifica linhas fora dos intervalos
    return line

def obfuscate_file(file_path, line_ranges, word_list):
    """Apenas ofusca palavras nos intervalos definidos do arquivo."""
    with open(file_path, 'r') as file:
        lines = file.readlines()

    obfuscated_lines = []

    # Processa cada linha e ofusca palavras apenas dentro dos intervalos especificados
    for i, line in enumerate(lines):
        is_in_range = False
        for start, end in line_ranges:
            if start-1 <= i <= end-1:  # Ajusta os índices para a indexação de zero
                is_in_range = True
                break
        
        obfuscated_line = obfuscate_line(line, word_list, is_in_range)
        obfuscated_lines.append(obfuscated_line)
    
    return obfuscated_lines

def save_obfuscated_file(output_path, lines):
    """Salva as linhas processadas em um novo arquivo."""
    with open(output_path, 'w') as file:
        # Garante as quebras de linha
        for line in lines:
            file.write(line + "\n")

def save_dict(output_path, obf_dict):
    """Salva o dicionário de palavras obfuscadas em um arquivo."""
    with open(output_path, 'w') as file:
        # Escreve o dicionário em formato JSON para fácil leitura e uso
        json.dump(obf_dict, file, ensure_ascii=False, indent=4)

# Intervalos a serem ofuscados (inclusivo)
line_ranges = [
    (14, 40),
    (46, 86),
    (92, 164),
    (170, 182),
    (196, 372)
]

# Arquivo de entrada
input_file_path = 'texto.txt'

# Roda o ofuscador
obfuscated_lines = obfuscate_file(input_file_path, line_ranges, dict_fict)

# Salva o conteúdo ofuscado em um novo arquivo
output_file_path = 'texto_ofuscado.txt'
save_obfuscated_file(output_file_path, obfuscated_lines)

# Salva o dicionário de mapeamento em dict.txt
dict_file_path = 'dict.txt'
save_dict(dict_file_path, obf_dict)

print(f"Arquivo ofuscado salvo em {output_file_path}")
print(f"Dicionário de palavras obfuscadas salvo em {dict_file_path}")
