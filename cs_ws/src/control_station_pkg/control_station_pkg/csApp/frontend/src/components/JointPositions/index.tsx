import Slider from "../../components/Slider";
import { Mode } from "../../utils/mode.type";
import styles from "./style.module.sass";

export default ({ positions }: { positions: number[] }) => {
	return (
		<div className={styles.container}>
			<h3 className={styles.text}>Joint Positions</h3>
			<Slider label="Slider 1" initValue={positions[0]} min={-1.5 * Math.PI} max={1.5*Math.PI} />
			<Slider label="Slider 2" initValue={positions[1]} min={- Math.PI} max={Math.PI / 2}/>
			<Slider label="Slider 3" initValue={positions[2]} min={- Math.PI / 4} max={ Math.PI / 4}/>
			<Slider label="Slider 4" initValue={positions[3]} min={- 2 * Math.PI} max={2 * Math.PI}/>
			<Slider label="Slider 5" initValue={positions[4]} min={- Math.PI / 2} max={Math.PI / 2}/>
			<Slider label="Slider 6" initValue={positions[5]} min={- Math.PI} max={Math.PI}/>
		</div>
	);
};
