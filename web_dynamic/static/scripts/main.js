// main.js

function searchEquipment() {
    const searchInput = document.getElementById('equipmentSearch').value.trim();

    if (searchInput) {
        // Use Fetch API or XMLHttpRequest for asynchronous search request
        fetch(`/search-equipment?query=${searchInput}`, {
            method: 'GET'
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response, e.g., display search results, redirect, etc.
            console.log(data);
        })
        .catch(error => {
            console.error('Error:', error);
        });
    } else {
        alert('Please enter a search query');
    }
}
