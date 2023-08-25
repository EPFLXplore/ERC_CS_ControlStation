import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import { Task } from "../../utils/tasks.type";
import TaskControl from "../../components/TaskControl";
import styles from "./style.module.sass";
import { WaveGraph } from "../../components/WaveGraph";
import { Table } from "../../components/Table";
import { Sensor } from "../../utils/sensor.type";
import useElecInfos from "../../hooks/elecHooks";

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
const values2 = [10, 16, 12, 6];

const candidates = [
	{ percentage: 78, element: "Phosphate" },
	{ percentage: 77.8, element: "Materiau1" },
	{ percentage: 74, element: "Materiau2" },
	{ percentage: 73.9, element: "Materiau3" },
	{ percentage: 73.3, element: "Materiau4" },
];

export default () => {
	const [humidity, temperature, conductivity, pH] = useElecInfos();

	return (
		<div className="page">
			<Background />
			<BackButton />
			<div className={styles.InfoContainer}>
				<WaveGraph
					measure={pointsFirstWave}
					pointsSecondWave={pointsSecondWave}
					candidates={candidates}
				/>
			</div>
			<div className={styles.Info}>
				<div className={styles.ControlsContainer}>
					<Table values={values1} sensorType={Sensor.NPK} />
					<Table
						values={[humidity, temperature, conductivity, pH]}
						sensorType={Sensor.ALL}
					/>
				</div>
			</div>
			<div className={styles.taskControlContainer}>
				<TaskControl task={Task.SCIENCE} />
			</div>
			<div className={styles.InfoControllerContainer}>
				<div className={styles.table}>
					<thead>
						<tr>
							<th>Candidate 1</th>
							<th>Candidate 2</th>
							<th>Candidate 3</th>
							<th>Candidate 4</th>
							<th>Candidate 5</th>
						</tr>
					</thead>
					<tbody>
						<tr>
							{candidates.map((candidate, index) => (
								<td>
									{candidate.percentage}%, {candidate.element}
								</td>
							))}
						</tr>
					</tbody>
				</div>
			</div>
		</div>
	);
};
