import React from "react";
import styles from "./style.module.sass";
import image from "../../assets/images/icons/back_button.png";
import { useNavigate } from "react-router-dom";

const BackButton = () => {
	const navigate = useNavigate();

	return (
		<button className={styles.Back} onClick={() => navigate(-1)}>
			<img src={image} className={styles.Image} alt="Background" />
		</button>
	);
};

export default BackButton;
