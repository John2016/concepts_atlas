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

    ## create 'Paper' node in neo4j graph database
    @classmethod
    def insert_entity_title(cls, tx, paper):
        try:
            assert(isinstance(title, aca_paper))
        except AssertionError as ee:
            print('Title is not aca_paper class')
            return
        tx.run("CREATE (:Paper {title: $title, pub_time: $pub_time, abstract:$abstract, available_link: $available_link})",\
            title=paper.title, pub_time = paper.pub_time, abstract = paper.abstract, available_link = paper.available_link)

    ## create 'Task' node in neo4j graph database
    @classmethod
    def insert_entity_tasks(cls, tx, tasks):
        try:
            assert(isinstance(tasks, task_category))
        except AssertionError as ee:
            print('Task is not task_category class')
            return
        tx.run("CREATE (:Task {name: $name, description: $description, sota_paper: $sota_paper})",\
            name = tasks.name, description = tasks.description, sota_paper = task.sota_paper)
    
    ## create 'Challenge' node in neo4j graph database
    @classmethod
    def insert_entity_challenges(cls, tx, challenge):
        try:
            assert(isinstance(challenge, special_challenges))
        except AssertionError as ee:
            print("Challenge is not special_challenges class")
            return
        tx.run("CREATE (:Challenge {name: $name, description: $description})",\
            name = challenge.name, description = challenge.description)
        return

    ## create 'Modules' node in neo4j graph database
    @classmethod
    def insert_entity_modules(cls, tx, module):
        try:
            assert(isinstance(module, classical_modules))
        except AssertionError as ee:
            print('Module is not classical_modules class')
            return
        tx.run("CREATE (:Module {name: $name, description: $description})",\
            name = module.name, description = module.description)
        return

    ## create 'Tricks' node in neo4j graph database
    @classmethod
    def insert_entity_tricks(cls, tx, tricks):
        try:
            assert(isinstance(tricks, special_tricks))
        except AssertionError as ee:
            print('Tricks is not special_tricks class')
            return
        tx.run("CREATE (:Tricks {name: $name, description: $description})",\
            name = tricks.name, description = tricks.description)

    ## insert relationship between title and scholars
    ## create relationship 'Contribute' with no attribution
    ## Scholar node would be created before this 
    @staticmethod
    def insert_relation_ts(tx, paper):
        try:
            assert(isinstance(paper, aca_paper))
        except AssertionError as ee:
            print('Error')
            return
        if len(paper.author) > 0:
            for author in paper.author:
                tx.run("MATCH (pa:Paper), (au:Scholar) \
                    WHERE pa.title = $title AND au.name = $author \
                    CREATE (pa)-[r:Contribute]->(au) RETURN r", \
                        title = paper.title, author = author)
        return

    # insert relationship between title and tasks
    @staticmethod
    def insert_relation_tta(tx, paper, task):
        try:
            assert(isinstance(paper, aca_paper))
            assert(isinstance(task, task_category))
        except AssertionError as ee:
            print('Class error')
            return
        tx.run("MATCH (pa:Paper), (ta:Task) \
            WHERE pa.title = $title AND ta.name = $task \
                CREATE (pa)-[r:TaskIs]->(ta) RETURN r", \
                    title = paper.title, task = task.name)
        return

    # insert relationship between title and modules
    ## check whether 'module' should be class or str
    @staticmethod
    def insert_relation_tm(tx, paper, module):
        try:
            assert(isinstance(paper, aca_paper))
            assert(isinstance(module, classical_modules))
        except AssertionError as ee:
            print('Class error')
            return
        tx.run("MATCH (pa:Paper), (mo:Module) \
            WHERE pa.title = $title AND mo.name = $module \
                CREATE (pa)-[r:ModuleIs]->(mo) RETURN r", \
                title = paper.title, module = module.name)
        return

    # isnert relationship between titles and challenges
    @staticmethod
    def insert_relation_tc(tx, paper, challenge):
        try:
            assert(isinstance(paper, aca_paper))
            assert(isinstance(challenge, special_challenges))
        except AssertionError as ee:
            print('class error!')
        tx.run("MATCH (pa:Paper), (ch:Challenge) \
            WHERE pa.title = $title AND ch.name = $challenge \
                CREATE (pa)-[r:ChallengeIs]->(ch) RETURN r", \
                    title = paper.title, challenge = challenge.name)
        return

    # insert relationship between titles and tricks
    @staticmethod
    def insert_relation_ttr(tx, paper, trick):
        try:
            assert(isinstance(paper, aca_paper))
            assert(isinstance(trick, special_tricks))
        except AssertionError as ee:
            print('class error!')
        tx.run("MATCH (pa:Paper), (tr:Trick) \
            WHERE pa.title = $title AND tr.name = $trick \
                CREATE (pa)-[r:TrickIs]->(tr) RETURN r", \
                    title = paper.title, trick = trick.name)
        return

    # insert relationship between tasks and tasks, including father, son and brothers
    # relationship of father and son means 'include' and 'belong to'
    @staticmethod
    def insert_relation_tata(tx, task):
        try:
            assert(isinstance(task, task_category))
            # assert(isinstance(task_2, task_category))
        except AssertionError as ee:
            print("Class of Task Error!")
            return
        if not task.father_task is None:
            tx.run("MATCH (ta1:Task),(ta2,Task) \
                WHERE ta1.name = $task_1 AND ta2.name = $task_2 \
                    CREATE (ta1)-[r:IsFather]->(ta2) RETURN r", \
                        task_1 = task.father_task, task_2 = task.name)
        # we assume that one task may have multi son task
        if not task.son_task is None:
            for son_name in task.son_task:
                tx.run("MATCH (ta1:Task),(ta2:Task) \
                    WHERE ta1.name = $task_1 AND ta2.name = $task_2 \
                        CREATE (ta1)-[r:IsSon]->(ta2) RETURN r", \
                            task_1 = task.son_name, task_2 = task.name)
        if not task.brother_task is None:
            for brother_name in task.brother_task
        return
            
    # insert relationship between tasks and it's sota_paper
    @staticmethod
    def insert_relation_tsotat(tx, task):
        try:
            asssert(isinstance(task, task_category))
        except AssertionError as ee:
            print('Class error')
            return
        if not task.sota_paper is None:
            # check if the sota_paper exists in GraphDatabase
            result = tx.run("MATCH (ti:Paper {title: $name})", name = task.sota_paper)
            if len(result) = 0:
                tx.run("CREATE (:Paper {title: $title}), title = task.sota_paper)")
            tx.run("MATCH (ta:Task), (pa:Paper) \
                WHERE ta.name = $ta_name AND pa.title = $pa_title \
                    CREATE (ta)-[r:sota_paper]->(pa) RETURN r", \
                        ta_name = task.name, sota_name = task.sota_paper)
        return

    @staticmethod
    def init_neo(self, url, user, password):
        self._driver = GraphDatabase.driver(url, auth=(user, password))

    
    def close_neo(self):
        self._driver.close()

    def resolve_neo(self):
        return

    def main(self):
        # load data from json file and extract key information
        paper_list = []
        
        task_list = []
        challenge_list = []
        trick_list = []
        module_list = []



        # insert entities
        
        with self._driver.session() as session_ta:
            for task in task_list:
                session_ta.write_transaction(self.insert_entity_tasks, task)

        with self._driver.session() as session_ch:
            for challenge in challenge_list:
                session_ch.write_transaction(self.insert_entity_challenges, challenge)

        with self._driver.session() as session_tr:
            for trick in trick_list:
                session_tr.write_transaction(self.insert_entity_tricks, trick)

        with self._driver.session() as session_mo:
            for module in module_list:
                session_mo.write_transaction(self.insert_entity_modules, module)

        # write title node and relation related to it
        with self._driver.session() as session_p:
            for paper in paper_list:
                session_p.write_transaction(self.insert_entity_title, paper)
                session_p.write_transaction(self.insert_relation_tta, paper, paper.task)
                session_p.write_transaction(self.insert_relation_tc, paper, paper.challenge)
                session_p.write_transaction(self.insert_relation_tm, paper, paper.module)
                session_P.write_transaction(self.insert_relation_ttr, paper, paper.trick)

        # write other relations into graph database, including relations between tasks and sota-relation
        with self._driver.session() as session_o:
            for task in task_list:
                session_o.write_transaction(self.insert_relation_tata, task)
                session_o.write_transaction(self.insert_relation_tsotat, task)

    

    
