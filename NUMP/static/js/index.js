const editButton = document.getElementById("editButton");
const formContainer = document.getElementById("formContainer");
const closeButton = document.getElementById("closeButton");
const buyButton = document.getElementById("buyButton");
const cartButton = document.getElementById("cartButton");



document.addEventListener("DOMContentLoaded", function(){
        // Show the form when "Edit" button is clicked
    editButton.addEventListener("click", function () {
        formContainer.style.display = "flex";
        console.log("Js loaded")
    });

        // Hide the form when the close button is clicked
    closeButton.addEventListener("click", function () {
        formContainer.style.display = "none";
    });

        // Optionally, hide the form when clicking outside the form content
    formContainer.addEventListener("click", function (event) {
        if (event.target === formContainer) {
            formContainer.style.display = "none";
        }
    });
});

document.addEventListener("DOMContentLoaded", function() {

    buyButton.addEventListener("click", function () {
        formContainer.style.display = "flex";
    });

    cartButton.addEventListener("click", function () {
        formContainer.style.display = "flex";
    });

        // Hide the form when the close button is clicked
    closeButton.addEventListener("click", function () {
        formContainer.style.display = "none";
    });

        // Optionally, hide the form when clicking outside the form content
    formContainer.addEventListener("click", function (event) {
        if (event.target === formContainer) {
            formContainer.style.display = "none";
        };
    });
});




const fileInput = document.getElementById("id_image");
const previewImage = document.getElementById("previewImage");


fileInput.addEventListener("change", (event) => {
  const file = event.target.files[0]; // Get the selected file
  if (file) {
    const reader = new FileReader(); // Create a FileReader to read the file

    // When the file is loaded, set the preview image source
    reader.onload = (e) => {
      previewImage.style.display = "block"; // Make the image visible
      previewImage.src = e.target.result;  // Set the image source to the file data
    };

    reader.readAsDataURL(file); // Read the file as a Data URL (base64)
  } else {
    previewImage.style.display = "none"; // Hide the image if no file is selected
  }
});

