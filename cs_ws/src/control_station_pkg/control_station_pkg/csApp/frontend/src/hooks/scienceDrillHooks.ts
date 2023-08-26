import { useState, useEffect } from "react";

function useScienceDrillInfos() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [state, setState] = useState("Waiting for task...");
	const [limitSwitches, setLimitSwitches] = useState([
		{ label: "1st LS", value: 0 },
		{ label: "2nd LS", value: 0 },
		{ label: "3rd LS", value: 0 },
		{ label: "4th LS", value: 0 },
	]);

	useEffect(() => {
		let scienceDrillSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/science_drill/");

		scienceDrillSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			// setState(geStateString(data.state));
			setLimitSwitches((values) =>
				data.limit_switches.map((value: number, index: number) => {
					let newval = values[index];
					return { label: values[index].label, value: value };
				})
			);
		};

		scienceDrillSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(scienceDrillSocket);
	}, []);

	return [state, limitSwitches] as const;
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
