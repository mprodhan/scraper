import requests
from bs4 import BeautifulSoup
# the reason BeautifulSoup is being imported from bs4, it is due to the fact that 
# BeauttifulSoup is modified by BeautifulSoup4(bs4).
import pprint


res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
# print(res) gives a "Response [200]"
print(res)
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
# print(soup)
# print(soup) will give you all of the html elements parsed out of the text from the source.

# print(soup.body)
# print(soup.body) will give you the body of the html in a cleaner format

# print(soup.body.contents)
# gives you the main contents of the body

# print(soup.find_all('title'))
# find_all method reduces the contents to the selected html elements

# print(soup.title)
# the difference between the top and this method, is that the above allows one to find objects
# this object, where instead of a soup.method(''), a soup.tag, will give one a direct htttml tag with
# information attached to that tag. The latter is much cleaner.

# print(soup.a)
# The find_all method gives you all of the a, this html tag method gives one the first a tag. 

# print(soup.find(id='score_25344762'))
# .find allows for a specific data to be tracked

# print(soup.select('.score'))
# .select method allows not only for captture of html data, but also with css seletor data.

# print(soup.select('#score_25344762'))
# print(soup.select('.storylink')[-1:])

links = soup.select('.storylink')
subtext = soup.select('.subtext')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2

print(subtext[0])
# the above print statement can be chained as well
print(subtext[0].get('id'))

def sort_stories_votes(hnlist):
    return sorted(hnlist, key=lambda k:k['votes'], reverse=True)

def create_custtom_hn(links, votes):
    hn = []
    for idx, item in enumerate(links):
        title = links[idx].getText()
        href = links[idx].get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace('points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_votes(hn)

pprint.pprint(create_custtom_hn(links, subtext))
# Tech Debt:Need to be able to call create_custom_hn(mega_links, mega_subtext)
# This resolution would be able to bind pages 1 and 2. 
# However, a better code would be to dynamically list from all pages.