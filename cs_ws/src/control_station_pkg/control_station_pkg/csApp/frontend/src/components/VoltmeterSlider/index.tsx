import styles from "./style.module.sass";
import React, { useState, useEffect } from "react";

interface Props {
	initValue: number;
	onValueChange: (value: number) => void;
}

export default function VoltmeterSlider({ initValue, onValueChange }: Props) {
	const [value, setValue] = useState(initValue);

	useEffect(() => {
		const ele = document.querySelector(".buble");
		if (ele instanceof HTMLElement) {
			ele.style.top = `${Number(value / 4)}px`;
		}
	});

	return (
		<div className={styles.sliderContainer}>
			<h3 className={styles.sliderTitle}>Voltmeter Control</h3>
			<div className={styles.slider}>
				<input
					type="range"
					min="1"
					max="180"
					defaultValue={initValue}
					onChange={(e) => onValueChange(parseInt(e.target.value))}
				/>
			</div>
		</div>
	);
}
