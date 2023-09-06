import React from "react";
import styles from "./style.module.sass";
import { roundToTwoDecimals } from "../../utils/maths";

const VoltmeterValue = ({ value }: { value: number }) => {
	return (
		<div className={styles.Container}>
			<p className={styles.Text}>
				<b>Voltmeter</b> : {roundToTwoDecimals(value)}V
			</p>
		</div>
	);
};

export default VoltmeterValue;
