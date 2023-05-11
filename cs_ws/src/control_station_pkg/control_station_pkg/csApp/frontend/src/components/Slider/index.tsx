import styles from "./style.module.sass";
import React, { useState, useEffect } from "react";

interface Props {
	label: String;
	initValue: number;
}

export default function App({ label, initValue }: Props) {
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
	}, []);

	return (
		<div className={styles.sliderContainer}>
			<div className={styles.slider}>
				<input type="range" min="1" max="100" value={value} />
			</div>
		</div>
	);
}
