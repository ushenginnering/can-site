let currentIndex = 1;
const items = document.querySelectorAll('.gallery-item');
const container = document.getElementById('gallery-container');

function scrollGallery(direction) {
  currentIndex += direction;
  currentIndex = Math.max(0, Math.min(currentIndex, items.length - 1));
  const newPosition = currentIndex * items[0].offsetWidth;

  container.scroll({
    left: newPosition,
    behavior: 'smooth'
  });
}


function goToIndex(index) {
  currentIndex = index;
  currentIndex = Math.max(0, Math.min(currentIndex, items.length - 1));

  const newPosition = currentIndex * items[0].offsetWidth;
  container.scroll({
    left: newPosition,
    behavior: 'smooth'
  });
}