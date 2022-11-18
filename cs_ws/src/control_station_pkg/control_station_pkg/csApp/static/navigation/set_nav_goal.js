document.querySelector("#nav_set").addEventListener("click", event => {
    event.preventDefault();

    let x = document.querySelector("#x").value
    let y = document.querySelector("#y").value
    /* sending goal coordinates to back-end*/
    let formData = new FormData();
    formData.append('x', x);
    formData.append('y', -y);
    formData.append('yaw', document.querySelector('#yaw').value);
    document.getElementById("xgoal").innerHTML = document.querySelector("#x").value;
    document.getElementById("ygoal").innerHTML = document.querySelector("#y").value;


    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let request = new Request('set_goal/', {
        method: 'POST',
        body: formData,
        headers: { "X-CSRFToken": csrfTokenValue }
    })
    fetch(request)
        .then(response => response.json())
        .then(result => { })

    myContext.fillStyle = 'red';
    myContext.fillRect(x, y, 10, 10)
})