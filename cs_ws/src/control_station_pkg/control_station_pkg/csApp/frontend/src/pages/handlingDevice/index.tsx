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
import useCameraManager from "../../hooks/cameraManager";
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

export default ({ mode }: { mode: Exclude<Mode, Mode.SEMI_AUTONOMOUS> }) => {
	const [images, cameras, selectCamera] = useCameraSelector([Cameras.CAM1]);
	const [jointPositions, jointVelocities, jointCurrents, detectedTags, taskSuccess] =
		useHandlingDevice();

	if (mode === Mode.AUTONOMOUS)
		return (
			<div className="page">
				<Background />
				<BackButton />
				<PageHeader
					title="Maintenance"
					settings
					optionTitle="Cameras"
					options={["Camera 1", "Camera 2", "Camera 3"]}
					optionsCallback={selectCamera}
				/>
				<div className={styles.globalContainer}>
					<div className={styles.container}>
						<button className={styles.button} onClick={() => buttonSelect(0)}>
							Button A1 1
						</button>
						<button className={styles.button} onClick={() => buttonSelect(1)}>
							Button A1 2
						</button>
						<button className={styles.button} onClick={() => buttonSelect(2)}>
							Button A1 3
						</button>
						<button className={styles.button} onClick={() => buttonSelect(3)}>
							Button A1 4
						</button>
						<button className={styles.button} onClick={() => buttonSelect(4)}>
							Button A1 5
						</button>
						<button className={styles.button} onClick={() => buttonSelect(5)}>
							Button A1 6
						</button>
						<button className={styles.button} onClick={() => buttonSelect(6)}>
							Button A1 7
						</button>
						<button className={styles.button} onClick={() => buttonSelect(7)}>
							Button A1 8
						</button>
						<button className={styles.button} onClick={() => buttonSelect(8)}>
							Button A1 9
						</button>
						<button className={styles.button} onClick={() => buttonSelect(9)}>
							Button A1 10
						</button>
						<button className={styles.button} onClick={() => buttonSelect(10)}>
							Button A2 1
						</button>
						<button className={styles.button} onClick={() => buttonSelect(11)}>
							Button A2 2
						</button>
						<button className={styles.button} onClick={() => buttonSelect(12)}>
							Button A2 3
						</button>
						<button className={styles.button} onClick={() => buttonSelect(13)}>
							Button A2 4
						</button>
						<button className={styles.button} onClick={() => buttonSelect(20)}>
							Button B1 1
						</button>
						<button className={styles.button} onClick={() => buttonSelect(21)}>
							Button B1 2
						</button>
					</div>
					<TaskControl task={Task.HANDLING_DEVICE} />
				</div>
				<Timer end={Date.now() + 10000} size={Size.SMALL} />
				<CameraView images={images} />
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
					"Camera 2",
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
				<ModeSlider />
				<GamepadHint />
				<TaskControl task={Task.HANDLING_DEVICE} />
			</div>

			<Timer end={Date.now() + 10000} size={Size.SMALL} />

			<CameraView images={images} />
		</div>
	);
};
