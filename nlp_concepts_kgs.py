## Construct a Kowledge Graph of academic papers


## get new papers' title from academic websites

URL_ARXIV = ''
URL_ACL   = ''
URL_CVPR  = ''
URL_AAAI  = ''

paper_list

class aca_paper:
    def __init__(title, publication, author, institute):
        self.title = title
    
class GetPapers::


    def __init__(URL_ROOT, num_limit, get_author = False, get_institute = False):

    
    def get_news():

        return()



## construct dict of authors, tricks, modules, tasks, challenges
## maybe we should use dict to construct both name and concepts
modules = ['CNN','ResNet','LSTM','RNN','Transformer']
tricks  = ['sparse','dropout','pre-train','attention']
tasks   = ['QA','relation','encoding','comprehensive']
challenges = ['scale','efficiency']


## construct relationship between papers and tasks, challenges, modules and tricks
## by hard rules or simple ML methods




## construct neo4j graph based on structured information of academic papers
import neo4jmk
