import { Task } from "../../utils/tasks.type";
import styles from "./style.module.sass";
import { useState } from "react";

const defaultTexts = ["HD", "NAV"];

const ModeSelector = ({
	mode,
	callback,
	texts = defaultTexts,
}: {
	mode: Task;
	callback: (mode: Task) => void;
	texts?: string[];
}) => {
	const modes = [Task.HANDLING_DEVICE, Task.NAVIGATION];

	const _setActiveIndex = (mode: number) => {
		callback(modes[mode]);
	};

	const handlePrev = () => {
		const newMode = (modes.indexOf(mode) - 1 + modes.length) % texts.length;
		_setActiveIndex(newMode);
	};

	const handleNext = () => {
		const newMode = (modes.indexOf(mode) + 1 + modes.length) % texts.length;
		_setActiveIndex(newMode);
	};

	return (
		<div className={styles.sliderContainer}>
			<h3 className={styles.sliderTitle}>Controls</h3>
			<div className={styles.sliderArrows}>
				<button onClick={handlePrev}>{"<"}</button>
				<span className={styles.sliderText}>{texts[modes.indexOf(mode)]}</span>
				<button onClick={handleNext}>{">"}</button>
			</div>
		</div>
	);
};

export default ModeSelector;
