import styles from "./style.module.sass";
import React, { useState, useEffect } from "react";

interface Props {
	label: String;
	initValue: number;
	min?: number;
	max?: number;
}

export default function App({ label, initValue, min = 1, max = 100 }: Props) {
	const [value, setValue] = useState(1);

	useEffect(() => {
		const ele = document.querySelector(".buble");
		if (ele instanceof HTMLElement) {
			ele.style.top = `${Number(value / 4)}px`;
		}
	});

	// update the value as needed
	useEffect(() => {
		setValue(initValue); // the value to the given parameter
	}, [initValue]);

	return (
		<div className={styles.sliderContainer}>
			<div className={styles.slider}>
				<input type="range" min={min} max={max} value={value} />
			</div>
		</div>
	);
}
