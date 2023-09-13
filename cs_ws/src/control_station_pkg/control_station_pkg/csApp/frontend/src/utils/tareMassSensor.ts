import { HD_Mode } from "./HDMode";
import { HD_Frame_Mode } from "./HDModeFrame";
import { getCookie } from "./requests";

function createRequest(id: HD_Frame_Mode) {
	const csrftoken = getCookie("csrftoken");

	if(id === 0) {
		return new Request("http://" + window.location.host + "/csApp/science/drill_tare", {
			method: "GET",
			headers: { "X-CSRFToken": csrftoken ?? "" },
		});
	} else {
		return new Request("http://" + window.location.host + "/csApp/science/container_tare", {
			method: "GET",
			headers: { "X-CSRFToken": csrftoken ?? "" },
		});
	}
}

export default (tare: number) => {
	const req = createRequest(tare);
	fetch(req)
		.then((response) => response.json())
		.then((data) => console.log(data));
};
