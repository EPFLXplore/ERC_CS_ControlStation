import React from "react";
import { useState, useEffect } from "react";
import { Cameras } from "../utils/cameras.type";

function useCameraSelector(item: Cameras) {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [image, setImage] = React.useState<string>("");

	useEffect(() => {
		let cameraSocket = new WebSocket(
			"ws://" + window.location.host + "/ws/cameras/" + "video" + item + "/"
		);

		cameraSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);
			setImage(data.message);
		};

		cameraSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(cameraSocket);
	}, []);

	return [image] as const;
}

export default useCameraSelector;
