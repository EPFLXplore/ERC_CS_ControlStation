import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import JointPositions from "../../components/JointPositions";
import { Mode } from "../../utils/mode.type";
import styles from "./style.module.sass";
import PageHeader from "../../components/PageHeader";
import CameraView from "../../components/CameraView";
import { Cameras } from "../../utils/cameras.type";
import Timer from "../../components/Timer";
import { Size } from "../../utils/size.type";
import JointSpeed from "../../components/JointSpeed";
import useHandlingDevice from "../../hooks/handlingDeviceHooks";
import JointCurrents from "../../components/JointCurrents";
import buttonSelect from "../../utils/buttonSelect";
import { Task } from "../../utils/tasks.type";
import TaskControl from "../../components/TaskControl";
import useCameraSelector from "../../hooks/cameraHooks";
import hdModeSelect from "../../utils/hdModeSelect";
import { useEffect, useState } from "react";
import { HD_Mode } from "../../utils/HDMode";
import Button from "../../components/Button";
import { Themes } from "../../utils/themes";
import VoltmeterValue from "../../components/VoltmeterValue";
import ButtonSelector from "../../components/ButtonSelector";

export default ({ mode }: { mode: Exclude<Mode, Mode.SEMI_AUTONOMOUS> }) => {
	const [images, cameras, selectCamera, flushCameras, rotateCams, setRotateCams] =
		useCameraSelector([Cameras.CAM7]);
	const [jointPositions, jointVelocities, jointCurrents, availableButtons,
		taskSuccess,
		voltmeter,
		openVoltmeter] =
		useHandlingDevice();
	const [hdSettings, setHdSettings] = useState(false);

	useEffect(() => {
		hdModeSelect(HD_Mode.Auto);
	}, []);

	return (
		<div className="page center">
			<CameraView images={images} rotate={rotateCams} setRotateCams={setRotateCams} />
			<Background />
			<BackButton onGoBack={() => flushCameras()} />
			<PageHeader
				title="Maintenance"
				settings
				optionTitle="Cameras"
				options={[
					//"Camera 1",
					//"Camera 2",
					"Camera 3",
					"Camera 4",
					// "Camera 5",
					// "Camera 6",
					"Camera Gripper",
					"Camera Nav"
				]}
				optionsCallback={selectCamera}
				currentOptions={cameras.map((camera) =>
					camera < 6 ? "Camera " + (camera + 1) : camera < 7 ? "Camera Gripper" : "Camera Nav"
				)}
			/>
			<div className={styles.jointContainer}>
				<JointPositions positions={jointPositions} />
				<JointSpeed speeds={jointVelocities} />
				<JointCurrents currents={jointCurrents} />
				<VoltmeterValue value={voltmeter} />
			</div>
			<div className={styles.globalContainer}>
				<ButtonSelector availableButtons={availableButtons} buttonSelect={buttonSelect}/>
				<Button size={Size.SMALL} theme={Themes.BROWN} text="Cancel" onClick={() => buttonSelect(-1)} />
				<TaskControl task={Task.HANDLING_DEVICE} />
			</div>
			<Timer end={Date.now() + 10000} size={Size.SMALL} />
		</div>
	);
};
