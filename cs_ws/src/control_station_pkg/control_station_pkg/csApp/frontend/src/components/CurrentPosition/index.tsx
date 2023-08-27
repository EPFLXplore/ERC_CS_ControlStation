import { roundToTwoDecimals } from "../../utils/maths";
import styles from "./style.module.sass";

interface Props {
	currentPoint: number[];
}

export default function MyComponent({ currentPoint }: Props) {

	return (
		<div className={styles.container}>
			<div className={styles.containerValues}>
				<div className={styles.coordinates}>{roundToTwoDecimals(currentPoint[0])}, </div>
				<div className={styles.coordinates}>{roundToTwoDecimals(currentPoint[1])}, </div>
				<div className={styles.coordinates}>{roundToTwoDecimals(currentPoint[2])}°</div>
			</div>
		</div>
	);
}
