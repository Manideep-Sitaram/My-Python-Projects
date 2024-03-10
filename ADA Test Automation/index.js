let inputBox = document.getElementById("UrlInput");
let button = document.getElementById("submit");

button.addEventListener('click', (e) => {

    const urlObject = {
        url: inputBox.value
    }

    fetch("http://127.0.0.1:8000/send-url/",{

        method: "POST",
        headers: {
            "Content-type": "application/json"
        },
        body: JSON.stringify(urlObject)
    })
    .then( res => res.json())
    .then(json => console.log(json))

    

})