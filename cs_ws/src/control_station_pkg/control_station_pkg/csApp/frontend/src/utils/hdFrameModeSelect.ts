import { HD_Mode } from "./HDMode";
import { HD_Frame_Mode } from "./HDModeFrame";
import { getCookie } from "./requests";

function createRequest(id: HD_Frame_Mode) {
	const csrftoken = getCookie("csrftoken");

	const data = new FormData();
	data.append("inverse_frame", id === 0 ? "gripper" : "rover");

	return new Request("http://" + window.location.host + "/csApp/handlingdevice/set_hd_inverse_frame", {
		method: "POST",
		body: data,
		headers: { "X-CSRFToken": csrftoken ?? "" },
	});
}

export default (mode: HD_Frame_Mode) => {
	const req = createRequest(mode);
	fetch(req)
		.then((response) => response.json())
		.then((data) => console.log(data));
};
