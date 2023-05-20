import { useState, useEffect } from "react";

function useElecInfos() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [humidity, setHumidity] = useState(0);
	const [temperature, setTemperature] = useState(0);
	const [conductivity, setConductivity] = useState(0);
	const [mass1, setMass1] = useState(0);
	const [mass2, setMass2] = useState(0);
	const [concentration, setConcentration] = useState(0);
	const [pH, setPH] = useState(0);

	useEffect(() => {
		let handlingDeviceSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/info_elec/");

		handlingDeviceSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setHumidity(data.humidity);
			setTemperature(data.temperature);
			setConductivity(data.conductivity);
			setMass1(data.mass_1);
			setMass2(data.mass_2);
			setConcentration(data.concentration);
			setPH(data.pH);
		};

		handlingDeviceSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(handlingDeviceSocket);
	}, []);

	return [humidity, temperature, conductivity, mass1, mass2, concentration, pH] as const;
}

export default useElecInfos;
