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
        data = pickle.load(info)
        for i in data:
            if data[i].get(query.lower()) is not None:
                return data[i].get(query.lower())
        return None

def get_color(entity):
    '''
    Given an 'entity', search for an appropriate color scheme
    based on the pickled file tree_colors
    '''
    with open('data/pickles/tree_colors', 'rb') as colors:
        data, key = pickle.load(colors), entity.lower()
        for color, items in data.items():
            if key in items:
                return color.upper()
    return '#000000'

def is_species(entity):
    with open('data/pickles/is_species', 'rb') as info:
        data = pickle.load(info)
        return data.get(entity.lower(), False)