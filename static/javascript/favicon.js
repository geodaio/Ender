const favicon = document.getElementById("favicon");
const mode = window.matchMedia("(prefers-color-scheme: dark)");


//Set on Entry
if (window.matchMedia("(prefers-color-scheme: dark)")){
  favicon.setAttribute("href", "{{ url_for('static', filename='images/logoDark.svg') }}");
}
else {
  favicon.setAttribute("href", "{{ url_for('static', filename='images/logoLight.svg') }}");
}


//Set on Change
mdoe.addEventListener("change", (event) => {
  if (event.matches){
    favicon.setAttribute("href", "{{ url_for('static', filename='images/logoDark.svg') }}");
  }
  else {
    favicon.setAttribute("href", "{{ url_for('static', filename='images/logoLight.svg') }}");
  }
                     
});
