
let header=document.getElementById('header')

const headerColorChange  = () => {
  document.body.scrollTop > 50 ||
  document.documentElement.scrollTop > 50 
    ? header.style.background= "#000"
    : header.style.background= "transparent"
};
// When the pages is loaded
window.addEventListener("DOMContentLoaded", () => {
  headerColorChange();
});
// When the user scrolls the page
window.addEventListener("scroll", () => {
  headerColorChange();
});

 // when user resizes the page to less than 532px
 window.addEventListener("resize", () => {
  headerColorChange();
});


var today = new Date().toISOString().split('T')[0];
document.getElementById("demo").setAttribute('min', today);
