from html.parser import HTMLParser
from urllib import parse

#temp change
from urllib.request import urlopen

class LinkFinder(HTMLParser):

    def error(self,message):
        pass

    def __init__(self, base_url, page_url):
        super().__init__()
        self.base_url = base_url
        self.page_url =page_url
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag =='a':
            #every tag has attributes and they have some value
            for (attributes, value) in attrs:
                if attributes =='href':
                    url = parse.urljoin(self.base_url, value)
                    self.links.add(url)

    def page_links(self):
        return self.links

#there is a method called handle start tag

#temp change
'''response = urlopen('https://en.wikipedia.org/wiki/Adjacency_list')
if response.getheader('Content-Type') == 'text/html; charset=UTF-8':
    html_bytes = response.read()
    html_string = html_bytes.decode('utf-8')
test_finder = LinkFinder('https://en.wikipedia.org/wiki/Adjacency_list','https://en.wikipedia.org/wiki/Adjacency_list')
test_finder.feed(html_string)
'''
