import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import JointPositions from "../../components/JointPositions";
import { Mode } from "../../utils/mode.type";
import styles from "./style.module.sass";
import GamepadHint from "../../components/GamepadHint";
import PageHeader from "../../components/PageHeader";
import DistanceHint from "../../components/DistanceHint";
import CameraView from "../../components/CameraView";
import { Cameras } from "../../utils/cameras.type";
import Timer from "../../components/Timer";
import { Size } from "../../utils/size.type";
import ModeSlider from "../../components/ModeSlider";
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

export default ({ mode }: { mode: Exclude<Mode, Mode.SEMI_AUTONOMOUS> }) => {
	const [images, cameras, selectCamera, flushCameras, rotateCams, setRotateCams] =
		useCameraSelector([Cameras.CAM1]);
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
					"Camera 1",
					//"Camera 2",
					"Camera 3",
					"Camera 4",
					// "Camera 5",
					// "Camera 6",
					"Camera Gripper",
				]}
				optionsCallback={selectCamera}
				currentOptions={cameras.map((camera) =>
					camera < 6 ? "Camera " + (camera + 1) : "Camera Gripper"
				)}
			/>
			<div className={styles.jointContainer}>
				<JointPositions positions={jointPositions} />
				<JointSpeed speeds={jointVelocities} />
				<JointCurrents currents={jointCurrents} />
				<VoltmeterValue value={voltmeter} />
			</div>
			<div className={styles.globalContainer}>
				<div className={styles.container}>
					<button
						className={availableButtons[0] == 1 ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(100)}
					>
						Switch A 1
					</button>
					<button
						className={availableButtons[1] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(101)}
					>
						Switch A 2
					</button>
					<button
						className={availableButtons[2] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(102)}
					>
						Switch A 3
					</button>
					<button
						className={availableButtons[3] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(103)}
					>
						Switch A 4
					</button>
					<button
						className={availableButtons[4] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(104)}
					>
						Switch A 5
					</button>
					<button
						className={availableButtons[5] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(105)}
					>
						Switch A 6
					</button>
					<button
						className={availableButtons[6] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(106)}
					>
						Switch A 7
					</button>
					<button
						className={availableButtons[7] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(107)}
					>
						Switch A 8
					</button>
					<button
						className={availableButtons[8] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(108)}
					>
						Switch A 9
					</button>
					<button
						className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(109)}
					>
						Switch A 10
					</button>
					<button
						className={availableButtons[10] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(10)}
					>
						Button Switch ON
					</button>
					<button
						className={availableButtons[11] == 1 ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(11)}
					>
						Metallic Plate
					</button>
					<button
						className={availableButtons[12] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(12)}
					>
						Magnet
					</button>
					<button
						className={availableButtons[10] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(13)}
					>
						Button Switch OFF
					</button>
					<button
						className={availableButtons[13] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(20)}
					>
						Voltmeter Detach
					</button>
					<button
						className={availableButtons[13] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(21)}
					>
						Voltmeter Retract
					</button>
					<button
						className={availableButtons[14] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(30)}
					>
						Ethernet Socket
					</button>
					<button
						className={availableButtons[15] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(31)}
					>
						Ethernet Cable
					</button>
					<button
						className={styles.button}
						onClick={() => buttonSelect(30)}
					>
						Pick Rock
					</button>
					<button
						className={styles.button}
						onClick={() => buttonSelect(31)}
					>
						Rassor Sample
					</button>
					<button
						className={availableButtons[0] == 1 ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(110)}
					>
						Switch A 1 OFF
					</button>
					<button
						className={availableButtons[1] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(111)}
					>
						Switch A 2 OFF
					</button>
					<button
						className={availableButtons[2] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(112)}
					>
						Switch A 3 OFF
					</button>
					<button
						className={availableButtons[3] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(113)}
					>
						Switch A 4 OFF
					</button>
					<button
						className={availableButtons[4] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(114)}
					>
						Switch A 5 OFF
					</button>
					<button
						className={availableButtons[5] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(105)}
					>
						Switch A 6 OFF
					</button>
					<button
						className={availableButtons[6] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(116)}
					>
						Switch A 7 OFF
					</button>
					<button
						className={availableButtons[7] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(117)}
					>
						Switch A 8 OFF
					</button>
					<button
						className={availableButtons[8] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(118)}
					>
						Switch A 9 OFF
					</button>
					<button
						className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
						onClick={() => buttonSelect(119)}
					>
						Switch A 10 OFF
					</button>
				</div>
				<Button size={Size.SMALL} theme={Themes.BROWN} text="Cancel" onClick={() => buttonSelect(-1)} />
				<TaskControl task={Task.HANDLING_DEVICE} />
			</div>
			<Timer end={Date.now() + 10000} size={Size.SMALL} />
		</div>
	);
};
