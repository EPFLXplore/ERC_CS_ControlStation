import hdModeSelect from "../../utils/hdModeSelect";
import styles from "./style.module.sass";
import { useState } from "react";

const ModeSlider = () => {
	const [activeIndex, setActiveIndex] = useState(0);
	const texts = ["IK", "FK", "SA"];

	const _setActiveIndex = (mode: number) => {
		hdModeSelect(mode);
		setActiveIndex(mode);
	};

	const handlePrev = () => {
		const newMode = (activeIndex - 1 + 3) % texts.length;
		_setActiveIndex(newMode);
	};

	const handleNext = () => {
		const newMode = (activeIndex + 1 + 3) % texts.length;
		_setActiveIndex(newMode);
	};

	return (
		<div className={styles.sliderContainer}>
			<h3 className={styles.sliderTitle}>Arm Mode</h3>
			<div className={styles.sliderArrows}>
				<button onClick={handlePrev}>{"<"}</button>
				<span className={styles.sliderText}>{texts[activeIndex]}</span>
				<button onClick={handleNext}>{">"}</button>
			</div>
		</div>
	);
};

export default ModeSlider;
