import styles from "./style.module.sass";

const ToggleFeature = ({
	title,
	onChange,
	value
}: {
	title: string;
	onChange: (mode: boolean) => void;
	value?: boolean;
}) => {
	if(value !== undefined) {
		return (
			<div className={styles.sliderContainer}>
				<h3 className={styles.sliderTitle}>{title}</h3>
				<label className={styles.switch}>
					<input
						type="checkbox"
						onChange={(e) => {
							onChange(e.target.checked);
						}}
						checked={value}
					/>
					<span className={`${styles.slider} ${styles.round}`}></span>
				</label>
			</div>
		);
	} else {
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
	}
	
};

export default ToggleFeature;
