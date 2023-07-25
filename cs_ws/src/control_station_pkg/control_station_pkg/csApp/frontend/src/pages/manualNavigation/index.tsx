import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import TaskControl from "../../components/TaskControl";
import { Task } from "../../utils/tasks.type";
import styles from "./style.module.sass";
import { Size } from "../../utils/size.type";
import Timer from "../../components/Timer";
import { useNavigation } from "../../hooks/navigationHooks";
import useCameraManager from "../../hooks/cameraManager";
import { Cameras } from "../../utils/cameras.type";
import CameraView from "../../components/CameraView";
import GamepadHint from "../../components/GamepadHint";
import useCameraSelector from "../../hooks/cameraHooks";
import PageHeader from "../../components/PageHeader";

export default () => {
	const [images, cameras, selectCamera] = useCameraSelector([Cameras.CAM1]);
	const [currentPosition, currentOrientation, wheelsPosition, linearVelocity, angularVelocity] =
		useNavigation();

	return (
		<div className="page center">
			<Background />
			<BackButton />
			<PageHeader
				title="Manual Control"
				settings
				optionTitle="Cameras"
				options={["Camera 1", "Camera 2", "Camera 3"]}
				optionsCallback={selectCamera}
			/>

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
					<GamepadHint mode={"NAV"} />
					<CameraView images={images} />
				</div>
			</div>
		</div>
	);
};
