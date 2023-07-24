import { Task } from "../../utils/tasks.type";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import TaskControl from "../../components/TaskControl";
import styles from "./style.module.sass";
import PageHeader from "../../components/PageHeader";
import { Cameras } from "../../utils/cameras.type";
import CameraView from "../../components/CameraView";
import useCameraSelector from "../../hooks/cameraHooks";

//to replace by the real data
const state = "Extracting sample..";

export default () => {
	const [images, cameras, selectCamera] = useCameraSelector([Cameras.CAM1]);
	return (
		<div>
			<Background />
			<BackButton />
			<BackButton />
			<div className={styles.InfoControllerContainer}>
				<div className={styles.title}>Drill State</div>
				<div className={styles.stateDisplay}>{state}</div>
			</div>
			<div className={styles.taskControlContainer}>
				<TaskControl task={Task.SCIENCE} />
			</div>
			<PageHeader
				title="Camera Selector"
				settings
				optionTitle="Cameras"
				options={["Camera 1", "Camera 2", "Camera 3", "Camera 4", "Camera 5", "Camera 6"]}
				optionsCallback={selectCamera}
				currentOptions={cameras.map((camera) => "Camera " + (camera + 1))}
			/>

			<CameraView images={images} />
		</div>
	);
};
