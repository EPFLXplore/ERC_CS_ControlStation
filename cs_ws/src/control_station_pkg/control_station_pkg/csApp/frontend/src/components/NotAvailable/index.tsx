import React from "react";
import DoNotDisturbIcon from "@mui/icons-material/DoNotDisturb";
import styles from "./style.module.sass";

export default () => {
	return (
		<div className={styles.container}>
			<DoNotDisturbIcon className={styles.icon} />
			<p className={styles.text}>Not Available</p>
			<p className={styles.description}>
				Someone is already using a feature that prevents your request.
			</p>
		</div>
	);
};
