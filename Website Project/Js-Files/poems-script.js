let mybutton = document.getElementById("scrollToTopBtn");

// Show the button when scrolling 20px down from the top
window.onscroll = function() {
    if (document.documentElement.scrollTop > 20 || document.body.scrollTop > 20) {
        mybutton.style.display = "block"; // Show the button
    } else {
        mybutton.style.display = "none"; // Hide the button
    }
};

// Scroll to top when the button is clicked
mybutton.onclick = function() {
    window.scrollTo({
        top: 0,
        left: 0,
        behavior: "smooth"
    });
    return false; // Prevent default anchor behavior
};

/*To prevent the default "jump to top" behavior, we use JavaScript with return false; 
in the onclick handler. This stops the browser from following the link (href="#"), and instead, 
it triggers the smooth scrolling action.*/