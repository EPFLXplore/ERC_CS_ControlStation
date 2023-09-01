import React from "react";
import { useState, useEffect } from "react";
import { Cameras } from "../utils/cameras.type";

/**
 * A custom hook that allows the user to select which cameras to display
 * @param startCamera The cameras to start with
 * @returns a custom hook that allows the user to select which cameras to display
 */
function useCameraSelector(startCamera: Array<Cameras>) {
	const [sockets, setSockets] = useState<Array<WebSocket | undefined>>([undefined]);
	const [images, setImages] = React.useState<Array<string>>([""]);
	const [cameras, setCameras] = useState<Array<Cameras>>(startCamera);

	/**
	 * Sets the cameras to be displayed on the screen
	 * @param camera The camera to be selected
	 * @param select Whether or not to select the camera
	 */
	const setCamera = (camera: Cameras, select: boolean) => {
		setCameras((prevCameras) => {
			let newCameras = prevCameras.filter((cam) => cam !== camera);
			if (select) newCameras.push(camera);
			console.log("selected: " + newCameras);
			return newCameras;
		});
	};

	/**
	 * Sets the image to be displayed on the screen for a specific camera
	 * @param image the image to be displayed
	 * @param index the index of the image to be displayed
	 */
	const setImage = (image: string, index: number) => {
		setImages((prevImages) => {
			let newImages = [...prevImages];
			newImages[index] = image;
			return newImages;
		});
	};

	/**
	 * Sets the socket that will receive the image for a specific camera
	 * @param socket the socket to be displayed
	 * @param index the index of the socket to be displayed
	 */
	const setSocket = (socket: WebSocket | undefined, index: number) => {
		setSockets((prevSockets) => {
			let newSockets = [...prevSockets];
			newSockets[index] = socket;
			return newSockets;
		});
	};

	/**
	 * Gets the value of a cookie
	 * @param name the name of the cookie
	 * @returns the value of the cookie
	 */
	const getCookie = (name: string): string | null => {
		let cookieValue = null;
		if (document.cookie && document.cookie !== "") {
			const cookies = document.cookie.split(";");
			for (let i = 0; i < cookies.length; i++) {
				const cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === name + "=") {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	};

	useEffect(() => {
		for (const socket in sockets) {
			if (Object.prototype.hasOwnProperty.call(sockets, socket)) {
				const element = sockets[socket];
				if (element) element.onmessage = null;
			}
		}

		let newSockets: Array<WebSocket> = [];
		setImages(new Array(cameras.length).fill(null));

		const csrftoken = getCookie("csrftoken");
		let formData = new FormData();

		formData.append("index", cameras.toString());

		let request = new Request("http://127.0.0.1:8000/csApp/cameras/enable_cameras", {
			method: "POST",
			headers: {
				"X-CSRFToken": csrftoken ?? "",
			},
			body: formData,
		});

		fetch(request)
			.then((res) => res.json())
			.then((data) => console.log(data))
			.catch((err) => console.log(err));

		for (let i = 0; i < cameras.length; i++) {
			let cameraSocket = new WebSocket(
				"ws://" + window.location.host + "/ws/cameras/" + "video" + cameras[i] + "/"
			);

			cameraSocket.onmessage = (e) => {
				const data = JSON.parse(e.data);
				console.log(data.data);
				setImage(data.data, i);
			};

			cameraSocket.onerror = (e) => {
				console.log(e);
				setSocket(undefined, i);
			};

			newSockets.push(cameraSocket);
		}

		setSockets(newSockets);
	}, [cameras]);

	/**
	 * Selects a camera to be displayed on the screen
	 * @param camera The camera to be selected
	 * @param select Whether or not to select the camera
	 */
	const selectCamera = (camera: string, select = true) => {
		switch (camera) {
			case "Camera 1":
				setCamera(
					Cameras.CAM1,
					!(cameras.includes(Cameras.CAM1) && cameras.length > 1) && select
				);
				break;
			case "Camera 2":
				setCamera(
					Cameras.CAM2,
					!(cameras.includes(Cameras.CAM2) && cameras.length > 1) && select
				);
				break;
			case "Camera 3":
				setCamera(
					Cameras.CAM3,
					!(cameras.includes(Cameras.CAM3) && cameras.length > 1) && select
				);
				break;
			case "Camera 4":
				setCamera(
					Cameras.CAM4,
					!(cameras.includes(Cameras.CAM4) && cameras.length > 1) && select
				);
				break;
			case "Camera 5":
				setCamera(
					Cameras.CAM5,
					!(cameras.includes(Cameras.CAM5) && cameras.length > 1) && select
				);
				break;
			case "Camera 6":
				setCamera(
					Cameras.CAM6,
					!(cameras.includes(Cameras.CAM6) && cameras.length > 1) && select
				);
				break;
			case "Camera Gripper":
				setCamera(
					Cameras.CAM7,
					!(cameras.includes(Cameras.CAM7) && cameras.length > 1) && select
				);
				break;
			default:
				setCamera(Cameras.NOCAM, select);
		}
	};

	const flushCameras = () => {
		setCameras([]);
	};

	return [images, cameras, selectCamera, flushCameras] as const;
}

export default useCameraSelector;
