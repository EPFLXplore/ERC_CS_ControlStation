import styles from "./style.module.sass";

interface Props {
	x: number;
	y: number;
	o: number;
}

export default function MyComponent({ x, y, o }: Props) {
	return (
		<div className={styles.container}>
			<div className={styles.containerValues}>
				<div className={styles.coordinates}>{x}, </div>
				<div className={styles.coordinates}>{y}, </div>
				<div className={styles.coordinates}>{o}°</div>
			</div>
			<div className={styles.inputContainer}>
				{/* WHAT TO DO WITH THE INPUTTED VALUES? */}
				<div className={styles.finalContainer}>
					X
					<input type="text" id="input-1" name="input-1" />
				</div>
				<div className={styles.finalContainer}>
					Y
					<input type="text" id="input-1" name="input-1" />
				</div>
				<div className={styles.finalContainer}>
					O
					<input type="text" id="input-1" name="input-1" />
				</div>
			</div>
		</div>
	);
}
