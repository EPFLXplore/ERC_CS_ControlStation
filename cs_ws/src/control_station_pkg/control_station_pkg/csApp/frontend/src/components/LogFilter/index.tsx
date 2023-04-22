import React, { useState } from "react";
import { Themes } from "../../utils/themes";
import styles from "./style.module.sass";

export default ({
	name,
	onActivate,
	onDisactivate,
	color,
}: {
	name: string;
	onActivate: () => void;
	onDisactivate: () => void;
	color: Omit<Themes, Themes.DARK | Themes.LIGHT>;
}) => {
	const [active, setActive] = useState(true);

	const getColorType = (type: Omit<Themes, Themes.DARK | Themes.LIGHT>) => {
		switch (type) {
			case Themes.GREY:
				return styles.Grey;
			case Themes.BROWN:
				return styles.Brown;
			case Themes.ORANGE:
				return styles.Orange;
			default:
				return styles.Red;
		}
	};

	const handleClick = () => {
		if (active) {
			onDisactivate();
		} else {
			onActivate();
		}
		setActive(!active);
	};

	return (
		<button
			className={`${getColorType(color)} ${active ? styles.Filled : styles.Outlined} ${
				styles.Filter
			}`}
			onClick={handleClick}
		>
			{name}
		</button>
	);
};
