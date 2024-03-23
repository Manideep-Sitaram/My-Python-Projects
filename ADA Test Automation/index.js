document.addEventListener("DOMContentLoaded", function() {
    let inputBox = document.getElementById("UrlInput");
    let button = document.getElementById("submit");

    button.addEventListener('click', (e) => {
        const urlObject = {
            url: inputBox.value
        };

        document.getElementById("loading-message").style.display = "block";

        fetch("http://127.0.0.1:8000/send-url/", {
            method: "POST",
            headers: {
                "Content-type": "application/json"
            },
            body: JSON.stringify(urlObject)
        })
        .then(res => res.json())
        .then(response => {
            document.getElementById("loading-message").style.display = "none";
            // Get the container element
            const testCaseContainer = document.getElementById('testCaseContainer');

            testCaseContainer.innerHTML = response.content       
            
        })
        .catch(error => console.error('Error:', error));
    });
});
