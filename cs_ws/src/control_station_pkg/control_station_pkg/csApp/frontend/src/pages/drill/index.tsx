import { Task } from "../../utils/tasks.type";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import TaskControl from "../../components/TaskControl";
import styles from "./style.module.sass";

//to replace by the real data
const state = "Extracting sample..";

export default () => {
	return (
		<div>
			<Background />
			<BackButton />
			<div className={styles.ControlsContainer}>
				<div className={styles.title}>Drill State</div>
				<div className={styles.stateDisplay}>{state}</div>
			</div>
			<div className={styles.taskControlContainer}>
				<TaskControl task={Task.SCIENCE} />
			</div>
			<BackButton />
		</div>
	);
};
