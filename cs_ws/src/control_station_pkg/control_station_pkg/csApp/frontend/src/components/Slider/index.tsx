import styles from "./style.module.sass";
import React, { useState, useEffect } from "react";

interface Props {
	label: String;
}

export default function App({ label }: Props) {
	const [value, onChange] = useState(1);
	useEffect(() => {
		const ele = document.querySelector(".buble");
		if (ele instanceof HTMLElement) {
			ele.style.top = `${Number(value / 4)}px`;
		}
	});
	return (
		<div className={styles.sliderParent}>
			<input
				type="range"
				min="1"
				max="100"
				value={value}
				onChange={({ target: { value: radius } }) => {
					onChange(parseInt(radius));
				}}
			/>
		</div>
	);
}
