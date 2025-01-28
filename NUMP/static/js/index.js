
document.addEventListener( "DOMContentLoaded", function() {
    const editButton = document.getElementById("editButton");
    const editFormContainer = document.getElementById("editFormContainer");
    const closeButton = document.getElementById("closeButton");

    // Show the form when "Edit" button is clicked
    editButton.addEventListener("click", function () {
        editFormContainer.style.display = "flex";
        console.log("Js loaded")
    });

    // Hide the form when the close button is clicked
    closeButton.addEventListener("click", function () {
        editFormContainer.style.display = "none";
    });

    // Optionally, hide the form when clicking outside the form content
    editFormContainer.addEventListener("click", function (event) {
        if (event.target === editFormContainer) {
            editFormContainer.style.display = "none";
        }
    });

   

    console.log("Js loaded")
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

    