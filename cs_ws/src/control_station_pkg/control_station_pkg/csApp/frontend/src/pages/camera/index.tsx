import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import CameraView from "../../components/CameraView";
import PageHeader from "../../components/PageHeader";
import Timer from "../../components/Timer";
import { Cameras } from "../../utils/cameras.type";
import useCameraSelector from "../../hooks/cameraHooks";

export default () => {
	const [images, cameras, selectCamera] = useCameraSelector([Cameras.CAM1]);

	return (
		<div className="page center">
			<Background />
			<BackButton />
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
				]}
				optionsCallback={selectCamera}
				currentOptions={cameras.map((camera) =>
					camera < 6 ? "Camera " + (camera + 1) : "Camera Gripper"
				)}
			/>
			<Timer end={Date.now() + 10000} />
			<CameraView images={images} />
		</div>
	);
};
