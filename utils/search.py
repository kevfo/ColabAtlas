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
    with open('data/pickles/missing_info_counts', 'rb') as info:
        data, refined = pickle.load(info), ' '.join([i for i in query.split() if '[' not in i and ']' not in i and not i.isdigit()]).lower()
        result = data.get(refined, None)
        if result is None:
            return find_queries(refined) 
        else:
            return {'item_chosen' : refined, 'missing' : data[refined]}
