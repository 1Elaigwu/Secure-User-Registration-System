document.getElementById('loginForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission behavior
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Check if the submit button clicked was the Register button
    if (event.submitter && event.submitter.id === 'registerButton') {
        // Redirect to the register page
        window.location.href = '/register';
        return; // Exit the function to prevent further execution
    }

    // Send a POST request to the /login endpoint
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Display success message
            const successMessage = document.getElementById('successMessage');
            successMessage.textContent = 'Login successful!';
            // Show success message for 3 seconds
            setTimeout(() => {
                successMessage.textContent = ''; // Clear the success message
                // Redirect to the user page after 3 seconds
                window.location.href = '/user';
            }, 3000);
        } else {
            // Display the appropriate error message to the user
            const messageElement = document.getElementById('message');
            messageElement.textContent = data.message;
            messageElement.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error during login:', error);
    });
});