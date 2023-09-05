import { roundToTwoDecimals } from "../../utils/maths";
import styles from "./style.module.sass";

interface Props {
	currents: number[];
}

export default ({ currents }: Props) => {
	return (
		<div className={styles.container}>
			<h3 className={styles.text}>Joint Currents</h3>
			<p className={styles.text}>{roundToTwoDecimals(currents[0], 3)} mA</p>
			<p className={styles.text}>{roundToTwoDecimals(currents[1], 3)} mA</p>
			<p className={styles.text}>{roundToTwoDecimals(currents[2], 3)} mA</p>
			<p className={styles.text}>{roundToTwoDecimals(currents[3], 3)} mA</p>
			<p className={styles.text}>{roundToTwoDecimals(currents[4], 3)} mA</p>
			<p className={styles.text}>{roundToTwoDecimals(currents[5], 3)} mA</p>
		</div>
	);
};
