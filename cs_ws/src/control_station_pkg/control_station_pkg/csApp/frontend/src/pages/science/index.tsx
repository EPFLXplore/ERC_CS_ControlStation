import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import { Task } from "../../utils/tasks.type";
import TaskControl from "../../components/TaskControl";
import styles from "./style.module.sass";
import { WaveGraph } from "../../components/WaveGraph";
import { Table } from "../../components/Table";
import { Sensor } from "../../utils/sensor.type";
import useScienceDataInfos from "../../hooks/scienceDataHooks";
import { useState } from "react";
import PageHeader from "../../components/PageHeader";
import useCameraSelector from "../../hooks/cameraHooks";
import useScienceDrillInfos from "../../hooks/scienceDrillHooks";
import { Cameras } from "../../utils/cameras.type";
import Button from "../../components/Button";
import { Size } from "../../utils/size.type";
import { Themes } from "../../utils/themes";
import CameraView from "../../components/CameraView";
import ModeSlider from "../../components/ModeSlider";

const candidates = [
	{ percentage: 78, element: "Phosphate" },
	{ percentage: 77.8, element: "Materiau1" },
	{ percentage: 74, element: "Materiau2" },
	{ percentage: 73.9, element: "Materiau3" },
	{ percentage: 73.3, element: "Materiau4" },
];

type DataRow = {
	id: string;
	velocity: number;
	distance: number | null;
	current: number;
};

export default () => {
	const [mode, setMode] = useState(0);

	const [images, cameras, selectCamera, flushCameras, rotateCams, setRotateCams] =
		useCameraSelector([Cameras.CAM1]);
	const [state, limitSwitches, module1, module2, drill, measureSpectro, resetSpectro] =
		useScienceDrillInfos();
	const sensorType = "Sensor Data";
	const rows = ["Velocity", "Distance", "Current"]; // Rows titles
	const columns = ["Module1", "Module2", "Drill"]; // Columns titles

	const [mass, npkSensor, fourInOneSensor, spectrometer, spectrometerCandidate] =
		useScienceDataInfos();

	if (mode === 0) {
		return (
			<div>
				<CameraView images={images} rotate={rotateCams} setRotateCams={setRotateCams} />
				<Background />
				<BackButton onGoBack={() => flushCameras()} />
				<div className={styles.InfoControllerContainer}>
					<div className={styles.InfoDiv}>
						<div className={styles.title}>Drill State</div>
						<div className={styles.stateDisplay}>{state}</div>
					</div>
					<div className={styles.InfoDiv}>
						<div className={styles.title}>Spectrometer</div>
						<div className={styles.Buttons}>
							<Button
								text="Measure"
								size={Size.SMALL}
								theme={Themes.BROWN}
								onClick={() => {
									measureSpectro();
								}}
								radius={10}
							/>
							<Button
								text="Reset"
								size={Size.SMALL}
								theme={Themes.BROWN}
								onClick={() => {
									resetSpectro();
								}}
								radius={10}
							/>
						</div>
					</div>
					<div className={styles.InfoDiv}>
						<ModeSlider
							name="Science Mode"
							mode={["Data", "Drill"]}
							functionTrigger={() => setMode(1)}
						/>
					</div>
				</div>
				<div className={styles.taskControlContainer}>
					<TaskControl task={Task.SCIENCE} />
				</div>
				<PageHeader
					title="Science Drill"
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
				<div className={styles.rightContainer}>
					<div>
						<h2 className={styles.title}>{sensorType}</h2>
						<table className={styles.table}>
							<thead>
								<tr>
									<th>
										<text>Data</text>
									</th>
									{columns.map((columnTitle) => (
										<th key={columnTitle}>
											<text>{columnTitle}</text>
										</th>
									))}
								</tr>
							</thead>
							<tbody>
								{rows.map((rowTitle, rowIndex) => (
									<tr key={rowTitle}>
										<td>
											<text>{rowTitle}</text>
										</td>
										{columns.map((columnTitle) => {
											const rowData = [module1, module2, drill].find(
												(item) => item.id === columnTitle
											);
											const value = rowData
												? rowData[rowTitle.toLowerCase() as keyof DataRow]
												: null;
											return (
												<td
													key={`${rowIndex}-${columnTitle}`}
													className={
														value === null ? styles.cellHashed : ""
													}
												>
													<text>{value !== null ? value : ""}</text>
												</td>
											);
										})}
									</tr>
								))}
							</tbody>
						</table>
					</div>

					<div>
						<h2 className={styles.title}>Limit switches</h2>
						<table className={styles.table}>
							<thead>
								<tr>
									<th>
										<text>Limit Switch</text>
									</th>
									<th>
										<text>State</text>
									</th>
								</tr>
							</thead>
							<tbody>
								{limitSwitches.map((circle, index) => (
									<tr key={index}>
										<td>
											<text>{circle.label}</text>
										</td>
										<td>
											<div
												className={
													circle.value === 1
														? styles.greenCircle
														: styles.redCircle
												}
											></div>
										</td>
									</tr>
								))}
							</tbody>
						</table>
					</div>
				</div>
			</div>
		);
	} else {
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
					<ModeSlider
						name="Science Mode"
						mode={["Drill", "Data"]}
						functionTrigger={() => setMode(0)}
					/>
				</div>
			</div>
		);
	}
};
