import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import WorkInProgress from "../../components/WorkInProgress";
import { Task } from "../../utils/tasks.type";
import TaskControl from "../../components/TaskControl";
import styles from "./style.module.sass";
import { WaveGraph } from "../../components/WaveGraph";
import { Table } from "../../components/Table";
import { Sensor } from "../../utils/sensor.type";

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

const values1 = [10, 5.4, 12];
const values2 = [10, 5.4, 12, 6];

export default () => {
	return (
		<div className="page">
			<Background />
			<BackButton />
			<div className={styles.InfoContainer}>
				<WaveGraph
					pointsFirstWave={pointsFirstWave}
					pointsSecondWave={pointsSecondWave}
					percentage={78}
					mainComponent="Phosphate"
				/>
			</div>
			<div className={styles.Info}>
				<div className={styles.ControlsContainer}>
					<Table values={values1} sensorType={Sensor.NPK} />
					<Table values={values2} sensorType={Sensor.ALL} />
				</div>
			</div>
			<div className={styles.taskControlContainer}>
				<TaskControl task={Task.SCIENCE} />
			</div>
		</div>
	);
};
