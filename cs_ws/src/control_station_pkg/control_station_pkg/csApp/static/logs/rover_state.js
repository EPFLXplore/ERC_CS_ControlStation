var test = JSON.parse(document.getElementById('state').textContent);

if (test == "Idle") {
    var elem = document.getElementById('idle-state');
    elem.style.opacity = 1;
} else if (test == "Navigation") {
    var elem = document.getElementById('navigation-state');
    elem.style.opacity = 1;
} else if (test == "Maintenance") {
    var elem = document.getElementById('hd-state');
    console.log(0)
    elem.style.opacity = 1;
} else if (test == "Waiting") {
    var elem = document.getElementById('waiting-state');
    elem.style.opacity = 1;
} else if (test == "Manual") {
    var elem = document.getElementById('manual-state');
    elem.style.opacity = 1;
}
else if (test == "Science") {
    var elem = document.getElementById('science-state');
    elem.style.opacity = 1;
}