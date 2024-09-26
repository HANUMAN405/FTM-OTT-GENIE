document.getElementById('downloadForm').addEventListener('submit', async function (e) {
    e.preventDefault();
    
    const videoLink = document.getElementById('videoLink').value;
    const statusMessage = document.getElementById('statusMessage');

    if (videoLink.trim() === "") {
        statusMessage.textContent = "Please enter a valid video link.";
        return;
    }

    statusMessage.textContent = "Processing...";

    try {
        const response = await fetch('/download', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ link: videoLink }),
        });

        const result = await response.json();
        if (response.ok) {
            statusMessage.textContent = result.message;
        } else {
            statusMessage.textContent = result.message;
        }
    } catch (error) {
        statusMessage.textContent = "Error occurred: " + error.message;
    }
});
