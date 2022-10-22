import os
import pandas as pd

#attempt to use pandas, adding the crawled and queued links to the dataframe and then getting its metadata.
def create_project_df(file_name_crawled, file_name_queued):
    print('creating dataframe with crawled and queued links ')
    df = pd.DataFrame()
    data_crawled = pd.read_csv(file_name_crawled)
    data_queued = pd.read_csv(file_name_queued)
    dataframe_links = pd.concat([data_queued,data_crawled])
    return dataframe_links

#each website you crawl is a separate project (folder)
def create_project_dir(directory):
  if not os.path.exists(directory):
    print('creating project' + directory)
    os.makedirs(directory)

create_project_dir('wikicrawl')

def create_data_files(project_name,base_url):
  queue = project_name+'/queue.txt'
  crawled = project_name+'/crawled.txt'
  if not os.path.isfile(queue):
    write_file(queue, base_url)
  if not os.path.isfile(crawled):
    write_file(crawled,'')

    #create a new file
def write_file(path,data):
  f=open(path,'w')
  f.write(data)
  f.close()

create_data_files('wikicrawl','https://en.wikipedia.org/wiki/Adjacency_list')

#add data onto an existing file
def append_to_file(path,data):
  with open (path, 'a',  encoding="utf-8") as file:
    file.write(data+'\n')


#delete content of an excisting file
def delete_file_contents(path):
  with open(path,'w'):
    pass

    #'set' can only have unique elements
#read a file and convert each line to set items
#rt : read text file
def file_to_set(file_name):
    results = set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results


 #iterate through a set, each item will be a new line it the file
def set_to_file(links,file):
  delete_file_contents(file)
  for link in sorted(links):
    append_to_file(file,link)

dataframe_links = create_project_df('wikicrawl/crawled.txt', 'wikicrawl/queue.txt')
dataframe_links.to_csv(r'D:\Users\Pratha S Dongre\Downloads\web_scraping\web_scraping_crawling_pratha\testproj\df_links.csv')
