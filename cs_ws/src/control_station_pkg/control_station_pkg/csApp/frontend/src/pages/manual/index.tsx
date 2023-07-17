import React, { useState } from "react";
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
import { useNavigation } from "../../hooks/navigationHooks";
import ManualModeSelector from "../../components/ManualModeSelector";
import { useLocation } from "react-router-dom";

function useQuery() {
	const { search } = useLocation();

	return React.useMemo(() => new URLSearchParams(search), [search]);
}

export default () => {
	const [camera, selectCamera] = useCameraManager(Cameras.CAM1);
	const [jointPositions, jointVelocities, jointCurrents, detectedTags, taskSuccess] =
		useHandlingDevice();
	const [currentPosition, currentOrientation, wheelsPosition, linearVelocity, angularVelocity] =
		useNavigation();
	const defaultMode = useQuery().get("defaultMode");

	console.log(defaultMode);

	const [mode, setMode] = useState(
		defaultMode === "nav" ? Task.NAVIGATION : Task.HANDLING_DEVICE
	);

	if (mode === Task.HANDLING_DEVICE) {
		return (
			<div className="page">
				<Background />
				<BackButton />
				<PageHeader
					title="Manual Control (HD)"
					settings
					optionTitle="Cameras"
					options={[
						"Camera 1",
						"Camera 2",
						"Camera 3",
						"Camera 4",
						"Camera 5",
						"Camera 6",
					]}
					optionsCallback={selectCamera}
				/>
				<div className={styles.Subheader}>
					<ManualModeSelector mode={Task.HANDLING_DEVICE} callback={setMode} />
				</div>
				{/* <DistanceHint distance={10} /> */}

				<div className={styles.jointContainer}>
					<JointPositions positions={jointPositions} />
					<JointSpeed speeds={jointVelocities} />
					<JointCurrents currents={jointCurrents} />
				</div>

				<div className={styles.globalContainer}>
					<ModeSlider />
					<TaskControl task={Task.HANDLING_DEVICE} />
				</div>

				<Timer end={Date.now() + 10000} size={Size.SMALL} />
				<GamepadHint />
				<CameraView camera={camera} />
			</div>
		);
	} else {
		return (
			<div className="page center">
				<Background />
				<BackButton />
				<PageHeader
					title="Manual Control (NAV)"
					settings
					optionTitle="Cameras"
					options={[
						"Camera 1",
						"Camera 2",
						"Camera 3",
						"Camera 4",
						"Camera 5",
						"Camera 6",
					]}
					optionsCallback={selectCamera}
				/>
				<div className={styles.Subheader}>
					<ManualModeSelector mode={Task.NAVIGATION} callback={setMode} />
				</div>

				<div className={styles.CamSpace}>
					<div className={styles.StatsContainer}>
						<div className={styles.InfoText}>
							<div>
								<h3>Current position</h3>
								<div className={styles.InfoArrangement}>
									<div style={{ marginRight: "20px" }}>
										<p>X coordinate: </p>
										<p>Y coordinate: </p>
										<p>Orientation: </p>
									</div>
									<div>
										<p>{currentPosition[0]}</p>
										<p>{currentPosition[1]}</p>
										<p>{currentOrientation[2]}°</p>
									</div>
								</div>
							</div>

							<div>
								<h3>Speed</h3>
								<div className={styles.InfoArrangement}>
									<div style={{ marginRight: "20px" }}>
										<p>Linear: </p>
										<p>Angular: </p>
									</div>
									<div>
										<p>
											{Math.sqrt(
												linearVelocity.reduce(
													(prev, curr) => prev + curr * curr
												)
											).toFixed(2)}{" "}
											m/s
										</p>
										<p>{angularVelocity[2]} rad/s</p>
									</div>
								</div>
							</div>

							<div>
								<h3>Wheels</h3>
								<div className={styles.InfoArrangement}>
									<div className={styles.InfoArrangement}>
										<div style={{ marginRight: "10px" }}>
											<p>Wheel FL: </p>
											<p>Wheel FR: </p>
											<p>Wheel RL: </p>
											<p>Wheel RR: </p>
										</div>
										<div style={{ marginRight: "30px" }}>
											<p>{wheelsPosition[0]}°</p>
											<p>{wheelsPosition[1]}°</p>
											<p>{wheelsPosition[2]}°</p>
											<p>{wheelsPosition[3]}°</p>
										</div>
									</div>
								</div>
							</div>
							<div className="Image of rover"> </div>
						</div>
						<Timer end={Date.now() + 10000} size={Size.SMALL} />
						<TaskControl task={Task.MANUAL_CONTROL} />
						<GamepadHint />
						<CameraView camera={camera} />
					</div>
				</div>
			</div>
		);
	}
};
