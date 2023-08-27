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

export default ({ mode }: { mode: Exclude<Mode, Mode.MANUAL> }) => {
	const { goals, addGoal, removeGoal, resetGoals, tempGoal, setTempGoal } = useGoalTracker();

	const [
		currentPosition,
		currentOrientation,
		wheelsPosition,
		linearVelocity,
		angularVelocity,
		trajectoryPoints,
	] = useNavigation();

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

			setTempGoal([]);
		}
	};

	// TODO Replace all these constants by the call to functions
	const distance = 15;
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
					tempGoals={tempGoal}
					onMapClick={(x, y) => {
						(document.getElementById("input-x") as HTMLInputElement).value =
							x.toString();
						(document.getElementById("input-y") as HTMLInputElement).value =
							y.toString();
						(document.getElementById("input-o") as HTMLInputElement).value = "0";
						const goal: Goal = { id: -1, x: x, y: y, o: 0 };
						setTempGoal((prev) => [goal]);
					}}
				/>
				<div className={styles.Info}>
					<h2 className={styles.InfoTitle}>{mode} Navigation</h2>
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
								<input type="number" id="input-x" name="input-x" />
							</div>
							<div className={styles.finalContainer}>
								Y
								<input type="number" id="input-y" name="input-y" />
							</div>
							<div className={styles.finalContainer}>
								O
								<input
									type="number"
									id="input-o"
									name="input-o"
									onInput={(e) => {
										setTempGoal((prev) => [
											{
												...prev[0],
												o: parseInt(
													(e.target as HTMLInputElement).value.length > 0
														? (e.target as HTMLInputElement).value
														: "0",
													10
												),
											},
										]);
									}}
								/>
							</div>
						</div>
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
								setTempGoal([]);
								// Clear the input fields
								(document.getElementById("input-x") as HTMLInputElement).value = "";
								(document.getElementById("input-y") as HTMLInputElement).value = "";
								(document.getElementById("input-o") as HTMLInputElement).value = "";
							}}
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
								<p>
									{Math.sqrt(
										linearVelocity.reduce((prev, curr) => prev + curr * curr)
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
							<div className="Image of rover"> </div>
						</div>
					</div>
				</div>
				<Timer end={Date.now() + 10000} size={Size.SMALL} />
				<TaskControl task={Task.NAVIGATION} />
			</div>
		</div>
	);
};
