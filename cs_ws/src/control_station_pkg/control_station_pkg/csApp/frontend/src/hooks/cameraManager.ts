import React from "react";
import { useState, useEffect } from "react";
import { Cameras } from "../utils/cameras.type";

function useCameraManager(startCamera: Cameras) {
	const [camera, setCamera] = useState<Cameras>(startCamera);

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
			case "Camera 4":
				setCamera(Cameras.CAM4);
				break;
			case "Camera 5":
				setCamera(Cameras.CAM5);
				break;
			case "Camera 6":
				setCamera(Cameras.CAM6);
				break;
			default:
				setCamera(Cameras.NOCAM);
		}
	};

	return [camera, selectCamera] as const;
}

export default useCameraManager;
