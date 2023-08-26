import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import { Task } from "../../utils/tasks.type";
import TaskControl from "../../components/TaskControl";
import styles from "./style.module.sass";
import { WaveGraph } from "../../components/WaveGraph";
import { Table } from "../../components/Table";
import { Sensor } from "../../utils/sensor.type";
import useScienceDataInfos from "../../hooks/scienceDataHooks";

const candidates = [
	{ percentage: 78, element: "Phosphate" },
	{ percentage: 77.8, element: "Materiau1" },
	{ percentage: 74, element: "Materiau2" },
	{ percentage: 73.9, element: "Materiau3" },
	{ percentage: 73.3, element: "Materiau4" },
];

export default () => {
	const [mass, npkSensor, fourInOneSensor, spectrometer, spectrometerCandidate] =
		useScienceDataInfos();

	return (
		<div className="page">
			<Background />
			<BackButton />
			<div className={styles.InfoContainer}>
				<WaveGraph
					measure={spectrometer.map((measure, index) => ({ x: index, y: measure }))}
					pointsSecondWave={spectrometerCandidate.map((measure, index) => ({
						x: index,
						y: measure,
					}))}
					candidates={candidates}
				/>
			</div>
			<div className={styles.Info}>
				<div className={styles.ControlsContainer}>
					<Table values={npkSensor} sensorType={Sensor.NPK} />
					<Table values={fourInOneSensor} sensorType={Sensor.ALL} />
					<Table values={mass} sensorType={Sensor.MASS} />
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
