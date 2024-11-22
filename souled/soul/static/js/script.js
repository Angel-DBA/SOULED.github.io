//login form
var wrapper = document.querySelector(".wrapper");
var signuplink = document.querySelector(".signup-link");
var loginlink = document.querySelector(".login-link");
signuplink.onclick = () => {
  wrapper.classList.add("active");
};
loginlink.onclick = () => {
  wrapper.classList.remove("active");
};

document.addEventListener("DOMContentLoaded", () => {
  // Dropdown toggle
  document.getElementById("cart-dropdown")?.classList.toggle("show");

  document.addEventListener("click", (e) => {
    const dropdown = document.getElementById("cart-dropdown");
    if (dropdown && !dropdown.contains(e.target)) {
      dropdown.classList.remove("show");
    }
  });

  // Signup and login links
  const wrapper = document.querySelector(".wrapper");
  const signuplink = document.querySelector(".signup-link");
  const loginlink = document.querySelector(".login-link");

  if (signuplink && loginlink) {
    signuplink.onclick = () => wrapper?.classList.add("active");
    loginlink.onclick = () => wrapper?.classList.remove("active");
  }

  // Login and register buttons
  const loginButton = document.getElementById("login-button");
  const registerButton = document.getElementById("register-button");
  const toggleDiv = document.getElementById("toggle-div");

  if (loginButton && registerButton && toggleDiv) {
    loginButton.addEventListener("click", () => {
      toggleDiv.style.display = "block";
    });
    registerButton.addEventListener("click", () => {
      toggleDiv.style.display = "block";
    });
  }

  // Search icon functionality
  const searchIcon = document.getElementById("searchIcon");
  const searchInput = document.getElementById("searchInput");

  if (searchIcon && searchInput) {
    searchIcon.addEventListener("click", () => {
      searchInput.classList.toggle("show");
    });
  }
});

document
  .getElementById("message-form")
  .addEventListener("submit", function (event) {
    event.preventDefault(); // Prevent the default form submission

    var formData = new FormData(this); // Collect the form data

    fetch("{% url 'submit_message' %}", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.success) {
          // Show success message on success
          document.getElementById("success-message").style.display = "block";
          // Clear the form fields after success
          document.getElementById("message-form").reset();
        } else {
          alert("There was an error. Please try again.");
        }
      })
      .catch((error) => {
        alert("Error: " + error);
      });
  });
