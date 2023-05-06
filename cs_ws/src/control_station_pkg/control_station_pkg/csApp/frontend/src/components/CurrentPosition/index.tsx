import styles from "./style.module.sass";

interface Props {
	currentX: number;
	currentY: number;
	currentO: number;
}

export default function MyComponent({ currentX, currentY, currentO }: Props) {
	return (
		<div className={styles.container}>
			<div className={styles.containerValues}>
				<div className={styles.coordinates}>{currentX}, </div>
				<div className={styles.coordinates}>{currentY}, </div>
				<div className={styles.coordinates}>{currentO}°</div>
			</div>
		</div>
	);
}
