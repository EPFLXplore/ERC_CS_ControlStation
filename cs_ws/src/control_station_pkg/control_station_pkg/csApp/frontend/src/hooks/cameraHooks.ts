import React from "react";
import { useState, useEffect } from "react";
import { Cameras } from "../utils/cameras.type";

function useCameraSelector(startCamera: Cameras) {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [image, setImage] = React.useState<string>("");
	const [camera, setCamera] = useState<Cameras>(startCamera);

	const getCookie = (name: string): string | null => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

	useEffect(() => {

		console.log("connect cam: " + camera)

		const csrftoken = getCookie('csrftoken');
		let formData = new FormData();
			formData.append("index",  camera.toString());
			//formData.append('y',  y.toString());
			//formData.append('yaw', o.toString());

		let request = new Request("http://127.0.0.1:8000/csApp/cameras/enable_cameras",
			{
				method: "POST",
				headers: {
					"X-CSRFToken": csrftoken ?? ''
				},
				body: formData,
			})
	
		fetch(request).then((res) => res.json()).then((data) => console.log(data));

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
