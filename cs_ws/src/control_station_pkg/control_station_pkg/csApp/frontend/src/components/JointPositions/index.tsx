import Slider from "../../components/Slider";
import { Mode } from "../../utils/mode.type";
import styles from "./style.module.sass";

export default () => {
	return (
		<div className={styles.container}>
			<p className={styles.text}>Joint Positions</p>
			<div className={styles.sliders}>
				<Slider label="Slider 1" />
				<Slider label="Slider 2" />
				<Slider label="Slider 3" />
				<Slider label="Slider 4" />
				<Slider label="Slider 5" />
				<Slider label="Slider 6" />
			</div>
		</div>
	);
};
