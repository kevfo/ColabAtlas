'''
Provides helper functions for the search functionalities
'''

import pickle 

def find_queries(query):
    '''
    Searches pickled_taxid for the organism name.
    '''
    with open('data/pickles/rna_counts_species', 'rb') as taxid:
        data = pickle.load(taxid)
        result = data.get(query.lower(), None)
        if result is None:
            return {'item_chosen' : query}
        return {'item_chosen' : query, 'taxid' : result['taxid'], 'rna' : result['rna_count'], 'ill' : result['illumina_rna_count']}

def find_entity_information(query):
    '''
    Returns information about a chosen entity in a tree.  Until more 
    information is provided, this function will just return the amount of children
    an object has (if not the amount of RNA information available for 
    species).
    '''
    with open('data/pickles/rna_counts', 'rb') as info:
        data, refined, result = pickle.load(info), ' '.join([i for i in query.split() if '[' not in i and ']' not in i and not i.isdigit()]), None
        key = refined.lower()
        if 'class' in query:
            result = data['classcount'].get(key)
        elif 'family' in query:
            result = data['familycount'].get(key)
        elif 'genus' in query:
            result = data['genuscount'].get(key)
        elif 'order' in query:
            result = data['ordercount'].get(key)
        return {'query' : refined, 'count' : result}
