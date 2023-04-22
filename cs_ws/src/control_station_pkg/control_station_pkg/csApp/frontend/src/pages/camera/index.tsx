import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import CameraView from "../../components/CameraView";
import PageHeader from "../../components/PageHeader";
import Timer from "../../components/Timer";
import { Cameras } from "../../utils/cameras.type";
import useCameraManager from "../../hooks/cameraManager";

export default () => {
	const [camera, selectCamera] = useCameraManager(Cameras.CAM1);

	return (
		<div className="page center">
			<Background />
			<BackButton />
			<PageHeader
				title="Camera"
				settings
				optionTitle="Cameras"
				options={["Camera 1", "Camera 2", "Camera 3"]}
				optionsCallback={selectCamera}
			/>
			<Timer end={Date.now() + 10000} />
			<CameraView camera={Cameras.NOCAM} />
		</div>
	);
};
