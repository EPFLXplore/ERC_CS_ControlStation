import { NavMode } from "./navMode";
import { getCookie } from "./requests";

function createModeRequest(id: NavMode) {
	const csrftoken = getCookie("csrftoken");

	const data = new FormData();

    switch (id) {
        case NavMode.Manual_Basic:
            data.append("mode", "manual");
            break;
        case NavMode.Manual_Normal:
            data.append("mode", "manual");
            break;
        case NavMode.Autonomous:
            data.append("mode", "auto");
            break;
    }
    
    return new Request("http://" + window.location.host + "/csApp/navigation/nav_mode", {
        method: "POST",
        body: data,
        headers: { "X-CSRFToken": csrftoken ?? "" },
    });
}

function createKinematicRequest(id: NavMode) {
	const csrftoken = getCookie("csrftoken");

	const data = new FormData();
    
    switch (id) {
        case NavMode.Manual_Basic:
            data.append("kinematic", "basic");
            break;
        case NavMode.Manual_Normal:
            data.append("kinematic", "normal");
            break;
        case NavMode.Autonomous:
            return null;
            break;
    }
    
    return new Request("http://" + window.location.host + "/csApp/navigation/nav_kinematic", {
        method: "POST",
        body: data,
        headers: { "X-CSRFToken": csrftoken ?? "" },
    });
}

export default (mode: NavMode) => {
	const req = createModeRequest(mode);
	fetch(req)
		.then((response) => response.json())
		.then((data) => console.log(data));

        const req2 = createKinematicRequest(mode);
        if (req2 != null) {
            fetch(req2)
                .then((response) => response.json())
                .then((data) => console.log(data));
        }
};
