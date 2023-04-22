import React from "react";
import styles from "./style.module.sass";
import image from "../../assets/images/icons/settings_button.png";

const SettingsButton = ({ onClick }: { onClick: () => void }) => {
	return (
		<button className={styles.Button} onClick={onClick}>
			<img src={image} className={styles.Image} alt="Background" />
		</button>
	);
};

export default SettingsButton;
