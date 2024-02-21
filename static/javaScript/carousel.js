
const roles = [
    { name: "John & Emily", role: "Padrinos de anillos" },
  { name: "Michael & Sophia", role: "Padrinos de arras" },
  { name: "David & Isabella", role: "Padrinos de biblia" }


]


// Function to create carousel items
function createCarouselItems() {
    const carousel = document.getElementById("carousel");
    carousel.innerHTML = "";
  
    roles.forEach(role => {
      const card = document.createElement("div");
      card.classList.add("card");
      card.innerHTML = `
        <h2 class="card-title">${role.name}</h2>
        <h3 class="card-subtitle">${role.role}</h3>
      `;
      carousel.appendChild(card);
    });
  }
  
  // Function to handle carousel navigation
  function navigateCarousel(direction) {
    const carousel = document.getElementById("carousel");
    const scrollAmount = direction === "next" ? carousel.scrollWidth : -carousel.scrollWidth;
    carousel.scrollBy({
      left: scrollAmount,
      behavior: "smooth"
    });
  }
  
  // Event listeners for prev and next buttons
  document.getElementById("prevBtn").addEventListener("click", () => navigateCarousel("prev"));
  document.getElementById("nextBtn").addEventListener("click", () => navigateCarousel("next"));
  
  // Initial setup
  createCarouselItems();