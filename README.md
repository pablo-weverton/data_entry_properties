# data_entry_properties

What's up, Dev? 😜

Já passou pela situção de transcrever uma grande quantidade de dados para uma tabela?
É uma tarefa bem maçante e árdua não é?! 👌

Pensando nisso, tomei como exemplo a procura de casas disponíveis no site Zillow e uma fiz um Web
Scraping com Beatiful Soup e automaziei o preenchimento de um form com a ajuda do Selenium.

O sistema consiste em ir ao site escolhido, fazer uma raspagem de dados e adiciona-los a uma tabela
via automatização.

![tabela_exemplo](https://user-images.githubusercontent.com/90657749/159280402-6a7afcfe-6e56-46ff-a354-567b7b42ad51.png)

##

      GUIA DE CONFIGURAÇÃO
      
- Baixei os arquivos disponíveis para download(main.py,fill_data.py)
- Proucure por seu HTTP hearder no site: http://myhttpheader.com e preencha os dados requeridos no programa (Accept-Language, User-Agent)
- Preencha a URL do site que você quer utilizar (No programa a URL presente é a do site Zillow)
- Certifique-se de baixar o chromewebdriver no site: https://chromedriver.chromium.org/downloads
- Preencha o PATH do download feito com 'chromedriver.exe' no final do PATH
- Crie um form no google forms colocando inputs para os dados raspados no site
![form_exemplo](https://user-images.githubusercontent.com/90657749/159283455-dd5943e2-73d8-4e41-b4ef-6c5d4b3067b6.png)
- Perceba que no arquivo fill_data.py existe uma classe que preenche apenas três inputs, logo, certifique-se de ter apenas 3.
- Cada input de formulário tem um caminho html, logo, os comandos de preenchimento de dados devem ser alterados na classe Fill.
- Rode o arquivo main.py

OBS* SINTA-SE À VONTADE PARA ALTERAR O CÓDIGO COMO QUISER

Enjoy it! 😉
