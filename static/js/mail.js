let x = document.getElementById('yo');

function yo() {
    alert("high");
    let xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            alert(this.responseText);
        }
    };
    xhttp.open("GET", "mail?name=Anubhav&message=Hello", true);
    xhttp.send();
}
x.addEventListener("click", yo);