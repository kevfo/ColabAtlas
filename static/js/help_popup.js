const TAXONIUM_SIDEBAR = document.getElementsByClassName('flex flex-col px-4 divide-y text-sm flex-grow min-h-0 h-full bg-white shadow-xl border-t md:border-0 overflow-y-auto md:overflow-hidden')[0];
const SEARCH = document.getElementsByClassName('py-3 flex flex-col md:min-h-0')[0] ; SEARCH.classList.add('pb-2');

let help_node = document.createElement('div') ; help_node.className = 'space-y-2 py-3 text-gray-500 overflow-auto';
help_node.innerHTML = `
    <span class = 'text-gray-500 font-semibold text-sm pb-1'> How do I navigate the tree viewer? </span>
    <p> 
        You can use your cursor to pan the viewer to focus on a different part of the tree.  
        You can also use your mouse wheel or mousepad to zoom in on a particular area of a
        tree.
    </p>
    <p class = 'pb-1'>
        Alternatively, you may also wish to utilize the magnifying glasses on the bottom right corner of the 
        tree viewer to zoom in and focus on a specific area of the tree.
    </p>
    <p> 
        You can also click on the gear icon in the viewer to toggle the tree's appearance and on the 
        camera icon to take a screenshot of the tree, and the full screen icon to enter full screen mode.
    </p>
`
TAXONIUM_SIDEBAR.appendChild(help_node);