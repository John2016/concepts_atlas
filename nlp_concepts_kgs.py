## Construct a Knowledge Graph of academic papers


## get new papers' title from academic websites

URL_ARXIVCL = 'https://arxiv.org/list/cs.CL/recent'
URL_ARXIVCL_DAILY = 'https://arxiv.org/list/cs.CL/new'
URL_CLJ   = 'https://www.mitpressjournals.org/toc/coli'
URL_ACL   = 'http://www.acl2019.org/EN/program.xhtml'
URL_NAACL = 'https://naacl2019.org/program/accepted/'
URL_CVPR  = ''
URL_AAAI  = ''

paper_list


    

""" from urllib.request import urlretrieve
from urllib.request import urlopen
import urllib
from bs4 import BeautifulSoup  """
import numpy as np
import pandas as pd
import re
import os
import json
from keywords import *
 

def get_info_json(onoff_line = False):
    ## run the scrapy or not

    ## get information from json file
    

class get_website_papers:
    def __init__(URL_ROOT, num_limit, get_author = False, get_institute = False):
        self.url_root = URL_ROOT
    
    def get_news():
        html   = urlopen(URL_ARXIVCL)
        bs_obj = BeautifulSoup(html, "lxml")

        ## find the link of the next page
        ## <small>[ total of 123 entries:  <b>1-25</b> | <a href="/list/cs.CL/pastweek?skip=25&amp;show=25">26-50</a> | <a href="/list/cs.CL/pastweek?skip=50&amp;show=25">51-75</a> | <a href="/list/cs.CL/pastweek?skip=75&amp;show=25">76-100</a> | <a href="/list/cs.CL/pastweek?skip=100&amp;show=25">101-123</a>  ]</small>
        paper_url = bs_obj.findAll("span",{"class":"list-identifier"}).find("a")
        paper_url = paper_url[1].href
        ## find the list of paper information
        title_list = bs_obj.findAll("div", {"class":"list-title mathjax"})
        for title in title_list:
            title_name = title
            publication = 'Arxiv'
            pub_time = ''

            author = title.find("div",{"class":"list-authors"}).find("a")
            abstract = title.parent.find("p",{"class","mathjax"})
            if (abstract is not None):
                download = title.parent.parent.previous_sibling.previous_sibling.find("a", {"title":"Download PDF"}).attrs['href']
                available_link = 'https://arxiv.org' + download
            # 'comments' part will say whether be accepted by some conf or journal

            
        # return structed information of {title,scholar,abstract,publication,datetime}
        return()



## construct dict of authors, tricks, modules, tasks, challenges
class aca_paper:
    def __init__(title, publication, pub_time, author, abstract, available_link=null):
        self.title = title
        self.publication = publication
        self.pub_time = pub_time
        self.author = author
        self.abstract = abstract
        self.available_link = available_link

    ## analysis title (and abstract later) and extract key informations
    ## matching-rules or machine learning methods
    ## keywords_list would be [modules, tricks, tasks, challenges]
    def title_analysis(self, keywords_list):
        self.tasks = ''
        self.challenge = ''
        self.module = ''
        self.trick = ''

## information of scholars, initialized by just name
## h_factor and high cited papers would be collected from GOOGLE 
class scholar:
    def __init__(name, h_factor=0, hcited_paper=''):
        self.name = name
        self.h_factor = h_factor
        self.hcited_paper = hcited_paper

    def get_h_google(self):
        h_factor_url = 'scholar.google.com\'
        ## scrapy
        self.h_factor = 0
        self.hcited_paper = ['']


## construct relationship between papers and tasks, challenges, modules and tricks
## by hard rules or simple ML methods
## out-program file and in-program class, if info is got through scrapy, then out-program file
class graph_concept:
    def __init__(json_file, ):

    
    ## 'e' means constructing new entity class 
    def e_titles(self):

        for paper in self.titles:
        acapaper(self.)
        return 

    ## insert all title entities
    def insert_entity_title(self):
        

    ## 'r' means constructing new relation class
    def r_title_scholar(self):

        return

    # insert relationship between title and tasks
    @staticmethod
    def insert_relation_tt(title, task):
        

        return

    # insert relationship between title and modules
    @staticmethod
    def insert_relation_tm():

        return

    def r_title_challenge(self):

        return

    def r_title_tricks(self):

        return

    def init_neo(self, url, user, password):
        self._driver = GraphDatabase.driver(url, auth=(user, password))

    def close_neo(self):
        self._driver.close()

    def resolve_neo(self):
        return

    @staticmethod
    def insert(sth):
        return





## construct neo4j graph based on structured information of academic papers
import neo4jmk

class data_to_graph:

    
