import requests
import lxml
import bs4

base_url = 'http://quotes.toscrape.com'

page_text = requests.get(base_url)
souped_page_text = bs4.BeautifulSoup(page_text.text, "lxml")
authors = [author.text for author in souped_page_text.select('.author')]

url_to_step = 'http://quotes.toscrape.com/page/{}'

i = 1
while True:
    subsequent_page_text = requests.get(url_to_step.format(i))
    soup_the_text = bs4.BeautifulSoup(subsequent_page_text.text, "lxml")
    new_authors = [new_author.text for new_author in soup_the_text.select('.author')]
    for author in new_authors:
        if author not in authors:
            authors.append(author)
        else: pass
    i += 1
    pages_done = soup_the_text.select('.next')
    if bool(pages_done) == False: break
    else: continue

author_set = set(authors)
print(author_set)
