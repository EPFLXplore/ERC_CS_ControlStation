var test = JSON.parse(document.getElementById('state').textContent);

if (test == "Idle"){
    var elem = document.getElementById('idle-state');
    elem.style.opacity = 1;
}else if(test == "Navigation"){
    var elem = document.getElementById('navigation-state');
    elem.style.opacity = 1;
}else if(test == "Maintenance"){
    var elem = document.getElementById('hd-state');
    console.log(0)
    elem.style.opacity = 1;
}else if(test == "Waiting"){
    var elem = document.getElementById('waiting-state');
    elem.style.opacity = 1;
}else if(test == "Manual"){
    var elem = document.getElementById('manual-state');
    elem.style.opacity = 1;
}
else if(test == "Science"){
    var elem = document.getElementById('science-state');
    elem.style.opacity = 1;
}


// wait button
document.querySelector("#wait-button").addEventListener("click", event => {
    event.preventDefault();


    var elem5 = document.getElementById('waiting-state');

    elem5.style.opacity = 1;


    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let request = new Request("wait/", {method: 'POST',
                                        body: '',
                                        headers: {"X-CSRFToken": csrfTokenValue}})
    fetch(request)
        .then(response => response.json())
        .then(result => {})
});

// abort button
document.querySelector("#abort-button").addEventListener("click", event => {
    event.preventDefault();

    var elem1 = document.getElementById('navigation-state');
    var elem2 = document.getElementById('idle-state');
    var elem3 = document.getElementById('hd-state');
    var elem4 = document.getElementById('manual-state');
    var elem5 = document.getElementById('waiting-state');
    var elem6 = document.getElementById('science-state');

    elem6.style.opacity = 0;
    elem1.style.opacity = 0.2;
    elem2.style.opacity = 1;
    elem3.style.opacity = 0.2;
    elem4.style.opacity = 0.2;
    elem5.style.opacity = 0.2;
    


    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let request = new Request("abort/", {method: 'POST',
                                        body: '',
                                        headers: {"X-CSRFToken": csrfTokenValue}})
    fetch(request)
        .then(response => response.json())
        .then(result => {})
});

// resume button
document.querySelector("#resume-button").addEventListener("click", event => {
    event.preventDefault();

 
    var elem5 = document.getElementById('waiting-state');

 
    elem5.style.opacity = 0.2;


    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let request = new Request("resume/", {method: 'POST',
                                        body: '',
                                        headers: {"X-CSRFToken": csrfTokenValue}})
    fetch(request)
        .then(response => response.json())
        .then(result => {})
});



