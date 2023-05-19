import React, { useCallback, useState } from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import Map from "../../components/Map";
import Button from "../../components/Button";
import CurrentPosition from "../../components/CurrentPosition";
import TaskControl from "../../components/TaskControl";
import SuppressableCard from "../../components/SuppressableCard";
import { Mode } from "../../utils/mode.type";
import { Task } from "../../utils/tasks.type";
import { Themes } from "../../utils/themes";
import styles from "./style.module.sass";
import { Size } from "../../utils/size.type";
import Timer from "../../components/Timer";
import { useGoalTracker } from "../../hooks/navigationHooks";
import { useNavigation } from "../../hooks/navigationHooks";
import useCameraManager from "../../hooks/cameraManager";
import { Cameras } from "../../utils/cameras.type";
import CameraView from "../../components/CameraView";

export default ({ mode }: { mode: Mode }) => {
	const [camera, selectCamera] = useCameraManager(Cameras.CAM1);
	const { goals, addGoal, removeGoal, resetGoals } = useGoalTracker();

	const [currentPosition, wheelsPosition] = useNavigation();

	const handleAddGoal = () => {
		// Get the values from the input fields
		const x = parseInt((document.getElementById("input-x") as HTMLInputElement).value, 10);
		const y = parseInt((document.getElementById("input-y") as HTMLInputElement).value, 10);
		const o = parseInt((document.getElementById("input-o") as HTMLInputElement).value, 10);

		// Create a new goal object and add it to the list of goals
		addGoal(x, y, o);

		// Clear the input fields
		(document.getElementById("input-x") as HTMLInputElement).value = "";
		(document.getElementById("input-y") as HTMLInputElement).value = "";
		(document.getElementById("input-o") as HTMLInputElement).value = "";
	};

	// TODO Replace all these constants by the call to functions
	const distance = 15;
	const routeLeft = 20;
	const EstimatedTime = "07:00";
	const linear = 5;
	const angular = 3;
	const WheelFL = 10;
	const WheelFR = 10;
	const WheelRL = 0;
	const WheelRR = 0;

	switch (mode) {
		case Mode.AUTONOMOUS:
		case Mode.SEMI_AUTONOMOUS:
			return (
				<div className="page center">
					<Background />
					<BackButton />
					<div className={styles.InfoContainer}>
						<Map
							origin={{
								//SET ORIGIN IN METERS DURING COMPETITION
								x: 300,
								y: 200,
								o: 0,
							}}
						/>
						<div className={styles.Info}>
							<h2 className={styles.InfoTitle}>{mode} Navigation</h2>
							<div className={styles.ControlsContainer}>
								<h3>Current Position</h3>
								<CurrentPosition currentPoint={currentPosition} />
								<div className={styles.inputContainer}>
									<div className={styles.finalContainer}>
										X
										<input type="number" id="input-x" name="input-x" />
									</div>
									<div className={styles.finalContainer}>
										Y
										<input type="number" id="input-y" name="input-y" />
									</div>
									<div className={styles.finalContainer}>
										O
										<input type="number" id="input-o" name="input-o" />
									</div>
								</div>
								<Button
									text="Add Goal"
									size={Size.SMALL}
									theme={Themes.BROWN}
									onClick={handleAddGoal}
									radius={10}
								/>
								<Button
									text="Reset Goals"
									size={Size.SMALL}
									theme={Themes.BROWN}
									onClick={resetGoals}
									radius={10}
								/>
								{goals.length > 0 && <h3>Next Goals</h3>}
								{goals.map((goal, index) => (
									<SuppressableCard
										key={goal.id}
										x={goal.x}
										y={goal.y}
										o={goal.o}
										removeGoal={() => removeGoal(goal.id)}
									/>
								))}
							</div>
						</div>
					</div>

					<div className={styles.StatsContainer}>
						<div className={styles.InfoText}>
							<div>
								<h3>Target</h3>
								<div className={styles.InfoArrangement}>
									<div style={{ marginRight: "20px" }}>
										<p>Distance to goal: </p>
										<p>Route left: </p>
										<p>Estimated time: </p>
									</div>
									<div>
										<p>{distance} m</p>
										<p>{routeLeft} m</p>
										<p>{EstimatedTime}</p>
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
										<p>{linear} m/s</p>
										<p>{angular} rad/s</p>
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
											<p>{wheelsPosition.fl}°</p>
											<p>{wheelsPosition.fr}°</p>
											<p>{wheelsPosition.rl}°</p>
											<p>{wheelsPosition.rr}°</p>
										</div>
									</div>
								</div>
							</div>
							<div className="Image of rover"> </div>
						</div>
						<Timer end={Date.now() + 10000} size={Size.SMALL} />
						<TaskControl task={Task.NAVIGATION} />
					</div>
				</div>
			);
		case Mode.MANUAL:
			return (
				<div className="page center">
					<Background />
					<BackButton />

					<div className={styles.CamSpace}>
						<div className={styles.StatsContainer}>
							<div className={styles.InfoText}>
								<div>
									<h3>Target</h3>
									<div className={styles.InfoArrangement}>
										<div style={{ marginRight: "20px" }}>
											<p>Distance to goal: </p>
											<p>Route left: </p>
											<p>Estimated time: </p>
										</div>
										<div>
											<p>{distance} m</p>
											<p>{routeLeft} m</p>
											<p>{EstimatedTime}</p>
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
											<p>{linear} m/s</p>
											<p>{angular} rad/s</p>
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
												<p>{wheelsPosition.fl}°</p>
												<p>{wheelsPosition.fr}°</p>
												<p>{wheelsPosition.rl}°</p>
												<p>{wheelsPosition.rr}°</p>
											</div>
										</div>
									</div>
								</div>
								<div className="Image of rover"> </div>
							</div>
							<Timer end={Date.now() + 10000} size={Size.SMALL} />
							<TaskControl task={Task.NAVIGATION} />
							<CameraView camera={camera} />
						</div>
					</div>
				</div>
			);
	}
};
