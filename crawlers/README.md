# Desafio 2: Crawlers

Parte do trabalho na IDwall inclui desenvolver *crawlers/scrapers* para coletar dados de websites.
Como nós nos divertimos trabalhando, às vezes trabalhamos para nos divertir!

O Reddit é quase como um fórum com milhares de categorias diferentes. Com a sua conta, você pode navegar por assuntos técnicos, ver fotos de gatinhos, discutir questões de filosofia, aprender alguns life hacks e ficar por dentro das notícias do mundo todo!

Subreddits são como fóruns dentro do Reddit e as postagens são chamadas *threads*.

Para quem gosta de gatos, há o subreddit ["/r/cats"](https://www.reddit.com/r/cats) com threads contendo fotos de gatos fofinhos.
Para *threads* sobre o Brasil, vale a pena visitar ["/r/brazil"](https://www.reddit.com/r/brazil) ou ainda ["/r/worldnews"](https://www.reddit.com/r/worldnews/).
Um dos maiores subreddits é o "/r/AskReddit".

Cada *thread* possui uma pontuação que, simplificando, aumenta com "up votes" (tipo um like) e é reduzida com "down votes".

Sua missão é encontrar e listar as *threads* que estão bombando no Reddit naquele momento!
Consideramos como bombando *threads* com 5000 pontos ou mais.

## Entrada
- Lista com nomes de subreddits separados por ponto-e-vírgula (`;`). Ex: "askreddit;worldnews;cats"

### Parte 1
Gerar e imprimir uma lista contendo a pontuação, subreddit, título da thread, link para os comentários da thread e link da thread.
Essa parte pode ser um CLI simples, desde que a formatação da impressão fique legível.

### Parte 2
Construir um robô que nos envie essa lista via Telegram sempre que receber o comando `/NadaPraFazer [+ Lista de subrredits]` (ex.: `/NadaPraFazer programming;dogs;brazil`)

### Dicas
 - Use https://old.reddit.com/
 - Qualquer método para coletar os dados é válido. Caso não saiba por onde começar, procure por JSoup (Java), SeleniumHQ (Java), PhantomJS (Javascript) e Beautiful Soup (Python).


# Solução Proposta
A solução final proposta para esse desafio foi robo de Telegram escrito em Python capaz de responder determinados comandos.

Entre os comandos possiveis, um recebe como parametros as SubReddits alvo de onde dados serao coletados e enviados por mensagem.

## Solução em Partes
Na resolucao da primeira parte foi desenvolvido o modulo crawler que fornece funcoes para coletar dados das paginas web do Reddit.

Para validar a Parte 1 foi utilizado argparse para receber as SubReddits de entrada (separadas por ";") e imprimir na stdout uma tabela com as threads quentes do momento.

Com o modulo crawler pronto e validado, o robo (telegram_bot.py) foi desenvolvido utilizando a biblioteca telebot que facilita a comunicacao com a API dos bots do Telegram e, inclusive, providencia anotacoes para deixar o codigo mais simples e legivel.
Mais informacoes sobre a biblioteca e o otimo projeto, no site: https://pypi.org/project/pyTelegramBotAPI/

O bot foi gerado no Telegram seguindo a documentacao do aplicativo (https://core.telegram.org/bots) e a API token gerada salva em uma variavel de ambiente para ser usada pelo robo.

## Documentação
Todas as funcoes do codigo incluem docstring com explicacoes em ingles dos parametros esperados e do resultado retornado.