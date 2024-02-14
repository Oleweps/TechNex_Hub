// static/js/equipment_inquiry_script.js
document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the "Inquire Equipment" button
    var inquireButtons = document.querySelectorAll('.inquire-equipment-btn');
    inquireButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Retrieve the equipment ID from the button's data attribute
            var equipmentId = button.getAttribute('data-equipment-id');

            // Use Fetch API or XMLHttpRequest for asynchronous equipment inquiry
            fetch('/inquire-equipment', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/x-www-form-urlencoded',
                },
                body: new URLSearchParams({
                    'equipment_id': equipmentId,
                }),
            })
            .then(response => response.json())
            .then(data => {
                // You can handle the response data, e.g., display a success message or update UI
                console.log(data);
            });
        });
    });
});
