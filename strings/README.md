# Desafio 1: Strings

Após ler o coding style do kernel Linux, você descobre a mágica que é
ter linhas de código com no máximo 80 caracteres cada uma.

Assim, você decide que de hoje em diante seus e-mails enviados também
seguirão um padrão parecido e resolve desenvolver um plugin para te ajudar
com isso. Contudo, seu plugin aceitará no máximo 40 caracteres por linha.

Implemente uma função que receba:
1. um texto qualquer
2. um limite de comprimento

e seja capaz de gerar os outputs dos desafios abaixo.

## Exemplo input

`In the beginning God created the heavens and the earth. Now the earth was formless and empty, darkness was over the surface of the deep, and the Spirit of God was hovering over the waters.`

`And God said, "Let there be light," and there was light. God saw that the light was good, and he separated the light from the darkness. God called the light "day," and the darkness he called "night." And there was evening, and there was morning - the first day.`

O texto deve ser parametrizável e se quiser, pode utilizar um texto de input de sua preferência.

### Parte 1 (Básico) - limite 40 caracteres
Você deve seguir o exemplo de output [deste arquivo](https://github.com/idwall/desafios/blob/master/strings/output_parte1.txt), onde basta o texto possuir, no máximo, 40 caracteres por linha. As palavras não podem ser quebradas no meio.

### Parte 2 (Intermediário) - limite 40 caracteres
O exemplo de output está [neste arquivo](https://github.com/idwall/desafios/blob/master/strings/output-parte2.txt), onde além de o arquivo possuir, no máximo, 40 caracteres por linha, o texto deve estar **justificado**.

### Dicas
- Existe um template para projetos em Java ;)

### Extras

- Parametrização da quantidade de caracteres por linha.

# Solução Proposta
A solução proposta para esse desafio foi um programa em Python capaz de ler textos de um dado arquivo e salvar o resultado formatado num novo arquivo de saida.

A formatação se dara por um limite de caracteres por linha, seguido de uma justificação de texto.

## Arquivos auxiliaries
Foram adicionados tres arquivos de texto contendo exemplos de textos para serem formatados pela solucao:
* 42.txt
* loremipsum.txt
* sample.txt 

## Solução parametrizada
Utilizando o modulo argparse, a funcao principal do programa e capaz de receber ate tres parametros conforme a necessidade do usuario:
* input_file: o arquivo de entrada contendo o text a ser formatado (valor padrao: sample.txt)
* output_file: o arquivo de saida onde o texto de entrado sera salvo no novo formato (valor padrao: output_<input_file>.txt)
* line_len: o tamanho maximo de linha, em numero de caracteres (valor padrao: 40)

## Documentação
Todas as funcoes do codigo incluem docstring com explicacoes em ingles dos parametros esperados e do resultado retornado.

Comentarios extras foram adicionados perto dos respectivos codigos onde pareceu interessante detalhar a solucao proposta.

## Testes
Foi desenvolvida uma pequena cobertura de testes, em especial para a Parte 2 do desafio, para simular TDD e facilitar a validacao das funcoes mais complexas do programa (as de justificacao de texto).

Os testes sao basicos, mas foram criados antes da implementacao, facilitando a validacao da solucao.
