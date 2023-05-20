import { useState, useEffect } from "react";

function useHandlingDevice() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [jointPositions, setJointPositions] = useState([0, 0, 0, 0, 0, 0]);
	const [jointVelocities, setJointVelocities] = useState([0, 0, 0, 0, 0, 0]);
	const [jointCurrents, setJointCurrents] = useState([0, 0, 0, 0, 0, 0]);
	const [detectedTags, setDetectedTags] = useState([false, false, false, false]);
	const [taskSuccess, setTaskSuccess] = useState(false);

	useEffect(() => {
		let handlingDeviceSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/info_hd/");

		handlingDeviceSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setJointPositions(data.joint_position);
			setJointVelocities(data.joint_velocity);
			setJointCurrents(data.joint_current);
			setDetectedTags(data.detected_tags);
			setTaskSuccess(data.task_outcome);
		};

		handlingDeviceSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(handlingDeviceSocket);
	}, []);

	return [jointPositions, jointVelocities, jointCurrents, detectedTags, taskSuccess] as const;
}

export default useHandlingDevice;
