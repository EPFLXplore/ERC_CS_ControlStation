import { useState, useEffect } from "react";

function useScienceInfos() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [state, setState] = useState(0);
	const [motorPos, setMotorPos] = useState(0);
	const [motorSpeed, setMotorSpeed] = useState(0);
	const [motorCurrent, setMotorCurrent] = useState(0);
	const [drillSpeed, setDrillSpeed] = useState(0);
	const [limitSwitch1, setLimitSwitch1] = useState(false);
	const [limitSwitch2, setLimitSwitch2] = useState(false);

	useEffect(() => {
		let handlingDeviceSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/info_science/");

		handlingDeviceSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setState(data.state);
			setMotorPos(data.motor_pos);
			setMotorSpeed(data.motor_speed);
			setMotorCurrent(data.motor_current);
			setDrillSpeed(data.drill_speed);
			setLimitSwitch1(data.limt_switch_1);
			setLimitSwitch2(data.limt_switch_2);
		};

		handlingDeviceSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(handlingDeviceSocket);
	}, []);

	return [
		state,
		motorPos,
		motorSpeed,
		motorCurrent,
		drillSpeed,
		limitSwitch1,
		limitSwitch2,
	] as const;
}

export default useScienceInfos;
