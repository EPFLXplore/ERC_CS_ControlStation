import React from "react";
import { Size } from "../../utils/size.type";
import { Themes } from "../../utils/themes";
import Button from "../Button";
import styles from "./style.module.sass";
import FSMControl from "../../utils/FSMControl";
import { Task } from "../../utils/tasks.type";

export default ({ task }: { task: Task }) => {
	return (
		<div className={styles.TaskControl}>
			<Button
				text="Launch"
				size={Size.SMALL}
				theme={Themes.BROWN}
				onClick={() => FSMControl.launchTask(task)}
				radius={10}
			/>
			<Button
				text="Abort"
				size={Size.SMALL}
				theme={Themes.BROWN}
				onClick={() => FSMControl.abortTask(task)}
				radius={10}
			/>
			<Button
				text="Wait"
				size={Size.SMALL}
				theme={Themes.BROWN}
				onClick={() => FSMControl.waitTask(task)}
				radius={10}
			/>
			<Button
				text="Resume"
				size={Size.SMALL}
				theme={Themes.BROWN}
				onClick={() => FSMControl.resumeTask(task)}
				radius={10}
			/>
		</div>
	);
};
