'''
Contains helper functions to generate JavaScript to be executed
on the client side
'''

def render_taxonium(option, raw_data):
    '''
    Returns JavaScript code that renders the Taxonium component.
    '''
    return('''
        let raw_data = `%s`, fileName = determineFileName("%s");

        const sourceData = {
            filename: fileName,
            filetype: "jsonl",
            data: raw_data,
            status: "loaded"
        }  

        ReactDOM.render(
            React.createElement(Taxonium, { sourceData : sourceData}),
            document.querySelector('.content')
        );
    ''' % (raw_data, option))
