## Construct a Kowledge Graph of academic papers


## get new papers' title from academic websites

URL_ARXIV = ''
URL_ACL   = 'http://www.acl2019.org/EN/program.xhtml'
URL_CVPR  = ''
URL_AAAI  = ''

paper_list

class aca_paper:
    def __init__(title, publication, author, institute):
        self.title = title
    
class get_website_papers:
    def __init__(URL_ROOT, num_limit, get_author = False, get_institute = False):
        self.url_root = URL_ROOT
    
    def get_news():

        return()



## construct dict of authors, tricks, modules, tasks, challenges
class scholar:
    def __init__(name, h_factor, hcited_paper):
        self.name = name
        self.h_factor = h_factor
        self.hcited_paper = hcited_paper

class classical_modules:
    def __init__(name, is_NN=True, original_paper,decscrition):
        self.name = name
        self.is_NN = is_NN
        self.original_paper = original_paper
        self.decscrition = decscrition

class 

## maybe we should use dict to construct both name and concepts
modules = ['CNN':'Convolutional Neural Networks',
           'ResNet':'Residual',
           'LSTM':'Long Short-Term Memory Networks',
           'RNN':'Recurrent Neural Networks',
           'Transformer':'Attention is all you need']
tricks  = ['sparse':'',
           'dropout':'',
           'pre-train':'',
           'attention':'self-attention',
           'multimodal':'',
           'hierarchical':'',
           'quantilization':'',
           'multi-hop':'',
           'rank':'']
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
           'graph network':'constructing graph networks, related to relation reasonning']
challenges = ['scale':'',
              'efficiency':'',
              'end-to-end':'',
              'on-device':'']
academic_stopwords = ['with',
                      'by']


## construct relationship between papers and tasks, challenges, modules and tricks
## by hard rules or simple ML methods




## construct neo4j graph based on structured information of academic papers
import neo4jmk
