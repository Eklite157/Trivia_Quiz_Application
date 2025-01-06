/*For the dropdowns*/
/*we get element by id... but id=volleyball essentially refers to the item-container class*/

document.addEventListener("DOMContentLoaded", function() {

document.getElementById("volleyball").addEventListener("click", function() {
    const dropdown = document.getElementById("volleyball-text");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
});

document.getElementById("chinese-poetry").addEventListener("click", function() {
    const dropdown = document.getElementById("chinese-poetry-text");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
});

document.getElementById("violin").addEventListener("click", function() {
    const dropdown = document.getElementById("violin-text");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
});

document.getElementById("ib").addEventListener("click", function() {
    const dropdown = document.getElementById("ib-text");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
});

document.getElementById("cs").addEventListener("click", function() {
    const dropdown = document.getElementById("cs-text");
    dropdown.style.display = dropdown.style.display === "block" ? "none" : "block";
});
})

