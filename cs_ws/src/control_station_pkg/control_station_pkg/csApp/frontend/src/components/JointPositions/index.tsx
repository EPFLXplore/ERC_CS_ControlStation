import Slider from "../../components/Slider";
import { Mode } from "../../utils/mode.type";
import styles from "./style.module.sass";

export default () => {
	return (
		<div className={styles.container}>
			<h3 className={styles.text}>Joint Positions</h3>
			<Slider label="Slider 1" initValue={20} />
			<Slider label="Slider 2" initValue={45} />
			<Slider label="Slider 3" initValue={38} />
			<Slider label="Slider 4" initValue={2} />
			<Slider label="Slider 5" initValue={12} />
			<Slider label="Slider 6" initValue={87} />
		</div>
	);
};
