const favicon = document.getElementById("favicon");
const mode = window.matchMedia("(prefers-color-scheme: dark)");


//Set on Entry
if (window.matchMedia("(prefers-color-scheme: dark)")){
  favicon.setAttribute("href", "static/images/logoDark.svg");
}
else {
  favicon.setAttribute("href", "static/images/logoLight.svg");
}


//Set on Change
mode.addEventListener("change", (event) => {
  if (event.matches){
    favicon.setAttribute("href", "static/images/logoDark.svg");
  }
  else {
    favicon.setAttribute("href", "static/images/logoLight.svg");
  }
                     
});
