document.getElementById('registerForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent the default form submission behavior
    
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Check if the submit button clicked was the Login button
    if (event.submitter && event.submitter.id === 'loginButton') {
        // Redirect to the login page
        window.location.href = '/login';
        return; // Exit the function to prevent further execution
    }

    // Send a POST request to the /register endpoint
    fetch('/register', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ username: username, password: password })
    })
    .then(response => response.json())
    .then(data => {
        // Check if registration was successful or not
        if (data.message === 'User registered successfully!') {
            // Display success message with delay
            const successMessage = document.getElementById('successMessage');
            successMessage.textContent = 'Registration successful!';
            setTimeout(() => {
                // Redirect to the login page after 2 seconds
                window.location.href = '/login';
            }, 3000);
        } else {
            // Display the error message to the user
            const messageElement = document.getElementById('message');
            messageElement.textContent = data.message;
            messageElement.style.color = 'red';
        }
    })
    .catch(error => {
        console.error('Error during registration:', error);
    });
});