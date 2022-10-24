from urllib.request import urlopen
from link_finder import LinkFinder
from general import *
#we need to share the same queue and crawled list amongst many spiders.
# For that we need

class Spider:
    #we need a shared class. All instance need to share the variables. Class variables:
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''
    crawled_file =''
    queue =set()
    crawled = set()
    def __init__(self, project_name, base_url,domain_name):
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name + '/queue.txt'
        Spider.crawled_file = Spider.project_name +'/crawled.txt'
        self.boot()

        #we need what page its crawling in
        self.crawl_page('first spider', Spider.base_url)

    @staticmethod
    def boot():
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name, Spider.base_url)
        #as soon as we boot up it takes links and saves
        #it as a set for faster operation. So below takes a file
        #of links and convert it to sets
        Spider.queue = file_to_set(Spider.queue_file)
        Spider.crawled = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawl_page(thread_name, page_url, link_id):
        #we need the prog telling us what page its crawling
        if page_url not in Spider.crawled:
            print(thread_name + ' now crawling ' + page_url)
            print('Queue ' + str(len(Spider.queue)) + ' | Crawled ' + str(len(Spider.crawled)))
            Spider.add_links_to_queue(Spider.gather_links(page_url), link_id)
            Spider.queue.remove(page_url)
            Spider.crawled.add(page_url)
            Spider.update_files()

#in the home page there is no use of multiple spiders as there
#is just one page in queue(the home page). Instead we crawl homepage with one spiders
#and then use multihreading for the links in homepage

    @staticmethod
    #below fn connects to a site, takes html in bits and
    #converts to a str format sends it to the LinkFinder
    #that parses through it and gets a set of all of the
    #urls and if there are no issues it returns them for us
    #to view
    def gather_links(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if response.getheader('Content-Type') == 'text/html; charset=UTF-8':
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
                #print(html_string)
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)

        except:
            print("error: cannot crawl page, this message is from Spider.gather_links fn")
            return set()

        return finder.page_links()

    @staticmethod
    #this fn takes a set of links and adds it to
    #the already excisting waiting list of links
    def add_links_to_queue(links,link_id):
        for url in links:
            if url in Spider.queue:
                continue
            if url in Spider.crawled:
                continue
            #makes sure it doesnt leave the site we want
            #to crawl, for eg if we're crawling wikipedia
            #below line makes sure it doesnt leave wikipedia
            if Spider.domain_name not in url:
                continue
    #Dont want: , # , % , ?, 'Category'
            if '#' in url:
                continue
            if '%' in url:
                continue
            if '?' in url:
                continue
            if 'Category' in url:
                continue
            if 'https://en.wikipedia.org' not in url:
                continue
            if 'Wikipedia:' in url:
                continue
            if 'Help:' in url:
                continue

            Spider.queue.add(url)

    @staticmethod
    def update_files():
        set_to_file(Spider.queue , Spider.queue_file)
        set_to_file(Spider.crawled, Spider.crawled_file)
