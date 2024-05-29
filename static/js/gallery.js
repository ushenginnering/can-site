// Get the modal
let modal = document.getElementById("myModal");
let isModalOpen = false;

let openImageModal = (img) => {
  let modalImg = document.getElementById("img01");

  modal.style.display = "flex";
  modalImg.src = img.src;
  isModalOpen = true;
};

function hideModal() {
  modal.style.display = "none";
  isModalOpen = false;
}

document.addEventListener("DOMContentLoaded", function () {
  let modal = document.getElementById("myModal");
  let modalImg = document.getElementById("img01");

  modal.addEventListener("click", function (event) {
    // Check if the click target is the modal itself (not the image)
    if (event.target === modal) {
      hideModal();
    }
  });

  document.addEventListener('keydown', (event)=>{
    if (event.key == 'Escape' && isModalOpen) {
      hideModal();
    }
    console.log(event);
  })

  // Prevent the modal from closing when the image is clicked
  modalImg.addEventListener("click", function (event) {
    event.stopPropagation();
  });
});
