function getCookie(name: string): string | null {
	let cookieValue = null;
	if (document.cookie && document.cookie !== "") {
		const cookies = document.cookie.split(";");
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			// Does this cookie string begin with the name we want?
			if (cookie.substring(0, name.length + 1) === name + "=") {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}

function createRequest(id: number) {
	const csrftoken = getCookie("csrftoken");

	const data = new FormData();
	data.append("mode", id.toString());

	return new Request("http://" + window.location.host + "/csApp/handlingdevice/set_hd_mode", {
		method: "POST",
		body: data,
		headers: { "X-CSRFToken": csrftoken ?? "" },
	});
}

export default (mode: number) => {
	const req = createRequest(mode);
	fetch(req)
		.then((response) => response.json())
		.then((data) => console.log(data));
};
