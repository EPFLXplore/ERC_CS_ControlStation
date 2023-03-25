import React from "react";
import { Size } from "../../utils/size.type";
import { Themes } from "../../utils/themes";
import styles from "./style.module.sass";

export default ({
	size = Size.SMALL,
	radius = 15,
	icon,
	text,
	onClick,
	outline = false,
	theme = Themes.LIGHT,
	disabled = false,
}: {
	size?: Size;
	radius?: number;
	icon?: JSX.Element;
	text: string;
	onClick: () => void;
	dark?: boolean;
	outline?: boolean;
	theme?: Themes;
	disabled?: boolean;
}) => {
	//Set the size of the button
	const style = {
		borderRadius: `${radius}px`,
	};

	//Set the theme of the button
	let themeStyle: string;
	switch (theme) {
		case Themes.LIGHT:
			themeStyle = styles.light;
			break;
		case Themes.DARK:
			themeStyle = styles.dark;
			break;
		case Themes.BROWN:
			themeStyle = styles.brown;
			break;
		case Themes.GREY:
			themeStyle = styles.grey;
			break;
		default:
			themeStyle = styles.light;
			break;
	}

	let sizeStyle: string;
	switch (size) {
		case Size.SMALL:
			sizeStyle = styles.small;
			break;
		case Size.MEDIUM:
			sizeStyle = styles.medium;
			break;
		case Size.LARGE:
			sizeStyle = styles.large;
			break;
		default:
			sizeStyle = styles.small;
			break;
	}

	if (icon) {
		return (
			<button
				style={style}
				className={`${styles.button} ${themeStyle} ${
					outline ? styles.outline : styles.plain
				} ${disabled ? styles.disabled : ""}`}
				onClick={() => {
					if (!disabled) onClick();
				}}
			>
				<div className={styles.iconContainer}>
					{React.cloneElement(icon, { className: styles.icon })}
				</div>
				<p className={`${styles.text} ${sizeStyle}`}>{text}</p>
			</button>
		);
	} else {
		return (
			<button
				style={style}
				className={`${styles.button} ${themeStyle} ${
					outline ? styles.outline : styles.plain
				} ${disabled ? styles.disabled : ""}`}
				onClick={() => {
					if (!disabled) onClick();
				}}
			>
				<p className={`${styles.text} ${sizeStyle}`}>{text}</p>
			</button>
		);
	}
};
