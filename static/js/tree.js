// Deals with the construction of the 
// Species tree as shown on https://phytozome-next.jgi.doe.gov/

const TREE_DISPLAY = document.querySelector('.treeDisplay');
const TREE_SELECTOR = document.querySelector('#jsonData');
const OPTIONS = document.querySelector('#displayOptions');

const updateTree = () => {
    TREE_DISPLAY.innerHTML = ''
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

    let loadingDots = window.setInterval(function() {
        TREE_DISPLAY.innerText = 'Loading';
        if (TREE_DISPLAY.innerText.length >= 10) {
            TREE_DISPLAY.innerText = 'Loading';
        } else {
            TREE_DISPLAY.innerText += '.';
        }
    }, 500)

    fetch(cdnLink)
        .then(response => response.json())
        .then(resData => {
            clearInterval(loadingDots); 
            TREE_DISPLAY.innerText = '';
            jsonToNestedBulletPoints(resData, TREE_DISPLAY);
        })
}


TREE_SELECTOR.addEventListener('change', () => {
    updateTree();
});
OPTIONS.addEventListener('change', () => {
    updateTree();
})

// Add event listeners for when somebody clicks on an item: