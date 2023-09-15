import { useState, useEffect } from "react";

function useScienceDataInfos() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [mass, setMass] = useState([0, 0]);
	const [npkSensor, setNpkSensor] = useState([0, 0, 0]);
	const [fourInOneSensor, setFourInOneSensor] = useState([0, 0, 0, 0]);
	const [spectrometer, setSpectrometer] = useState(new Array(18).fill(0));
	const [spectrometerCandidate, setSpectrometerCandidate] = useState(new Array(18).fill(0));

	useEffect(() => {
		let scienceDataSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/science_data/");

		scienceDataSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setMass([data.drill_mass, data.container_mass]);
			setNpkSensor(data.npk_sensor);
			setFourInOneSensor(data.four_in_one);
			setSpectrometer(data.spectrometer);
			setSpectrometerCandidate(data.spectrometer_closest_candidate);
		};

		scienceDataSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(scienceDataSocket);
	}, []);

	return [mass, npkSensor, fourInOneSensor, spectrometer, spectrometerCandidate] as const;
}

export default useScienceDataInfos;
