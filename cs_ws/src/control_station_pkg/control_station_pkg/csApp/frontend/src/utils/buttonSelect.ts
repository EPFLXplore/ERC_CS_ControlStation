import { getCookie } from "./requests";

function createRequest(id: number) {
	const csrftoken = getCookie("csrftoken");

	const data = new FormData();
	data.append("id", id.toString());

	return new Request("http://127.0.0.1:8000/csApp/handlingdevice/set_id", {
		method: "POST",
		body: data,
		headers: { "X-CSRFToken": csrftoken ?? "" },
	});
}

function createCancelRequest() {
	const csrftoken = getCookie("csrftoken");

	return new Request("http://127.0.0.1:8000/csApp/handlingdevice/cancel_hd", {
		method: "GET",
		headers: { "X-CSRFToken": csrftoken ?? "" },
	});
}

export default (task: number) => {
	console.log("Task " + task + " selected");

	if(task === -1) {
		const req = createCancelRequest();
		fetch(req).then((response) => response.status === 200);
		return;
	}

	const req = createRequest(task);
	fetch(req).then((response) => response.status === 200);
};
