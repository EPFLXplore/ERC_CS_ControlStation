import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import Map from "../../components/Map";
import Button from "../../components/Button";
import DisplayPosition from "../../components/DisplayPosition";
import TaskControl from "../../components/TaskControl";
import SuppressableCard from "../../components/SuppressableCard";
import { Mode } from "../../utils/mode.type";
import { Task } from "../../utils/tasks.type";
import { Themes } from "../../utils/themes";
import styles from "./style.module.sass";
import { Size } from "../../utils/size.type";

export default ({ mode }: { mode: Mode }) => {
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
	return (
		<div className="page center">
			<Background />
			<BackButton />
			<div className={styles.InfoContainer}>
				<Map />
				<div className={styles.Info}>
					<h2 className={styles.InfoTitle}>{mode} Navigation</h2>

					<div className={styles.ControlsContainer}>
						<h3>Current Position</h3>
						<DisplayPosition x={41} y={15} o={42} /> {/*CONNECT TO BACKEND*/}
						<Button
							text="Add Goal"
							size={Size.SMALL}
							theme={Themes.BROWN}
							onClick={() => {}}
							radius={10}
						/>
						<Button
							text="Reset Goal"
							size={Size.SMALL}
							theme={Themes.BROWN}
							onClick={() => {}}
							radius={10}
						/>
						<h3>Next Goals</h3>
						<SuppressableCard x={42} y={19} o={25} /> {/*CONNECT TO BACKEND*/}
						<SuppressableCard x={24} y={32} o={47} />
						<SuppressableCard x={25} y={56} o={54} />
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
									<p>{WheelFL}°</p>
									<p>{WheelFR}°</p>
									<p>{WheelRL}°</p>
									<p>{WheelRR}°</p>
								</div>
							</div>

							{/* <div className={styles.InfoArrangement}>
								<div style={{ marginRight: "10px" }}>
									<p>Wheel RL: </p>
									<p>Wheel RR: </p>
								</div>
								<div>
									<p>{WheelFL}°</p>
									<p>{WheelFR}°</p>
								</div>
							</div> */}
						</div>
					</div>
					<div className="Image of rover"> </div>
				</div>
				<TaskControl task={Task.NAVIGATION} />
			</div>
		</div>
	);
};
