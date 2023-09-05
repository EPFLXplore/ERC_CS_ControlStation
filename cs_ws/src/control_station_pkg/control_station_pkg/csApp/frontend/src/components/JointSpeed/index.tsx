import { roundToTwoDecimals } from "../../utils/maths";
import styles from "./style.module.sass";

interface Props {
	speeds: number[];
}

export default ({ speeds }: Props) => {
	return (
		<div className={styles.container}>
			<h3 className={styles.text}>Joint Speed</h3>
			<p className={styles.text}>{roundToTwoDecimals(speeds[0])} °/s</p>
			<p className={styles.text}>{roundToTwoDecimals(speeds[1])} °/s</p>
			<p className={styles.text}>{roundToTwoDecimals(speeds[2])} °/s</p>
			<p className={styles.text}>{roundToTwoDecimals(speeds[3])} °/s</p>
			<p className={styles.text}>{roundToTwoDecimals(speeds[4])} °/s</p>
			<p className={styles.text}>{roundToTwoDecimals(speeds[5])} °/s</p>
		</div>
	);
};
