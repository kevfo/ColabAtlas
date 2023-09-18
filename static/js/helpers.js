const determineFileName = (genus) => {
    // Given a 'genus', return the appropriate file name
    let name = 'misc/raw_data/';
    switch(genus) {
        case 'r':
            name += 'r_taxonfull.jsonl';
            break;
        case 'g':
            name += 'g_jsonl.jsonl';
            break;
        case 'v':
            name += 'v_taxonfull.jsonl';
            break;
    }
    return name;
}