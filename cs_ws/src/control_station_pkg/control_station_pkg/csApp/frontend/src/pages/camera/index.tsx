import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import CameraView from "../../components/CameraView";
import PageHeader from "../../components/PageHeader";
import Timer from "../../components/Timer";
import { Cameras } from "../../utils/cameras.type";
import useCameraSelector from "../../hooks/cameraHooks";

export default () => {
	const [images, cameras, selectCamera, flushCameras, rotateCams, setRotateCams] =
		useCameraSelector([Cameras.CAM3]);

	return (
		<div className="page center">
			<CameraView images={images} rotate={rotateCams} setRotateCams={setRotateCams} />
			<Background />
			<BackButton onGoBack={() => flushCameras()} />
			<PageHeader
				title="Camera"
				settings
				optionTitle="Cameras"
				options={[
					"Camera 1",
					"Camera 2",
					"Camera 3",
					"Camera 4",
					"Camera 5",
					"Camera 6",
					"Camera Gripper",
					"Camera Nav"
				]}
				optionsCallback={selectCamera}
				currentOptions={cameras.map((camera) =>
					camera < 6 ? "Camera " + (camera + 1) : camera < 7 ? "Camera Gripper" : "Camera Nav"
				)}
			/>
			<Timer end={Date.now() + 10000} />
		</div>
	);
};
