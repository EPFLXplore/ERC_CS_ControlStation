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

export default ({ mode }: { mode: Exclude<Mode, Mode.SEMI_AUTONOMOUS> }) => {
	const [images, cameras, selectCamera, flushCameras, rotateCams, setRotateCams] =
		useCameraSelector([Cameras.CAM1]);
	const [jointPositions, jointVelocities, jointCurrents, availableButtons, taskSuccess] =
		useHandlingDevice();

	if (mode === Mode.AUTONOMOUS)
		return (
			<div className="page">
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
				</div>
				<div className={styles.globalContainer}>
					<div className={styles.container}>
						<button
							className={availableButtons[0] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(0)}
						>
							Switch A 1
						</button>
						<button
							className={availableButtons[1] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(1)}
						>
							Switch A 2
						</button>
						<button
							className={availableButtons[2] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(2)}
						>
							Switch A 3
						</button>
						<button
							className={availableButtons[3] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(3)}
						>
							Switch A 4
						</button>
						<button
							className={availableButtons[4] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(4)}
						>
							Switch A 5
						</button>
						<button
							className={availableButtons[5] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(5)}
						>
							Switch A 6
						</button>
						<button
							className={availableButtons[6] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(6)}
						>
							Switch A 7
						</button>
						<button
							className={availableButtons[7] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(7)}
						>
							Switch A 8
						</button>
						<button
							className={availableButtons[8] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(8)}
						>
							Switch A 9
						</button>
						<button
							className={availableButtons[9] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(9)}
						>
							Switch A 10
						</button>
						<button
							className={availableButtons[10] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(10)}
						>
							Button Switch
						</button>
						<button
							className={availableButtons[11] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(11)}
						>
							Socket
						</button>
						<button
							className={availableButtons[12] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(12)}
						>
							Magnet
						</button>
						<button
							className={availableButtons[13] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(13)}
						>
							Mettalic Plate
						</button>
						<button
							className={availableButtons[14] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(20)}
						>
							Ethernet Socket
						</button>
						<button
							className={availableButtons[15] ? styles.button : styles.disabledButton}
							onClick={() => buttonSelect(21)}
						>
							Ethernet Cable
						</button>
					</div>
					<TaskControl task={Task.HANDLING_DEVICE} />
				</div>
				<Timer end={Date.now() + 10000} size={Size.SMALL} />
			</div>
		);

	return (
		<div className="page">
			<Background />
			<BackButton />
			<PageHeader
				title="Maintenance"
				settings
				optionTitle="Cameras"
				options={[
					"Camera 1",
					//"Camera 2",
					"Camera 3",
					"Camera 4",
					"Camera 5",
					"Camera 6",
					"Camera 7",
				]}
				optionsCallback={selectCamera}
				currentOptions={cameras.map((camera) => "Camera " + (camera + 1))}
			/>
			<DistanceHint distance={10} />

			<div className={styles.jointContainer}>
				<JointPositions positions={jointPositions} />
				<JointSpeed speeds={jointVelocities} />
				<JointCurrents currents={jointCurrents} />
			</div>

			<div className={styles.globalContainer}>
				<ModeSlider
					name={"Arm Mode"}
					mode={["IK", "FK"]}
					functionTrigger={() => hdModeSelect(0)}
				/>
				<GamepadHint mode={"HD"} />
				<TaskControl task={Task.HANDLING_DEVICE} />
			</div>

			<Timer end={Date.now() + 10000} size={Size.SMALL} />

			<CameraView images={images} />
		</div>
	);
};
