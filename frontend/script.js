document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('videoForm');  // Form element
    const urlInput = document.getElementById('urlInput');  // Input field for video URL
    const downloadButton = document.getElementById('downloadButton');  // Download button
    const messageBox = document.getElementById('message');  // Message box for alerts

    // Event listener for the form submission
    form.addEventListener('submit', function (event) {
        event.preventDefault();  // Prevent default form submission

        const url = urlInput.value.trim();  // Get the URL from the input field

        // Validate the URL input
        if (!url) {
            showMessage('Please enter a valid video URL.', 'error');
            return;
        }

        // Show loading message and disable the button
        downloadButton.disabled = true;
        downloadButton.innerText = 'Downloading...';

        // Send a POST request to the Flask server
        fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
            body: new URLSearchParams({ url: url })  // Prepare the body with the URL
        })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok: ' + response.statusText);
            }
            return response.blob();  // Get the response as a Blob
        })
        .then(blob => {
            const blobUrl = window.URL.createObjectURL(blob);  // Create a local URL for the blob
            const a = document.createElement('a');  // Create an anchor element
            a.href = blobUrl;
            a.download = 'video.mp4';  // Set the desired file name
            document.body.appendChild(a);  // Append to the body
            a.click();  // Programmatically click the anchor to trigger download
            a.remove();  // Remove the anchor from the document
            showMessage('Download completed!', 'success');  // Show success message
            downloadButton.innerText = 'Download Video';  // Reset button text
            downloadButton.disabled = false;  // Enable button again
        })
        .catch(error => {
            console.error('Error downloading video:', error);
            showMessage('Error downloading video. Please try again later.', 'error');  // Show error message
            downloadButton.innerText = 'Download Video';  // Reset button text
            downloadButton.disabled = false;  // Enable button again
        });
    });

    // Function to display messages
    function showMessage(message, type) {
        messageBox.textContent = message;  // Set message text
        messageBox.className = type;  // Set class for styling (e.g., success or error)
        setTimeout(() => {
            messageBox.textContent = '';  // Clear message after a delay
            messageBox.className = '';
        }, 3000);  // Clear message after 3 seconds
    }
});
