import styles from "./style.module.sass";

type Point = {
	x: number;
	y: number;
	o: number;
};

interface Props {
	currentPoint: Point;
}

export default function MyComponent({ currentPoint }: Props) {
	return (
		<div className={styles.container}>
			<div className={styles.containerValues}>
				<div className={styles.coordinates}>{currentPoint.x}, </div>
				<div className={styles.coordinates}>{currentPoint.y}, </div>
				<div className={styles.coordinates}>{currentPoint.o}°</div>
			</div>
		</div>
	);
}
