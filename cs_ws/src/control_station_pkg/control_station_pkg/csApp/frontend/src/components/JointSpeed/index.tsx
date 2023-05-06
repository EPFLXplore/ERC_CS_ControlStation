import styles from "./style.module.sass";

interface Props {
	joint1: number;
	joint2: number;
	joint3: number;
	joint4: number;
	joint5: number;
	joint6: number;
}

export default ({ joint1, joint2, joint3, joint4, joint5, joint6 }: Props) => {
	return (
		<div className={styles.container}>
			<h3 className={styles.text}>Joint Speed</h3>
			<p className={styles.text}>{joint1}</p>
			<p className={styles.text}>{joint2}</p>
			<p className={styles.text}>{joint3}</p>
			<p className={styles.text}>{joint4}</p>
			<p className={styles.text}>{joint5}</p>
			<p className={styles.text}>{joint6}</p>
		</div>
	);
};
