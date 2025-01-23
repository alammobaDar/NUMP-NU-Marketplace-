const editButton = document.getElementById("editButton");
const editFormContainer = document.getElementById("editFormContainer");
const closeButton = document.getElementById("closeButton");

// Show the form when "Edit" button is clicked
editButton.addEventListener("click", function () {
    editFormContainer.style.display = "flex";
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