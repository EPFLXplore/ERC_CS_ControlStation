import React from "react";
import styles from "./style.module.sass";

const DistanceHint = ({ distance }: { distance: number }) => {
	return (
		<div className={styles.Container}>
			<p className={styles.Text}>Distance to Goal : {distance}cm</p>
		</div>
	);
};

export default DistanceHint;
