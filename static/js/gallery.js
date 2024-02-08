// Get the modal
var modal = document.getElementById("myModal");

let openImageModal = (img) => {
  var modalImg = document.getElementById("img01");

  modal.style.display = "block";
  modalImg.src = img.src;
  var modalImg = document.getElementById("img01");
};

// // Get the <span> element that closes the modal
// var span = document.getElementsByClassName("close")[0];

// // When the user clicks on <span> (x), close the modal
// span.onclick = function () {
//   modal.style.display = "none";
// };

function hideModal() {
  modal.style.display = "none";
}

document.addEventListener("DOMContentLoaded", function () {
  var modal = document.getElementById("myModal");
  var modalImg = document.getElementById("img01");

  modal.addEventListener("click", function (event) {
    // Check if the click target is the modal itself (not the image)
    if (event.target === modal) {
      hideModal();
    }
  });

  // Prevent the modal from closing when the image is clicked
  modalImg.addEventListener("click", function (event) {
    event.stopPropagation();
  });
});
