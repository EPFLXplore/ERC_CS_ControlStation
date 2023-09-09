import { ToggleButton } from "@mui/material";
import hdModeSelect from "../../utils/hdModeSelect";
import styles from "./style.module.sass";
import { useState } from "react";

const ToggleFeature = ({
	title,
	onChange,
}: {
	title: string;
	onChange: (mode: boolean) => void;
}) => {
	return (
		<div className={styles.sliderContainer}>
			<h3 className={styles.sliderTitle}>{title}</h3>
			<label className={styles.switch}>
				<input
					type="checkbox"
					onChange={(e) => {
						onChange(e.target.checked);
					}}
				/>
				<span className={`${styles.slider} ${styles.round}`}></span>
			</label>
		</div>
	);
};

export default ToggleFeature;
