
function showDirect(){
    var direct  = document.getElementById("direct_box");
    var inverse = document.getElementById("inverse_box");

    direct.style.display = "initial";
    inverse.style.display = "none";
}

function showInverse(){
    var direct  = document.getElementById("direct_box");
    var inverse = document.getElementById("inverse_box");

    inverse.style.display = "initial";
    direct.style.display = "none";
}