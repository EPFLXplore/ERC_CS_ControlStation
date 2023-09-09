import React, { useState } from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import JointPositions from "../../components/JointPositions";
import styles from "./style.module.sass";
import GamepadHint from "../../components/GamepadHint";
import PageHeader from "../../components/PageHeader";
import CameraView from "../../components/CameraView";
import { Cameras } from "../../utils/cameras.type";
import Timer from "../../components/Timer";
import { Size } from "../../utils/size.type";
import ModeSlider from "../../components/ModeSlider";
import JointSpeed from "../../components/JointSpeed";
import useHandlingDevice from "../../hooks/handlingDeviceHooks";
import JointCurrents from "../../components/JointCurrents";
import { Task } from "../../utils/tasks.type";
import TaskControl from "../../components/TaskControl";
import { useNavigation } from "../../hooks/navigationHooks";
import ModeSelector from "../../components/ModeSelector";
import { useLocation } from "react-router-dom";
import useCameraSelector from "../../hooks/cameraHooks";
import hdModeSelect from "../../utils/hdModeSelect";
import ToggleFeature from "../../components/ToggleFeature";
import VoltmeterSlider from "../../components/VoltmeterSlider";
import VoltmeterValue from "../../components/VoltmeterValue";
import SettingsModal from "../../components/SettingsModal";

function useQuery() {
	const { search } = useLocation();

	return React.useMemo(() => new URLSearchParams(search), [search]);
}

export default () => {
	const [images, cameras, selectCamera, flushCameras, rotateCams, setRotateCams] =
		useCameraSelector([
			Cameras.CAM1,
			// Cameras.CAM2,
			// Cameras.CAM3,
			// Cameras.CAM4,
		]);
	const [
		jointPositions,
		jointVelocities,
		jointCurrents,
		detectedTags,
		taskSuccess,
		voltmeter,
		openVoltmeter,
	] = useHandlingDevice();
	const [currentPosition, currentOrientation, wheelsPosition, linearVelocity, angularVelocity] =
		useNavigation();
	const defaultMode = useQuery().get("defaultMode");

	const [mode, setMode] = useState(
		defaultMode === "nav" ? Task.NAVIGATION : Task.HANDLING_DEVICE
	);

	const [manualSettings, setManualSettings] = useState(false);

	return (
		<div className="page">
			<CameraView images={images} rotate={rotateCams} setRotateCams={setRotateCams} />
			<BackButton onGoBack={() => flushCameras()} />
			<PageHeader
				title="Manual Control"
				settings
				settingsCallback={() => {
					setManualSettings(true);
				}}
				optionTitle="Cameras"
				options={[
					"Camera 1",
					// "Camera 2",
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
			<div className={styles.Subheader}>
				<ModeSelector mode={mode} callback={setMode} />
			</div>
			{/* <DistanceHint distance={10} /> */}

			{mode === Task.HANDLING_DEVICE && (
				<div className={styles.jointContainer}>
					<JointPositions positions={jointPositions} />
					<JointSpeed speeds={jointVelocities} />
					<JointCurrents currents={jointCurrents} />
					<VoltmeterValue value={voltmeter} />
				</div>
			)}

			{mode === Task.HANDLING_DEVICE && (
				<div className={styles.globalContainer}>
					{/* <ModeSlider
						name="Arm Mode"
						mode={["IK", "FK"]}
						functionTrigger={() => hdModeSelect(0)}
					/>
					<VoltmeterSlider initValue={0} onValueChange={openVoltmeter} /> */}
					<ToggleFeature
						title="Voltmeter"
						onChange={(m) => {
							console.log(m);
							//"bool -> Voltmeter"
						}}
					/>
					<ToggleFeature
						title="LED Drone"
						onChange={(m) => {
							console.log(m);
						}}
					/>
					<TaskControl task={Task.MANUAL_CONTROL} />
				</div>
			)}

			{mode === Task.NAVIGATION && (
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
						<div className={styles.globalContainer}>
							<ModeSlider
								name="Nav Mode"
								mode={["NORMAL", "BASIC"]}
								functionTrigger={() => hdModeSelect(0)}
							/>
							<TaskControl task={Task.MANUAL_CONTROL} />
						</div>
					</div>
				</div>
			)}

			<Timer end={Date.now() + 10000} size={Size.SMALL} />
			<GamepadHint
				mode={mode === Task.NAVIGATION ? "NAV" : "HD"}
				selectorCallback={() =>
					setMode((oldMode) =>
						oldMode === Task.NAVIGATION ? Task.HANDLING_DEVICE : Task.NAVIGATION
					)
				}
				visible
			/>
			<Background />
			<SettingsModal open={manualSettings} onClose={() => setManualSettings(false)}>
				{}
			</SettingsModal>
		</div>
	);
};

////////////////////////// OLD CODE //////////////////////////

// if (mode === Task.HANDLING_DEVICE) {
// 	return (
// 		<div className="page">
// 			<Background />
// 			<BackButton />
// 			<PageHeader
// 				title="Manual Control (HD)"
// 				settings
// 				optionTitle="Cameras"
// 				options={[
// 					"Camera 1",
// 					"Camera 2",
// 					"Camera 3",
// 					"Camera 4",
// 					"Camera 5",
// 					"Camera 6",
// 					"Camera Gripper",
// 				]}
// 				optionsCallback={selectCamera}
// 				currentOptions={cameras.map((camera) =>
// 					camera < 6 ? "Camera " + (camera + 1) : "Camera Gripper"
// 				)}
// 			/>
// 			<div className={styles.Subheader}>
// 				<ManualModeSelector mode={Task.HANDLING_DEVICE} callback={setMode} />
// 			</div>
// 			{/* <DistanceHint distance={10} /> */}

// 			<div className={styles.jointContainer}>
// 				<JointPositions positions={jointPositions} />
// 				<JointSpeed speeds={jointVelocities} />
// 				<JointCurrents currents={jointCurrents} />
// 			</div>

// 			<div className={styles.globalContainer}>
// 				<ModeSlider />
// 				<TaskControl task={Task.MANUAL_CONTROL} />
// 			</div>

// 			<Timer end={Date.now() + 10000} size={Size.SMALL} />
// 			<GamepadHint mode="HD" selectorCallback={() => setMode(Task.NAVIGATION)} visible />
// 			<CameraView images={images} />
// 		</div>
// 	);
// } else {
// 	return (
// 		<div className="page center">
// 			<Background />
// 			<BackButton />
// 			<PageHeader
// 				title="Manual Control (NAV)"
// 				settings
// 				optionTitle="Cameras"
// 				options={[
// 					"Camera 1",
// 					"Camera 2",
// 					"Camera 3",
// 					"Camera 4",
// 					"Camera 5",
// 					"Camera 6",
// 					"Camera Gripper",
// 				]}
// 				optionsCallback={selectCamera}
// 				currentOptions={cameras.map((camera) =>
// 					camera < 6 ? "Camera " + (camera + 1) : "Camera Gripper"
// 				)}
// 			/>
// 			<div className={styles.Subheader}>
// 				<ManualModeSelector mode={Task.NAVIGATION} callback={setMode} />
// 			</div>

// 			<div className={styles.CamSpace}>
// 				<div className={styles.StatsContainer}>
// 					<div className={styles.InfoText}>
// 						<div>
// 							<h3>Current position</h3>
// 							<div className={styles.InfoArrangement}>
// 								<div style={{ marginRight: "20px" }}>
// 									<p>X coordinate: </p>
// 									<p>Y coordinate: </p>
// 									<p>Orientation: </p>
// 								</div>
// 								<div>
// 									<p>{currentPosition[0]}</p>
// 									<p>{currentPosition[1]}</p>
// 									<p>{currentOrientation[2]}°</p>
// 								</div>
// 							</div>
// 						</div>

// 						<div>
// 							<h3>Speed</h3>
// 							<div className={styles.InfoArrangement}>
// 								<div style={{ marginRight: "20px" }}>
// 									<p>Linear: </p>
// 									<p>Angular: </p>
// 								</div>
// 								<div>
// 									<p>
// 										{Math.sqrt(
// 											linearVelocity.reduce(
// 												(prev, curr) => prev + curr * curr
// 											)
// 										).toFixed(2)}{" "}
// 										m/s
// 									</p>
// 									<p>{angularVelocity[2]} rad/s</p>
// 								</div>
// 							</div>
// 						</div>

// 						<div>
// 							<h3>Wheels</h3>
// 							<div className={styles.InfoArrangement}>
// 								<div className={styles.InfoArrangement}>
// 									<div style={{ marginRight: "10px" }}>
// 										<p>Wheel FL: </p>
// 										<p>Wheel FR: </p>
// 										<p>Wheel RL: </p>
// 										<p>Wheel RR: </p>
// 									</div>
// 									<div style={{ marginRight: "30px" }}>
// 										<p>{wheelsPosition[0]}°</p>
// 										<p>{wheelsPosition[1]}°</p>
// 										<p>{wheelsPosition[2]}°</p>
// 										<p>{wheelsPosition[3]}°</p>
// 									</div>
// 								</div>
// 							</div>
// 						</div>
// 						<div className="Image of rover"> </div>
// 					</div>
// 					<Timer end={Date.now() + 10000} size={Size.SMALL} />
// 					<TaskControl task={Task.MANUAL_CONTROL} />
// 					<GamepadHint
// 						mode="NAV"
// 						selectorCallback={() => setMode(Task.HANDLING_DEVICE)}
// 						visible
// 					/>
// 					<CameraView images={images} />
// 				</div>
// 			</div>
// 		</div>
// 	);
// }
