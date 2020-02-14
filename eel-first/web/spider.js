async function printResults(n) {
  console.log("Results: ".concat(n));
}

async function getNumOfLinks() {
  document.getElementById("progressReporter").innerHTML = "Calculating number of links..."

  var enteredURL = document.getElementById("urlInput").value;

  let numberOfLinks = await eel.getNumLinks(enteredURL)();
  window.alert(numberOfLinks);

  document.getElementById("progressReporter").innerHTML = "";

}
