## Construct a Kowledge Graph of academic papers


## get new papers' title from academic websites

URL_ARXIVCL = 'https://arxiv.org/list/cs.CL/recent'
URL_CLJ   = 'https://www.mitpressjournals.org/toc/coli'
URL_ACL   = 'http://www.acl2019.org/EN/program.xhtml'
URL_NAACL = 'https://naacl2019.org/program/accepted/'
URL_CVPR  = ''
URL_AAAI  = ''

paper_list


    
class get_website_papers:
    def __init__(URL_ROOT, num_limit, get_author = False, get_institute = False):
        self.url_root = URL_ROOT
    
    def get_news():

        return()



## construct dict of authors, tricks, modules, tasks, challenges
class aca_paper:
    def __init__(title, publication, author, abstract, available_link):
        self.title = title
        self.publication = publication
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
           'Transformer':'Attention is all you need'
           'Graphical Decomposition':''
           'GNN':'Graph Convolutional Networks']

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
           'memory':'memory networks']

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
           'generation':'',
           'summarization':'',
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
