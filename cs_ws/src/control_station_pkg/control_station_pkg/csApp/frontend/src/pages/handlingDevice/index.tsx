import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import Slider from "../../components/Slider";
import JointPositions from "../../components/JointPositions";
import { Mode } from "../../utils/mode.type";
import styles from "./style.module.sass";

export default ({ mode }: { mode: Exclude<Mode, Mode.SEMI_AUTONOMOUS> }) => {
	return (
		<div className="page">
			<Background />
			<BackButton />
			<JointPositions />
		</div>
	);
};
