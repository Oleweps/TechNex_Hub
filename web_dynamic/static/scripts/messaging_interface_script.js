// static/js/messaging_interface_script.js
document.addEventListener('DOMContentLoaded', function () {
    // Add event listener to the "Reply" buttons
    var replyButtons = document.querySelectorAll('.reply-btn');
    replyButtons.forEach(function (button) {
        button.addEventListener('click', function () {
            // Retrieve the sender ID from the button's data attribute
            var senderId = button.getAttribute('data-sender-id');

            // You can now perform some action with the senderId, for example,
            // pre-fill the recipient field in the form
            document.getElementById('receiver_id').value = senderId;
        });
    });
});
