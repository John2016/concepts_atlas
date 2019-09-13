# *-utf-8 - *

## modules would be initialized by name list or dict
## is_NN and original_paper will be done later
class classical_modules:
    def __init__(name, is_NN=True, original_paper='', description):
        self.name = name
        self.is_NN = is_NN
        self.original_paper = original_paper
        self.description = description

    def get_is_NN(self):
        ## maybe achieved by hand

    def get_ori_paper(self):
        url = ''
        ## be completed in future

## same with classical_modules
class special_tricks:
    def __init__(name, original_paper, description):
        self.name = name
        self.original_paper = original_paper
        self.description = description

    def get_ori_papers(self):
        # be done later
        self.original_paper = ['']

## same with above
class task_category:
    def __init__(name, description, sota_paper = None, father_task = None, son_task = None, brother_task = None):
        self.name = name
        self.description = description
        self.sota_paper = sota_paper
        self.father_task = father_task
        self.son_task = son_task
        self.brother_task = brother_task

    def get_sota(self):
        self.sota_paper = ''

    def get_neighbor_task(self):
        self.father_task = None
        self.son_task = None
        self.brother_task = [None, None]

## easy initialization        
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
           'CRF':'conditional random fields'
           'MemNN':'Memory Neural Networks']

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
           'text classification':''
           'language representation':'pre-trained model']

challenges = ['scale':'',
              'efficiency':'',
              'end-to-end':'',
              'on-device':'',
              'complex':'',
              'constrained':'',
              'large-scale':'',
              'task oriented':'',
              'mutti':'',
              'knowledge base':'KGs should be used in this task'
              'enhanced':'normal challenges']

academic_stopwords = ['with',
                      'by',
                      'based on',
                      'for',
                      'over']
