# Ofuscação de dados pessoais e processamento de dados de um documento oficial

## Descrição

Este projeto processa a ata oficial de uma colação de grau da UFMS, ele ofusca os nomes dos graduados e dos assinantes da ata e compara os nomes de uma lista ofuscada com a outra, com o intuito de saber se algum dos discentes está a assinar e quais dos docentes já assinaram.
Ele lê o documento que deve ser chamado texto.txt e salvo na raiz do projeto (utilizei o documento 5330285 do processo 23104.001636/2024-91, não incluso no repositório), salva o arquivo ofuscado em texto_ofuscado.txt, salva os nomes ofuscados em nomes_gen.txt, os assinantes ofuscados em assinantes_gen.txt e salva o dicionário no arquivo dict.txt caso desofuscamento seja necessário e retorna no stdout quais nomes estão presentes numa das listas mas não na outra.

## Uso

Para iniciar o projeto, utilize o comando:

```bash
python3 extrator.py
```
