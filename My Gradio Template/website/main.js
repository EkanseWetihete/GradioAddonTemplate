function observeTestingButtonClick() {
  const observer = new MutationObserver(function(mutationsList) {
    for (let mutation of mutationsList) { 
      if (mutation.type === 'childList') { // Checks for changes in HTML
        const testingButton = document.getElementById("testing"); // Finds a testing button
        if (testingButton) {
          testingButton.addEventListener("click", function() {
            document.getElementById("body_container").innerHTML = ''; // Removes div elements of body_container from body.html
          });
        }
      }
    }
  });

  observer.observe(document.body, { childList: true, subtree: true }); // Observes added/removed elements of HTML Body
}