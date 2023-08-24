function jsonToNestedBulletPoints(jsonObj, parentElement) {
    let ulElement = document.createElement('ul');

    for (const key in jsonObj) {
        if (jsonObj.hasOwnProperty(key)) {
            let liElement = document.createElement('li');
            let aElement = document.createElement('a');

            if (typeof jsonObj[key] === 'object') {
                fetch(`/find_information/${key.toLowerCase()}`, {method : 'POST'})
                    .then(res => res.json())
                    .then(meta => {
                        aElement.textContent = `${key} (${meta.missing !== null ? meta.missing.toString() + ' entity / entities with missing information' : 'no available information'})`;
                        aElement.href = '';
                        aElement.target = '_blank';

                        jsonToNestedBulletPoints(jsonObj[key], aElement)
                        liElement.appendChild(aElement);
                        ulElement.appendChild(liElement);
                    })
                    .catch(e => console.error(e))
            } else {
                liElement.appendChild(aElement);
                ulElement.appendChild(liElement);
            }
        } 
    }

    parentElement.appendChild(ulElement);
}