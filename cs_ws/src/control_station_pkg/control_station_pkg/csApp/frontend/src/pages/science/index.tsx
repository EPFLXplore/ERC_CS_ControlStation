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

// Sample data for the table
const lines = [
	{ id: "Phosphate", content: 10 },
	{ id: "Azote", content: 5.4 },
	{ id: "Potassium", content: 12 },
];

const lines2 = [
	{ id: "Humidity", content: 10 },
	{ id: "Temperature", content: 5.4 },
	{ id: "Elec", content: 12 },
	{ id: "PH", content: 6 },
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
				<div className={styles.ControlsContainer}>
					<h2 className={styles.title}>NPK sensor</h2>
					<Table lines={lines} sensorType={Sensor.NPK} />
					<h2 className={styles.title}>4-in-1 sensor</h2>
					<Table lines={lines2} sensorType={Sensor.ALL} />
				</div>
			</div>
			<div className={styles.taskControlContainer}>
				<TaskControl task={Task.SCIENCE} />
			</div>
		</div>
	);
};
