document.addEventListener('DOMContentLoaded', function() {
    // Fetch user data asynchronously
    fetchUserData();

    // Fetch service request data asynchronously
    fetchServiceRequestData();

    // Fetch equipment listing data asynchronously
    fetchEquipmentListingData();
});

function fetchUserData() {
    fetch('/user-profile')  // Update the route based on your API design
        .then(response => response.json())
        .then(data => {
            // Render user data dynamically
            renderUserData(data);
        })
        .catch(error => {
            console.error('Error fetching user data:', error);
        });
}

function fetchServiceRequestData() {
    fetch('/service_request_form')  // Update the route based on your API design
        .then(response => response.json())
        .then(data => {
            // Render service request data dynamically
            renderServiceRequestData(data);
        })
        .catch(error => {
            console.error('Error fetching service request data:', error);
        });
}

function fetchEquipmentListingData() {
    fetch('/equipment_listings_marketplace')  // Update the route based on your API design
        .then(response => response.json())
        .then(data => {
            // Render equipment listing data dynamically
            renderEquipmentListingData(data);
        })
        .catch(error => {
            console.error('Error fetching equipment listing data:', error);
        });
}

function renderUserData(users) {
    const userList = document.getElementById('userList');
    userList.innerHTML = '';

    users.forEach(user => {
        const listItem = document.createElement('li');
        listItem.textContent = user.username;
        userList.appendChild(listItem);
    });
}

function renderServiceRequestData(requests) {
    const requestList = document.getElementById('requestList');
    requestList.innerHTML = '';

    requests.forEach(request => {
        const listItem = document.createElement('li');
        listItem.textContent = request.service_type;
        requestList.appendChild(listItem);
    });
}

function renderEquipmentListingData(listings) {
    const listingList = document.getElementById('listingList');
    listingList.innerHTML = '';

    listings.forEach(listing => {
        const listItem = document.createElement('li');
        listItem.textContent = listing.equipment_name;
        listingList.appendChild(listItem);
    });
}
