import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import WorkInProgress from "../../components/WorkInProgress";
import { Task } from "../../utils/tasks.type";
import TaskControl from "../../components/TaskControl";
import styles from "./style.module.sass";
import { WaveGraph } from "../../components/WaveGraph";

const pointsFirstWave = [
	{ x: 0, y: 0 },
	{ x: 1, y: 1 },
	{ x: 2, y: 3 },
	{ x: 3, y: 2 },
	{ x: 0, y: 0 },
	{ x: 1, y: 1 },
	{ x: 2, y: 3 },
	{ x: 3, y: 2 },
	{ x: 0, y: 0 },
	{ x: 1, y: 1 },
	{ x: 2, y: 3 },
	{ x: 3, y: 2 },
	{ x: 0, y: 0 },
	{ x: 1, y: 1 },
	{ x: 2, y: 3 },
	{ x: 3, y: 2 },
];

const pointsSecondWave = [
	{ x: 0, y: 0 },
	{ x: 2, y: 2 },
	{ x: 3, y: 2 },
	{ x: 0, y: 2 },
	{ x: 0, y: 2 },
	{ x: 0, y: 0 },
	{ x: 2, y: 2 },
	{ x: 3, y: 2 },
	{ x: 0, y: 2 },
	{ x: 0, y: 2 },
	{ x: 0, y: 0 },
	{ x: 2, y: 2 },
	{ x: 3, y: 2 },
	{ x: 0, y: 2 },
	{ x: 0, y: 2 },
	{ x: 3, y: 2 },
];

export default () => {
	return (
		<div className="page">
			<Background />
			<BackButton />
			<div className={styles.infoContainer}>
				<div className={styles.GraphContainer}>
					<WaveGraph
						pointsFirstWave={pointsFirstWave}
						pointsSecondWave={pointsSecondWave}
					/>
				</div>
			</div>
			<div className={styles.Info}>
				<div className={styles.ControlsContainer}></div>
			</div>
			<div className={styles.taskControlContainer}>
				<TaskControl task={Task.SCIENCE} />
			</div>
		</div>
	);
};
