document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('editProfileBtn').addEventListener('click', function () {
        document.getElementById('editProfileForm').style.display = 'block';
        document.querySelector('.profile-details').style.display = 'none';
        document.getElementById('editProfileBtn').style.display = 'none';
    });
});
