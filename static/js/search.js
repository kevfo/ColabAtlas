const SUBMIT_BUTTON = document.querySelector('#submitButton');
const USER_QUERY = document.querySelector('#queryInput');
const RESULTS = document.querySelector('.results');

const submitResults = () => {
    event.preventDefault();
    if (!USER_QUERY.value.length) {
        RESULTS.innerHTML = `<p> Please enter a search query to search for a species! </p>`;
    } else {
        RESULTS.innerHTML = '<p> Searching... </p>';
        fetch('/find', {method : 'POST', body: USER_QUERY.value})
        .then(response => response.json())
        .then(resData => {
            if (typeof resData === 'object') {
                RESULTS.innerHTML = `<p> Taxonomic ID: ${resData.taxid} </p> <p> RNA Count: ${resData.rna} </p> <p> Illumina RNA Count: ${resData.ill} </p>`
            } else {
                RESULTS.innerHTML = `<p> No information found </p>`
            }
        })
        .catch(error => console.error(error));
    }
}

SUBMIT_BUTTON.addEventListener('click', () => {submitResults()});