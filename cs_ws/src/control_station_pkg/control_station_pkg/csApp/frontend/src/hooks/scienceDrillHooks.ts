import { useState, useEffect } from "react";
import { roundToTwoDecimals } from "../utils/maths";
import { getCookie } from "../utils/requests";

function useScienceDrillInfos() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [state, setState] = useState("Waiting for task...");
	const [limitSwitches, setLimitSwitches] = useState([
		{ label: "1st LS", value: 0 },
		{ label: "2nd LS", value: 0 },
		{ label: "3rd LS", value: 0 },
		{ label: "4th LS", value: 0 },
	]);
	const [module1, setModule1] = useState({
		id: "Module1",
		velocity: 10,
		distance: 3,
		current: 12,
	});
	const [module2, setModule2] = useState({
		id: "Module2",
		velocity: 10,
		distance: 3,
		current: 12,
	});
	const [drill, setDrill] = useState({ id: "Drill", velocity: 5, distance: null, current: 9 });

	useEffect(() => {
		let scienceDrillSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/science_drill/");

		scienceDrillSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setState(geStateString(data.state));
			setLimitSwitches((values) =>
				data.limit_switches.map((value: number, index: number) => {
					let newval = values[index];
					return { label: values[index].label, value: value };
				})
			);
			setModule1((values) => {
				return {
					id: values.id,
					velocity: roundToTwoDecimals(data.motors_speed[0]),
					distance: roundToTwoDecimals(data.motors_pos[0]),
					current: roundToTwoDecimals(data.motors_currents[0]),
				};
			});
			setModule2((values) => {
				return {
					id: values.id,
					velocity: roundToTwoDecimals(data.motors_speed[1]),
					distance: roundToTwoDecimals(data.motors_pos[1]),
					current: roundToTwoDecimals(data.motors_currents[1]),
				};
			});
			setDrill((values) => {
				return {
					id: values.id,
					velocity: roundToTwoDecimals(data.motors_speed[2]),
					distance: null,
					current: roundToTwoDecimals(data.motors_currents[2]),
				};
			});
		};

		scienceDrillSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(scienceDrillSocket);
	}, []);

	const measureSpectro = () => {
		const csrftoken = getCookie("csrftoken");

		let request = new Request("http://127.0.0.1:8000/csApp/science/mesure_spectro", {
			method: "GET",
			headers: {
				"X-CSRFToken": csrftoken ?? "",
			},
		});

		fetch(request)
			.then((res) => res.json())
			.then((data) => console.log(data))
			.catch((err) => console.log(err));
	};

	const resetSpectro = () => {
		const csrftoken = getCookie("csrftoken");

		let request = new Request("http://127.0.0.1:8000/csApp/cameras/science/reset_spectro", {
			method: "GET",
			headers: {
				"X-CSRFToken": csrftoken ?? "",
			},
		});

		fetch(request)
			.then((res) => res.json())
			.then((data) => console.log(data))
			.catch((err) => console.log(err));
	};

	return [state, limitSwitches, module1, module2, drill, measureSpectro, resetSpectro] as const;
}

const geStateString = (state: number) => {
	switch (state) {
		case 0:
			return "Beginning the task...";
		case 1:
			return "Descending module...";
		case 2:
			return "Module is down...";
		case 3:
			return "Drilling...";
		case 4:
			return "Drilling is done...";
		case 5:
			return "Ascending drill...";
		case 6:
			return "Drill is up...";
		case 7:
			return "Dirt is discharged...";
		case 8:
			return "Ascending module...";
		case 9:
			return "Module is up...";
		case 10:
			return "Task is done succesfully...";
		case 11:
			return "Abort receive...";
		case 12:
			return "Abort mode: module go up...";
		case 13:
			return "Abort mode: module is up...";
		case 14:
			return "Abort mode: drill go up...";
		case 15:
			return "Abort mode: drill is up...";
		case 16:
			return "Abort mode: task is done...";
		case 17:
			return "Wait receive...";
		default:
			return "Unknown state...";
	}
};

export default useScienceDrillInfos;
