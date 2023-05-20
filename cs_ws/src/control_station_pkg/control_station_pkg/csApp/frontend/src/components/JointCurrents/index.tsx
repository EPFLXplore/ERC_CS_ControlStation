import styles from "./style.module.sass";

interface Props {
	currents: number[];
}

export default ({ currents }: Props) => {
	return (
		<div className={styles.container}>
			<h3 className={styles.text}>Joint Currents</h3>
			<p className={styles.text}>{currents[0]} mA</p>
			<p className={styles.text}>{currents[1]} mA</p>
			<p className={styles.text}>{currents[2]} mA</p>
			<p className={styles.text}>{currents[3]} mA</p>
			<p className={styles.text}>{currents[4]} mA</p>
			<p className={styles.text}>{currents[5]} mA</p>
		</div>
	);
};
