import React from "react";
import labItem from "../../assets/images/icons/lab_items.png";
import styles from "./style.module.sass";

export default () => {
	return (
		<div className={styles.container}>
			<img src={labItem} alt="labItem" className={styles.icon} />
			<p className={styles.text}>In Progress</p>
		</div>
	);
};
