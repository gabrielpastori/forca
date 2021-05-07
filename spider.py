import scrapy

class TerraSpider(scrapy.Spider):
    name = 'terra' # Nome do spider
    start_urls=['https://www.terra.com.br/noticias/'] # Lista de urls que iremos aplicar o scrapping

    def parse(self, response): 
        for noticia in response.css('.news .title'): # Para cada notícia
            yield { # Dados que iremos extrair, por meio de expressões css
                'source':'Terra',
                'title': noticia.css('h3 a::text').get(),
                'link': noticia.css('h3 a').attrib['href'],
            }

class JpSpider(scrapy.Spider):
    name='jp' # Nome do spider
    start_urls = ['https://jovempan.com.br/tag/rio-de-janeiro/'] # Lista de urls que iremos aplicar o scrapping
    count=0 # Contador para controlar o número de páginas que iremos aplicar o scrapping
    def parse(self, response):
        for noticia in response.css('.post-title'): # Para cada notícia
            yield{ # Dados que iremos extrair, por meio de expressões css
                'source': 'Jovem Pan',
                'title': noticia.css('a::text').get(),
                'link': noticia.css('a').attrib['href'],
            }
        next_page = response.css('a[aria-label="Próxima"]').attrib['href']  # Extrai o link do anchor que permite passar para a próxima página
        if next_page is not None and self.count<4: # Próxima página se existir e se a contagem for menor que 4 (arbitrário)
            yield response.follow(next_page, callback=self.parse) # Executa novamente o parser para aplicar o scrapping na próxima página
        self.count+=1 # Adicionamos 1 no contador de páginas

class IgSpider(scrapy.Spider):  
    name='ig' # Nome do spider
    start_urls = ['https://www.ig.com.br/#pagina1']  # Lista de urls que iremos aplicar o scrapping

    def parse(self, response):
        for noticia in response.css('div[data-tb-region-item=data-tb-region-item]'): # Para cada notícia
            yield{ # Dados que iremos extrair, por meio de expressões css
                'source':'IG',
                'title': noticia.css('h2 a::text').get(),
                'link': noticia.css('h2 a').attrib['href'],
            }