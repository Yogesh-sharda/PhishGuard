// Simple interactivity: alert on button click

document.addEventListener("DOMContentLoaded", function() {
  document.getElementById("cta-btn").addEventListener("click", function() {
    alert("Thanks for your interest! Scroll down to sign up.");
  });

  document.getElementById("signup-btn").addEventListener("click", function() {
    alert("Signup feature coming soon!");
  });
});