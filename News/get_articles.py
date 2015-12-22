import newspaper
from pathlib import Path


news_folder = Path("E:\\", "code", 'news')

sites = {'exame': 'http://exame.abril.com.br/',
              'g1': ['http://g1.globo.com/politica', 
                     'http://g1.globo.com/tecnologia', 
                     'http://g1.globo.com/mundo', 
                     'http://g1.globo.com/economia'],
              'uol': 'http://noticias.uol.com.br/',
              'terra': 'http://noticias.terra.com.br/'}

news = newspaper.build(
    sites['terra'], language='pt', memoize_articles=True, fetch_images=False)


for cat in news.category_urls():
    print(cat)
# a.download()
# a.parse()


