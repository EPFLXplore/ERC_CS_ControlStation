import styles from "./style.module.sass";
import { useState } from "react";

const ModeSlider = () => {
	const [activeIndex, setActiveIndex] = useState(0);
	const texts = ["IK", "FK"];

	const handlePrev = () => {
		setActiveIndex((prevIndex) => (prevIndex + texts.length - 1) % texts.length);
	};

	const handleNext = () => {
		setActiveIndex((prevIndex) => (prevIndex + 1) % texts.length);
	};

	return (
		<div className={styles.sliderContainer}>
			<h3 className={styles.sliderTitle}>Mode</h3>
			<div className={styles.sliderArrows}>
				<button onClick={handlePrev}>{"<"}</button>
				<span className={styles.sliderText}>{texts[activeIndex]}</span>
				<button onClick={handleNext}>{">"}</button>
			</div>
		</div>
	);
};

export default ModeSlider;
