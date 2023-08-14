// Deals with the construction of the 
// Species tree as shown on https://phytozome-next.jgi.doe.gov/

const TREE_DISPLAY = document.querySelector('.treeDisp');
const TREE_SELECTOR = document.querySelector('#jsonData');
const INFO_DISP = document.querySelector('.disp');

const determineEntity = (entity) => {
    if (entity.includes('[genus]')) {
        return 'species';
    } else if (entity.includes('[family]')) {
        return 'genuses';
    } else if (entity.includes('[class]')) {
        return 'families';
    } else {
        return 'entities';
    }
}

const showInformation = () => {
    let chosen = event.target.innerText;
    fetch('/find_entity', {method: 'POST', body: chosen})
    .then(response => {return response.json()})
    .then(resData => {
        if (resData.missing !== undefined) {
            INFO_DISP.innerHTML = `<h3> You chose: ${resData.item_chosen} </h3> 
            <p> Amount of ${determineEntity(chosen)} with missing data: ${resData.missing} </p>`
        } else if (resData.ill !== undefined) {
            INFO_DISP.innerHTML = `<h3> You chose: ${resData.item_chosen} </h3> 
            <p> Amount of Illumina RNA data: ${resData.illumina_rna_count} </p> 
            <p> Amount of RNA: ${resData.rna_count} </p>`
        } else {
            INFO_DISP.innerHTML = `<h3> You chose: ${resData.item_chosen} </h3>
            <p> No available information! </p>`
        }
    })
    .catch(error => console.error(error))
}

const updateTree = () => {
    if (TREE_DISPLAY.innerHTML.length !== 0) {
        TREE_DISPLAY.innerHTML = ''
    }
    let value = TREE_SELECTOR.value, cdnLink = '';
    
    switch(value) {
        case 'G':
            cdnLink = 'https://atlascdn.netlify.app/G_taxon_fulllist_edited.json';
            break;
        case 'R':
            cdnLink = 'https://atlascdn.netlify.app/R_taxonfull_edited.json';
            break;
        case 'V':
            cdnLink = 'https://atlascdn.netlify.app/V_taxonfull_edited.json';
            break;
        default:
            return;
    }

    fetch(cdnLink)
    .then(response => response.json())
    .then(resData => {
        let reformat = updateFieldInJSON(resData, 'type', Tree.FOLDER);
        let tree = new Tree(TREE_DISPLAY);
        tree.json(reformat);
        document.querySelectorAll('[data-type="folder"]').forEach(item => {
            item.addEventListener('click', showInformation)
        })
    })
}

TREE_SELECTOR.addEventListener('change', () => {
    updateTree();
});