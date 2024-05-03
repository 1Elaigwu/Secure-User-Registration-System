document.getElementById('logoutBtn').addEventListener('click', function(event) {
    event.preventDefault();
    fetch('/logout', { method: 'POST' })  // Send a POST request to logout
        .then(response => {
            if (response.ok) {
                // Redirect to the login page after successful logout
                window.location.href = '/login';
            } else {
                console.error('Failed to logout');
            }
        })
        .catch(error => {
            console.error('Error during logout:', error);
        });
});