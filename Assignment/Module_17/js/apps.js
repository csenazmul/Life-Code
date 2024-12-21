// Get references to DOM elements
const memoryCostElement = document.getElementById("memory-cost");
const storageCostElement = document.getElementById("storage-cost");
const deliveryCostElement = document.getElementById("delivery-cost");
const totalPriceElement = document.getElementById("total-price");
const userPaymentElement = document.getElementById("user-payment");

const promoInputField = document.getElementById("input-field");
const applyPromoButton = document.getElementById("apply-btn");

// Initial values
const basePrice = 1299;
let extraMemoryCost = 0;
let extraStorageCost = 0;
let deliveryCost = 0;

// Utility function to calculate and update the total price
function updateTotalPrice() {
  const totalPrice = basePrice + extraMemoryCost + extraStorageCost + deliveryCost;
  totalPriceElement.textContent = totalPrice;
  userPaymentElement.textContent = totalPrice;
}

// Memory option event listeners
document.getElementById("8gb-memory").addEventListener("click", () => {
  extraMemoryCost = 0;
  memoryCostElement.textContent = extraMemoryCost;
  updateTotalPrice();
});

document.getElementById("16gb-memory").addEventListener("click", () => {
  extraMemoryCost = 180;
  memoryCostElement.textContent = extraMemoryCost;
  updateTotalPrice();
});

// Storage option event listeners
document.getElementById("256gb-storage").addEventListener("click", () => {
  extraStorageCost = 0;
  storageCostElement.textContent = extraStorageCost;
  updateTotalPrice();
});

document.getElementById("512gb-storage").addEventListener("click", () => {
  extraStorageCost = 100;
  storageCostElement.textContent = extraStorageCost;
  updateTotalPrice();
});

document.getElementById("1tb-storage").addEventListener("click", () => {
  extraStorageCost = 180;
  storageCostElement.textContent = extraStorageCost;
  updateTotalPrice();
});

// Delivery option event listeners
document.getElementById("late-delivery").addEventListener("click", () => {
  deliveryCost = 0;
  deliveryCostElement.textContent = deliveryCost;
  updateTotalPrice();
});

document.getElementById("early-delivery").addEventListener("click", () => {
  deliveryCost = 20;
  deliveryCostElement.textContent = deliveryCost;
  updateTotalPrice();
});

// Promo code application
applyPromoButton.addEventListener("click", () => {
  const enteredPromoCode = promoInputField.value.trim();

  if (enteredPromoCode === "OSTAD10") {
    const totalPrice = parseFloat(totalPriceElement.textContent);
    const discountedPrice = totalPrice * 0.9;

    totalPriceElement.textContent = discountedPrice.toFixed(2);
    userPaymentElement.textContent = discountedPrice.toFixed(2);

    alert("Promo code applied! You've received a 10% discount.");
  } else {
    alert("Invalid promo code. Please try again.");
  }
});


// function promocode() {
//   const promoInput = document.getElementById("input-field").value.trim(); // Get promo code input
//   const totalPriceElement = document.getElementById("total-price"); // Total price element
//   const userPaymentElement = document.getElementById("user-payment"); // User payment element
//   const totalCost = updateTotal(); // Calculate total cost

//   // Check promo code validity
//   if (promoInput === "OSTAD10") {
//     const discountedPrice = totalCost * 0.9; // 10% discount
//     totalPriceElement.textContent = discountedPrice.toFixed(2); // Update total price in UI
//     userPaymentElement.textContent = discountedPrice.toFixed(2); // Update user payment in UI
//     alert("Promo code applied! You've received a 10% discount.");
//   } else {
//     alert("Invalid promo code. Please try again.");
//   }

//   // Clear promo input field
//   document.getElementById("input-field").value = "";
// }

// Countdown for Remaining Days
// let daysLeft = 6; // Starting days
// const daysLeftElement = document.getElementById("days-left");

// // Update days left every day (this is simulated for a live countdown)
// const updateDaysLeft = setInterval(() => {
//   if (daysLeft > 0) {
//     daysLeft--;
//     daysLeftElement.textContent = daysLeft;
//   } else {
//     clearInterval(updateDaysLeft);
//     alert("The promo code is no longer valid.");
//     document.getElementById("fixed-header").style.display = "none"; // Hide header
//   }
// }, 24 * 60 * 60 * 1000); // Update every 24 hours (simulated timing here for demonstration)



// // Set promo expiration date (6 days from now)
// const promoEndDate = new Date();
// promoEndDate.setDate(promoEndDate.getDate() + 1);

// // Update the countdown timer every second
// const countdownTimerElement = document.getElementById("countdown-timer");

// const updateCountdown = setInterval(() => {
//   const now = new Date();
//   const timeLeft = promoEndDate - now;

//   if (timeLeft > 0) {
//     // Calculate remaining days, hours, minutes, and seconds
//     const days = Math.floor(timeLeft / (1000 * 60 * 60 * 24));
//     const hours = Math.floor((timeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
//     const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
//     const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

//     // Display the countdown
//     countdownTimerElement.textContent = `${days}d ${hours.toString().padStart(2, '0')}:${minutes
//       .toString()
//       .padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
//   } else {
//     // Promo expired
//     clearInterval(updateCountdown);
//     countdownTimerElement.textContent = "Expired";
//     document.getElementById("fixed-header").style.backgroundColor = "#e74c3c";
//     alert("The promo code has expired.");
//   }
// }, 1000);


// Set promo expiration date (1 hours from now)
const promoEndDate = new Date();
promoEndDate.setTime(promoEndDate.getTime() + 1 * 60 * 60 * 1000); // Add 2 hours in milliseconds

// Update the countdown timer every second
const countdownTimerElement = document.getElementById("countdown-timer");

const updateCountdown = setInterval(() => {
  const now = new Date();
  const timeLeft = promoEndDate - now;

  if (timeLeft > 0) {
    // Calculate remaining hours, minutes, and seconds
    const hours = Math.floor(timeLeft / (1000 * 60 * 60));
    const minutes = Math.floor((timeLeft % (1000 * 60 * 60)) / (1000 * 60));
    const seconds = Math.floor((timeLeft % (1000 * 60)) / 1000);

    // Display the countdown
    countdownTimerElement.textContent = `${hours.toString().padStart(1, '0')}:${minutes
      .toString()
      .padStart(1, '0')}:${seconds.toString().padStart(1, '0')}`;
  } else {
    // Promo expired
    clearInterval(updateCountdown);
    countdownTimerElement.textContent = "Expired";
    document.getElementById("fixed-header").style.backgroundColor = "#e74c3c";
    alert("The promo code has expired.");
  }
}, 1000);


