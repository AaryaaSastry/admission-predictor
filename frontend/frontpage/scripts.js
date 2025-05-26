// Automatic Slideshow
let slideIndex = 0;
showSlides();

function showSlides() {
    let slides = document.getElementsByClassName("slide");
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > slides.length) { slideIndex = 1 }
    slides[slideIndex - 1].style.display = "block";
    setTimeout(showSlides, 3000); // Change image every 3 seconds
}

// Login Modal controls
function openLogin() {
    document.getElementById("loginForm").style.display = "flex";
}

function closeLogin() {
    document.getElementById("loginForm").style.display = "none";
}

function openSignup() {
    document.getElementById("signupForm").style.display = "flex";
}

function closeSignup() {
    document.getElementById("signupForm").style.display = "none";
}

// Login validation and redirect
function validateLogin() {
    const username = document.getElementById("username").value;
    const password = document.getElementById("password").value;

    // Replace with actual login validation
    if (username === "user" && password === "pass") {
        window.location.href = "main.html";
        return false;
    } else {
        alert("Incorrect username or password");
        return false;
    }
}

// Signup function (dummy function for now)
function registerUser() {
    const newUsername = document.getElementById("newUsername").value;
    const newPassword = document.getElementById("newPassword").value;

    // Add logic to save user information here
    alert("Account created successfully! Please login.");
    closeSignup();
    return false;
}
