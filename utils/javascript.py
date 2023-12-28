'''
Contains helper functions to generate JavaScript to be executed
on the client side
'''

def create_metadata(raw_data, raw_filename, metadata, meta_filename):
    '''
    Returns JavaScript code that renders the Taxonium component.
    '''
    return('''
        let metaData = {
            status: "loaded",
            filetype: "meta_csv",
            filename: "%s",
            data: `%s`,
        };
           
        let sourceData = {
            status: "loaded",
            filename: "%s",
            data: `%s`,
            filetype: "nwk",
            metadata: metaData,
        }
    ''' % (meta_filename, metadata, raw_filename, raw_data))

def render_taxonium():
    '''
    Displays the code for the taxonium component to render.  This function currently just returns the 
    boilerplate code required to implement Taxonium as a React component, but it may be useful in the future
    when we need to modify how Taxonium renders.
    '''
    return('''
        ReactDOM.render(
            React.createElement(Taxonium, {sourceData : sourceData}),
            document.querySelector('.content')
        );
        ''')