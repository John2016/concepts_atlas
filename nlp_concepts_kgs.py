## Construct a Kowledge Graph of academic papers


## get new papers' title from academic websites

URL_ARXIVCL = 'https://arxiv.org/list/cs.CL/recent'
URL_ARXIVCL_DAILY = 'https://arxiv.org/list/cs.CL/new'
URL_CLJ   = 'https://www.mitpressjournals.org/toc/coli'
URL_ACL   = 'http://www.acl2019.org/EN/program.xhtml'
URL_NAACL = 'https://naacl2019.org/program/accepted/'
URL_CVPR  = ''
URL_AAAI  = ''

paper_list


    

from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup 
import numpy as np
import pandas as pd
import urllib
import re
import os
 



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

class scholar:
    def __init__(name, h_factor, hcited_paper):
        self.name = name
        self.h_factor = h_factor
        self.hcited_paper = hcited_paper

class classical_modules:
    def __init__(name, is_NN=True, original_paper,description):
        self.name = name
        self.is_NN = is_NN
        self.original_paper = original_paper
        self.description = description

class special_tricks:
    def __init__(name, original_paper, description):
        self.name = name
        self.original_paper = original_paper
        self.description = description

class task_category:
    def __init__(name, description, sota_paper, father_task, son_task, brother_task):
        self.name = name
        self.description = description
        self.sota_paper = sota_paper
        self.father_task = father_task
        self.son_task = son_task
        self.brother_task = brother_task

class special_challenges:
    def __init__(name, description):
        self.name = name
        self.description = description

## maybe we should use dict to construct both name and concepts
modules = ['CNN':'Convolutional Neural Networks',
           'ResNet':'Residual',
           'LSTM':'Long Short-Term Memory Networks',
           'RNN':'Recurrent Neural Networks',
           'Transformer':'Attention is all you need',
           'Graphical Decomposition':'Matrix',
           'GNN':'Graph Convolutional Networks',
           'GAN':'Generative Adversarial Networks',
           'CRF':'conditional random fields']

tricks  = ['sparse':'',
           'dropout':'',
           'pre-train':'',
           'attention':'self-attention',
           'multimodal':'',
           'hierarchical':'',
           'quantilization':'',
           'multi-hop':'',
           'rank':''
           'distributinal':'',
           'semi-supervised':'',
           'bidirectional':'',
           'memory':'memory networks',
           'multi-hop':''，
           'bi':'bi-direction something',
           'semi-':'semi-supervised'
           'tree':'combined with TREE structure']

tasks   = ['QA':'Question and Answer',
           'relation':'relation extraction and relation reasoning',
           'encoding':'natural language encoded into vectors, or compressed sentence representation',
           'comprehensive':'',
           'translation':'machine translation',
           'SQL':'natural language sequence to SQL',
           'chatbot':'',
           'dialogue':'',
           'inferring':'',
           'entity':'entity recognition',
           'semantition':'semantic',
           'text processing':'',
           'graph network':'constructing graph networks, related to relation reasonning',
           'task generation':'',
           'matching':'',
           'onversation generation':'',
           'summarization':'text summarization',
           'text classification':'']

challenges = ['scale':'',
              'efficiency':'',
              'end-to-end':'',
              'on-device':'',
              'complex':'',
              'constrained':'',
              'large-scale':'',
              'task oriented':'',
              'mutti':'',
              'knowledge base':"KGs should be used in this task"]

academic_stopwords = ['with',
                      'by',
                      'based on',
                      'for',
                      'over']


## construct relationship between papers and tasks, challenges, modules and tricks
## by hard rules or simple ML methods
class graph_cooncept:
    def __init__(structed_info):

    ## 'e' means constructing new entity class 
    def e_titles(self):

        for paper in self.titles:
        acapaper(self.)
        return

    ## 'r' means constructing new relation class
    def r_title_scholar(self):

        return

    def r_title_tasks(self):

        return

    def r_title_modules(self):

        return

    def r_title_challenge(self):

        return

    def r_title_tricks(self):

        return

    





## construct neo4j graph based on structured information of academic papers
import neo4jmk

class data_to_graph:

    def __init__(self, url, user, password):
        self._driver = GraphDatabase.driver(url, auth=(user, password))

    def close(self):
        self._driver.close()

    def resolve(self):
        return

    @staticmethod
    def __insert(sth):
        return
