import React from "react";
import { useState, useEffect } from "react";
import { Cameras } from "../utils/cameras.type";

function useCameraSelector(startCamera: Cameras) {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [image, setImage] = React.useState<string>("");
	const [camera, setCamera] = useState<Cameras>(startCamera);
	
	useEffect(() => {
		console.log("connect cam: " + camera)
		let cameraSocket = new WebSocket(
			"ws://" + window.location.host + "/ws/cameras/" + "video" + camera + "/"
		);

		cameraSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);
			console.log(data.data);
			setImage(data.data);
		};

		cameraSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(cameraSocket);
	}, [camera]);

	const selectCamera = (camera: string) => {
		switch (camera) {
			case "Camera 1":
				setCamera(Cameras.CAM1);
				break;
			case "Camera 2":
				setCamera(Cameras.CAM2);
				break;
			case "Camera 3":
				setCamera(Cameras.CAM3);
				break;
			default:
				setCamera(Cameras.NOCAM);
		}
	};

	return [image, camera, selectCamera] as const;
}

export default useCameraSelector;
