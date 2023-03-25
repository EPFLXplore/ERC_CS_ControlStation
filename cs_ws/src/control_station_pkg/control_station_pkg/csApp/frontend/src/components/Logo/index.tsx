import React from "react";
import styles from "./style.module.sass";
import logoLarge from "../../assets/images/logos/logo_XPlore.png";
import logoSmall from "../../assets/images/logos/short_logo_XPlore.png";
import { Size } from "../../utils/size.type";

const Logo = ({ size }: { size: Size }) => {
	switch (size) {
		case Size.SMALL:
			return (
				<div className={styles.LogoSmall}>
					<img src={logoSmall} className={styles.Image} alt="Logo Xplore" />
				</div>
			);
		case Size.MEDIUM:
			return (
				<div className={styles.LogoMedium}>
					<img src={logoSmall} className={styles.Image} alt="Logo Xplore" />
				</div>
			);
		case Size.LARGE:
			return (
				<div className={styles.LogoLarge}>
					<img src={logoLarge} className={styles.Image} alt="Logo Xplore" />
				</div>
			);
		default:
			return (
				<div className={styles.LogoSmall}>
					<img src={logoSmall} className={styles.Image} alt="Logo Xplore" />
				</div>
			);
	}
};

export default Logo;
