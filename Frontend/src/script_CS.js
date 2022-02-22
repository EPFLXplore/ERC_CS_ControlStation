function openTab(evt, tabName) {
    var i, x, tablinks;
    x = document.getElementsByClassName("tab");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    tablinks = document.getElementsByClassName("tablink");
    for (i = 0; i < x.length; i++) {
        tablinks[i].className = tablinks[i].className.replace(" w3-blue", ""); 
    }
    document.getElementById(tabName).style.display = "block";
    evt.currentTarget.className += " w3-blue";
    
}
// =============================================================
var battery = navigator.battery;
var level    = battery.level * 100;
var batteryLevel = jQuery('.battery .battery-level');
batteryLevel.css('width', level + '%');
batteryLevel.text(level + '%');
if (battery.charging) {
    batteryLevel.addClass('charging');
} else if (level > 50) {  
    batteryLevel.addClass('high');  
} else if (level >= 25 ) {  
    batteryLevel.addClass('medium');  
} else {  
    batteryLevel.addClass('low');  
}
// =============================================================
function updateBatteryDisplay(battery) {
	var level = battery.level * 100;
	var batteryLevel = jQuery('battery battery-level');
	batteryLevel.css('width', level + '%');
	batteryLevel.text(level + '%');
	if (battery.charging) {
	    batteryLevel.addClass('charging');
	    batteryLevel.removeClass('high');  
	    batteryLevel.removeClass('medium');  
	    batteryLevel.removeClass('low');  
	} else if (level > 50) {  
	    batteryLevel.addClass('high');  
	    batteryLevel.removeClass('charging');
	    batteryLevel.removeClass('medium');  
	    batteryLevel.removeClass('low');  
	} else if (level >= 25 ) {  
	    batteryLevel.addClass('medium');  
	    batteryLevel.removeClass('charging');
	    batteryLevel.removeClass('high');  
	    batteryLevel.removeClass('low');  
	} else {  
	    batteryLevel.addClass('low');  
	    batteryLevel.removeClass('charging');
	    batteryLevel.removeClass('high');  
	    batteryLevel.removeClass('medium');  
	}
}

var battery = navigator.battery;
updateBatteryDisplay(battery);
battery.onchargingchange = function () {
    updateBatteryDisplay(battery);
};
battery.onlevelchange = function () {
    updateBatteryDisplay(battery);
};