import { HD_Mode } from "./HDMode";
import { getCookie } from "./requests";

function createRequest(id: HD_Mode) {
	const csrftoken = getCookie("csrftoken");

	const data = new FormData();
	data.append("mode", id.toString());

	return new Request("http://" + window.location.host + "/csApp/handlingdevice/set_hd_mode", {
		method: "POST",
		body: data,
		headers: { "X-CSRFToken": csrftoken ?? "" },
	});
}

export default (mode: HD_Mode, callback?: (mode: number) => void) => {
	const req = createRequest(mode);
	callback && callback(mode);
	fetch(req)
		.then((response) => response.json())
		.then((data) => console.log(data));
};
