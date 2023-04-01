import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import CameraView from "../../components/CameraView";
import PageHeader from "../../components/PageHeader";
import Timer from "../../components/Timer";
import { Cameras } from "../../utils/cameras.type";

export default () => {
	return (
		<div className="page center">
			<Background />
			<BackButton />
			<PageHeader title="Camera" />
			<Timer end={Date.now() + 10000} />
			<CameraView camera={Cameras.NOCAM} />
		</div>
	);
};
