import React from "react";
import styles from "./style.module.sass";
import { Goal } from "../../hooks/navigationHooks";

type DispatchType =
	| React.Dispatch<React.SetStateAction<Goal[]>>
	| React.Dispatch<React.SetStateAction<Goal | undefined>>;

function GoalInputBox({
	setGoal,
	isSavedGoal,
	children,
	name,
}: {
	setGoal: DispatchType;
	isSavedGoal: boolean;
	children: React.ReactNode[];
	name?: string;
}) {
	return (
		<div className={styles.container}>
			<div className={styles.inputContainer}>
				{isSavedGoal && (
					<>
						<div className={styles.finalContainer}>
							ID
							<input type="text" id={"input-id" + name} name="input-id" />
						</div>
						<div className={styles.finalContainer}>
							X
							<input type="number" id={"input-sx" + name} name="input-sx" />
						</div>
						<div className={styles.finalContainer}>
							Y
							<input type="number" id={"input-sy" + name} name="input-sy" />
						</div>
						<div className={styles.finalContainer}>
							O
							<input type="number" id={"input-so" + name} name="input-so" />
						</div>
					</>
				)}
				{!isSavedGoal && (
					<>
						<div className={styles.finalContainer}>
							X
							<input
								type="number"
								id={"input-x" + name}
								name="input-x"
								onInput={(e) => {
									setGoal((prev: any) => {
										if (!prev) {
											return {
												id: "-1",
												x: parseFloat(
													(e.target as HTMLInputElement).value.length > 0
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
													(e.target as HTMLInputElement).value.length > 0
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
								id={"input-y" + name}
								name="input-y"
								onInput={(e) => {
									setGoal((prev: any) => {
										if (!prev) {
											return {
												id: "-1",
												x: 0,
												y: parseFloat(
													(e.target as HTMLInputElement).value.length > 0
														? (e.target as HTMLInputElement).value
														: "0"
												),
												o: 0,
											};
										} else {
											return {
												...prev,
												y: parseFloat(
													(e.target as HTMLInputElement).value.length > 0
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
								id={"input-o" + name}
								name="input-o"
								onInput={(e) => {
									setGoal((prev: any) => {
										if (!prev) {
											return {
												id: "-1",
												x: 0,
												y: 0,
												o: parseFloat(
													(e.target as HTMLInputElement).value.length > 0
														? (e.target as HTMLInputElement).value
														: "0"
												),
											};
										} else {
											return {
												...prev,
												o: parseFloat(
													(e.target as HTMLInputElement).value.length > 0
														? (e.target as HTMLInputElement).value
														: "0"
												),
											};
										}
									});
								}}
							/>
						</div>
					</>
				)}
			</div>
			<div className={styles.buttonGoalContainer}>
				{children}
				</div>
		</div>
	);
}

export default GoalInputBox;
