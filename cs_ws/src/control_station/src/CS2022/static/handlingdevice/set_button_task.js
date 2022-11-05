document.querySelector("#set_id").addEventListener("click", event => {
    event.preventDefault();
    
    /* sending goal coordinates to back-end*/
    let formData = new FormData();
    formData.append('id', document.querySelector("#dropdown_id").value);

    let csrfTokenValue = document.querySelector('[name=csrfmiddlewaretoken]').value;
    let request = new Request('set_id/', {method: 'POST',
                                        body: formData,
                                        headers: {"X-CSRFToken": csrfTokenValue}})
    fetch(request)
        .then(response => response.json())
        .then(result => {})
    })