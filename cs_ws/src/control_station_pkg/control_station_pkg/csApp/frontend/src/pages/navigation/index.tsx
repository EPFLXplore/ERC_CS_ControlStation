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
import { Goal, useGoalTracker } from "../../hooks/navigationHooks";
import { useNavigation } from "../../hooks/navigationHooks";
import { angle, getDistance, roundToTwoDecimals } from "../../utils/maths";
import WheelsIndicator from "../../components/WheelsIndicator";
import PageHeader from "../../components/PageHeader";
import SettingsModal from "../../components/SettingsModal";
import { useState } from "react";

export default ({ mode }: { mode: Exclude<Mode, Mode.MANUAL> }) => {
	const {
		goals,
		addGoal,
		removeGoal,
		resetGoals,
		tempGoal,
		setTempGoal,
		savedGoals,
		setSavedGoals,
	} = useGoalTracker();

	const [
		currentPosition,
		currentOrientation,
		wheelsPosition,
		linearVelocity,
		angularVelocity,
		trajectoryPoints,
	] = useNavigation();

	const [navSettings, setNavlSettings] = useState(false);

	const handleAddGoal = () => {
		// Get the values from the input fields
		const x = parseFloat((document.getElementById("input-x") as HTMLInputElement).value);
		const y = parseFloat((document.getElementById("input-y") as HTMLInputElement).value);
		const o = parseFloat((document.getElementById("input-o") as HTMLInputElement).value);

		if (x.toString() !== "NaN" && y.toString() !== "NaN" && o.toString() !== "NaN") {
			// Create a new goal object and add it to the list of goals
			addGoal(x, y, o);

			// Clear the input fields
			(document.getElementById("input-x") as HTMLInputElement).value = "";
			(document.getElementById("input-y") as HTMLInputElement).value = "";
			(document.getElementById("input-o") as HTMLInputElement).value = "";

			setTempGoal(undefined);
		}
	};

	// TODO Replace all these constants by the call to functions
	const routeLeft = 20;
	const EstimatedTime = "07:00";

	return (
		<div className="page center">
			<Background />
			<BackButton />
			<div className={styles.InfoContainer}>
				<Map
					origin={{
						//SET ORIGIN IN METERS DURING COMPETITION
						x: 753,
						y: 93,
						o: 0,
					}}
					trajectory={trajectoryPoints}
					goals={goals}
					tempGoal={tempGoal}
					savedGoals={savedGoals}
					onMapClick={(x, y) => {
						for (var savedGoal of savedGoals) {
							if (getDistance({ x: x, y: y, o: 0 }, savedGoal) < 0.6) {
								x = savedGoal.x;
								y = savedGoal.y;
							}
						}

						(document.getElementById("input-x") as HTMLInputElement).value =
							x.toString();
						(document.getElementById("input-y") as HTMLInputElement).value =
							y.toString();
						(document.getElementById("input-o") as HTMLInputElement).value =
							(document.getElementById("input-o") as HTMLInputElement).value.length >
							0
								? (document.getElementById("input-o") as HTMLInputElement).value
								: "0";
						const goal: Goal = {
							id: "-1",
							x: x,
							y: y,
							o: parseFloat(
								(document.getElementById("input-o") as HTMLInputElement).value
							),
						};
						setTempGoal(goal);
					}}
					onMapDrag={(x, y) => {
						setTempGoal((prev) => {
							if (!prev) return undefined;
							const o = roundToTwoDecimals(
								(angle(x, y, prev?.x, prev?.y) + 180) % 360
							);
							(document.getElementById("input-o") as HTMLInputElement).value =
								o.toString();
							return {
								...prev,
								o: o,
							};
						});
					}}
				/>
				<div className={styles.Info}>
					<PageHeader
						title="Camera"
						settings
						settingsCallback={() => setNavlSettings(true)}
					/>
					<div className={styles.ControlsContainer}>
						<h3>Current Position</h3>
						<CurrentPosition
							currentPoint={[
								currentPosition[0],
								currentPosition[1],
								currentOrientation[2],
							]}
						/>
						<div className={styles.inputContainer}>
							<div className={styles.finalContainer}>
								X
								<input
									type="number"
									id="input-x"
									name="input-x"
									onInput={(e) => {
										setTempGoal((prev) => {
											if (!prev) {
												return {
													id: "-1",
													x: parseFloat(
														(e.target as HTMLInputElement).value
															.length > 0
															? (e.target as HTMLInputElement).value
															: "0"
													),
													y: 0,
													o: 0,
												};
											} else {
												return {
													...prev,
													x: parseFloat(
														(e.target as HTMLInputElement).value
															.length > 0
															? (e.target as HTMLInputElement).value
															: "0"
													),
												};
											}
										});
									}}
								/>
							</div>
							<div className={styles.finalContainer}>
								Y
								<input
									type="number"
									id="input-y"
									name="input-y"
									onInput={(e) => {
										setTempGoal((prev) => {
											if (!prev) {
												return {
													id: "-1",
													x: 0,
													y: parseFloat(
														(e.target as HTMLInputElement).value
															.length > 0
															? (e.target as HTMLInputElement).value
															: "0"
													),
													o: 0,
												};
											} else {
												return {
													...prev,
													y: parseFloat(
														(e.target as HTMLInputElement).value
															.length > 0
															? (e.target as HTMLInputElement).value
															: "0"
													),
												};
											}
										});
									}}
								/>
							</div>
							<div className={styles.finalContainer}>
								O
								<input
									type="number"
									id="input-o"
									name="input-o"
									onInput={(e) => {
										setTempGoal((prev) => {
											if (!prev) {
												return {
													id: "-1",
													x: 0,
													y: 0,
													o: parseFloat(
														(e.target as HTMLInputElement).value
															.length > 0
															? (e.target as HTMLInputElement).value
															: "0"
													),
												};
											} else {
												return {
													...prev,
													o: parseFloat(
														(e.target as HTMLInputElement).value
															.length > 0
															? (e.target as HTMLInputElement).value
															: "0"
													),
												};
											}
										});
									}}
								/>
							</div>
						</div>
						<div className={styles.buttonGoalContainer}>
							<Button
								text="Go"
								size={Size.SMALL}
								theme={Themes.BROWN}
								onClick={handleAddGoal}
								radius={10}
							/>
							<Button
								text="Cancel"
								size={Size.SMALL}
								theme={Themes.BROWN}
								onClick={() => {
									resetGoals();
									setTempGoal(undefined);
									// Clear the input fields
									(document.getElementById("input-x") as HTMLInputElement).value =
										"";
									(document.getElementById("input-y") as HTMLInputElement).value =
										"";
									(document.getElementById("input-o") as HTMLInputElement).value =
										"";
								}}
								radius={10}
							/>
						</div>
						{goals.length > 0 && <h3 style={{ marginTop: "20px" }}>Next Goals</h3>}
						<div className={styles.buttonGoalsContainer}>
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
			</div>

			<div className={styles.StatsContainer}>
				<div className={styles.InfoText}>
					<div>
						<h3>Target</h3>
						<div className={styles.InfoArrangement}>
							<div className={styles.Infos} style={{ marginRight: "20px" }}>
								<p>Distance to goal: </p>
								<p>Route left: </p>
								<p>Estimated time: </p>
							</div>
							<div className={styles.Infos}>
								<p>
									{goals.length > 0
										? roundToTwoDecimals(
												getDistance(
													{
														x: currentPosition[0],
														y: currentPosition[1],
														o: currentPosition[2],
													},
													goals[0]
												)
										  )
										: "--"}{" "}
									m
								</p>
								<p>{"--"} m</p>
								<p>
									{goals.length > 0
										? roundToTwoDecimals(
												getDistance(
													{
														x: currentPosition[0],
														y: currentPosition[1],
														o: currentPosition[2],
													},
													goals[0]
												) /
													(getSpeedOrDefault(linearVelocity, true) * 60),
												0
										  )
										: "--"}
									{":"}
									{goals.length > 0
										? roundToTwoDecimals(
												getDistance(
													{
														x: currentPosition[0],
														y: currentPosition[1],
														o: currentPosition[2],
													},
													goals[0]
												) / getSpeedOrDefault(linearVelocity, true),
												0
										  ) % 60
										: "--"}
								</p>
							</div>
						</div>
					</div>

					<div>
						<h3>Speed</h3>
						<div className={styles.InfoArrangement}>
							<div className={styles.Infos} style={{ marginRight: "20px" }}>
								<p>Linear: </p>
								<p>Angular: </p>
							</div>
							<div className={styles.Infos}>
								<p>{getSpeedOrDefault(linearVelocity).toFixed(2)} m/s</p>
								<p>{angularVelocity[2]} rad/s</p>
							</div>
						</div>
					</div>

					<div>
						<h3>Wheels</h3>
						<div style={{ display: "flex", flexDirection: "row" }}>
							<div className={styles.InfoArrangement}>
								<div className={styles.Infos} style={{ marginRight: "10px" }}>
									<p>Wheel FL: </p>
									<p>Wheel FR: </p>
									<p>Wheel RL: </p>
									<p>Wheel RR: </p>
								</div>
								<div className={styles.Infos} style={{ marginRight: "30px" }}>
									<p>{wheelsPosition[0]}°</p>
									<p>{wheelsPosition[1]}°</p>
									<p>{wheelsPosition[2]}°</p>
									<p>{wheelsPosition[3]}°</p>
								</div>
							</div>
							<div className="Image of rover" style={{ marginTop: "20px" }}>
								<WheelsIndicator wheelsOrientation={wheelsPosition} />
							</div>
						</div>
					</div>
				</div>
				<Timer end={Date.now() + 10000} size={Size.SMALL} />
				<TaskControl task={Task.NAVIGATION} />
			</div>
			<SettingsModal open={navSettings} onClose={() => setNavlSettings(false)}>
				{}
			</SettingsModal>
		</div>
	);
};

const getSpeedOrDefault = (linearVelocity: number[], isNonNull = false) => {
	const defaultSpeed = 0.3;

	if (linearVelocity.length !== 3) return isNonNull ? defaultSpeed : 0;
	if (linearVelocity.some((value) => isNaN(value))) return isNonNull ? defaultSpeed : 0;
	if (linearVelocity.every((value) => value === 0)) return isNonNull ? defaultSpeed : 0;
	return Math.sqrt(linearVelocity.reduce((prev, curr) => prev + curr * curr));
};
