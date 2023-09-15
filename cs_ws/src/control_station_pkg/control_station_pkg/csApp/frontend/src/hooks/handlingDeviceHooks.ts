import { useState, useEffect } from "react";
import { getCookie } from "../utils/requests";

function useHandlingDevice() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [jointPositions, setJointPositions] = useState([0, 0, 0, 0, 0, 0]);
	const [jointVelocities, setJointVelocities] = useState([0, 0, 0, 0, 0, 0]);
	const [jointCurrents, setJointCurrents] = useState([0, 0, 0, 0, 0, 0]);
	const [availableButtons, setAvailableButtons] = useState(new Array(16).fill(false));
	const [taskSuccess, setTaskSuccess] = useState(false);
	const [voltmeter, setVoltmeter] = useState(0);
	const [ready, setReady] = useState(false);

	useEffect(() => {
		let handlingDeviceSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/info_hd/");

		handlingDeviceSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setJointPositions(data.joint_position);
			setJointVelocities(data.joint_velocity);
			setJointCurrents(data.joint_current);
			setAvailableButtons(data.available_buttons);
			setTaskSuccess(data.task_outcome);
			setVoltmeter(data.voltage);
			setReady(data.ready == 1);
		};

		handlingDeviceSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(handlingDeviceSocket);
	}, []);

	const openVoltmeter = (open: boolean) => {
		const csrftoken = getCookie("csrftoken");
		const data = new FormData();
		data.append("deployment", open ? "open" : "close");

		let request = new Request(
			"http://127.0.0.1:8000/csApp/handlingdevice/deploy_hd_voltmeter",
			{
				method: "POST",
				headers: {
					"X-CSRFToken": csrftoken ?? "",
				},
				body: data,
			}
		);

		fetch(request)
			.then((res) => res.json())
			.then((data) => console.log(data))
			.catch((err) => console.log(err));
	};

	return [
		jointPositions,
		jointVelocities,
		jointCurrents,
		availableButtons,
		taskSuccess,
		voltmeter,
		openVoltmeter,
		ready
	] as const;
}

export default useHandlingDevice;
