document.addEventListener("DOMContentLoaded", function () {
    showTextbox();
});

function showTextbox() {
    var textBox = document.getElementById("textbox");
    textBox.style.display = "block";
    setTimeout(function () {
        textBox.classList.add("active");
    }, 10);
}

document.addEventListener("click", function (event) {
    var closeButton = document.querySelector(".close");

    if (closeButton && closeButton.contains(event.target)) {
        hideTextbox();
    }
});

function hideTextbox() {
    var textBox = document.getElementById("textbox");
    textBox.classList.remove("active");
    textBox.style.display = "none";
    window.location.href = "/"; 
}
