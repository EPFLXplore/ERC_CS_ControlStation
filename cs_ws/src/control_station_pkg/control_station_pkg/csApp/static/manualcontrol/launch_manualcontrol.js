/* code when launching MANUAL */					
document.querySelector("#launch-button").addEventListener("click", event => {
    event.preventDefault();

    // dim the states on top of the GUI and highlight Manual
    var elem1 = document.getElementById('navigation-state');
    var elem2 = document.getElementById('idle-state');
    var elem3 = document.getElementById('hd-state');
    var elem4 = document.getElementById('manual-state');
    var elem5 = document.getElementById('waiting-state');

    elem1.style.opacity = 0.2;
    elem2.style.opacity = 0.2;
    elem3.style.opacity = 0.2;
    elem4.style.opacity = 1;
    elem5.style.opacity = 0.2;

    // request back-end to launch manual
    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let request = new Request("launch/", {method: 'POST',
                                        body: '',
                                        headers: {"X-CSRFToken": csrfTokenValue}})
    fetch(request)
        .then(response => response.json())
        .then(result => {})
})