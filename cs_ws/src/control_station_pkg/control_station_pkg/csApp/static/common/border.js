
neon   = getComputedStyle(document.documentElement).getPropertyValue('--clr-neon');
yellow = getComputedStyle(document.documentElement).getPropertyValue('--clr-y');

/*=========================| IDLE |==============================================*/
function lit_idle_state() {
    var idle_state = document.getElementById('idle-state');
    idle_state.style.background = yellow;
    idle_state.style.color = "black";
    idle_state.style.textShadow = "none";
    idle_state.style.boxShadow  = "0 0 2em 0.3em"+yellow;
}
function unlit_idle_state() {
    var idle_state = document.getElementById('idle-state');
    idle_state.style.background = "transparent";
    idle_state.style.textShadow = "0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.25em currentColor";
    idle_state.style.boxShadow  = "inset 0 0 0.5em 0 "+yellow+", 0 0 0.5em 0 "+yellow;
}

/*=======================| NAVIGATION |===========================================*/
function lit_navigation_state() {
    var nav_state = document.getElementById('navigation-state');
    nav_state.style.opacity = 1;

}
function unlit_navigation_state() {
    var nav_state = document.getElementById('navigation-state');
    nav_state.style.opacity = 0.5;

}

/*=======================| HANDLING DEVICE |===========================================*/
function lit_hd_state() {
    var hd_state = document.getElementById('hd-state');
    hd_state.style.background = neon;
    hd_state.style.textShadow = "none";
    hd_state.style.boxShadow  = "0 0 2em 0.3em"+neon;
}
function unlit_hd_state() {
    var hd_state = document.getElementById('hd-state');
    hd_state.style.background = "transparent";
    hd_state.style.textShadow = "0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.25em currentColor";
    hd_state.style.boxShadow  = "inset 0 0 0.5em 0 "+neon+", 0 0 0.5em 0 "+neon;
}

/*=======================| SCIENCE |===========================================*/
function lit_science_state() {
    var science_state = document.getElementById('science-state');
    science_state.style.background = neon;
    science_state.style.textShadow = "none";
    science_state.style.boxShadow  = "0 0 2em 0.3em"+neon;
}
function unlit_science_state() {
    var science_state = document.getElementById('science-state');
    science_state.style.background = "transparent";
    science_state.style.textShadow = "0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.25em currentColor";
    science_state.style.boxShadow  = "inset 0 0 0.5em 0 "+neon+", 0 0 0.5em 0 "+neon;
}

/*=======================| MANUALCONTROL |===========================================*/
function lit_manual_state() {
    var manual_state = document.getElementById('manual-state');
    manual_state.style.background = neon;
    manual_state.style.textShadow = "none";
    manual_state.style.boxShadow  = "0 0 2em 0.3em"+neon;
}
function unlit_manual_state() {
    var manual_state = document.getElementById('manual-state');
    manual_state.style.background = "transparent";
    manual_state.style.textShadow = "0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.25em currentColor";
    manual_state.style.boxShadow  = "inset 0 0 0.5em 0 "+neon+", 0 0 0.5em 0 "+neon;
}

/*=========================| WAITING |==============================================*/
function lit_waiting_state() {
    var waiting_state = document.getElementById('waiting-state');
    waiting_state.style.background = yellow;
    waiting_state.style.color = "black";
    waiting_state.style.textShadow = "none";
    waiting_state.style.boxShadow  = "0 0 2em 0.3em"+yellow;
}
function unlit_waiting_state() {
    var waiting_state = document.getElementById('waiting-state');
    waiting_state.style.background = "transparent";
    waiting_state.style.color = "white";
    waiting_state.style.textShadow = "0 0 0.125em hsl(0 0% 100% / 0.3), 0 0 0.25em currentColor";
    waiting_state.style.boxShadow  = "inset 0 0 0.5em 0 "+yellow+", 0 0 0.5em 0 "+yellow;
}
