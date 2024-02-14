document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the "Clear All Notifications" button
    var clearButton = document.querySelector('.clear-notifications-btn');
    clearButton.addEventListener('click', function () {
        // Assuming you have a route in your Flask app to handle clearing notifications
        var clearNotificationsURL = '/notifications-center';

        // Make an asynchronous request to clear notifications
        fetch(clearNotificationsURL, {
            method: 'POST',
        })
        .then(response => response.json())
        .then(data => {
            // Update the UI or perform any additional actions
            console.log('Notifications cleared:', data.message);
            // For example, you could reload the page or update the notifications list
            location.reload();
        })
        .catch(error => {
            console.error('Error clearing notifications:', error);
        });
    });
});
