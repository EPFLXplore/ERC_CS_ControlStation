import { useState, useEffect } from "react";

function useScienceDataInfos() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [mass, setMass] = useState([0, 0]);
	const [npkSensor, setNpkSensor] = useState([0, 0, 0]);
	const [fourInOneSensor, setFourInOneSensor] = useState([0, 0, 0, 0]);

	useEffect(() => {
		let scienceDataSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/science_data/");

		scienceDataSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setMass(data.mass);
			setNpkSensor(data["npk-sensor"]);
			setFourInOneSensor(data["four-in-one-sensor"]);
		};

		scienceDataSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(scienceDataSocket);
	}, []);

	return [mass, npkSensor, fourInOneSensor] as const;
}

export default useScienceDataInfos;
