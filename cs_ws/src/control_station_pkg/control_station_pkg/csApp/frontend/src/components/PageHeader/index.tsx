import React from "react";
import styles from "./style.module.sass";
import SettingsButton from "../SettingsButton";

const PageHeader = ({
	title,
	optionTitle,
	currentOption,
	options = [],
	optionsCallback = (option) => {},
	settings = false,
	settingsCallback = () => {},
}: {
	title: string;
	optionTitle?: string;
	currentOption?: string;
	options?: string[];
	optionsCallback?: (option: string) => void;
	settings?: boolean;
	settingsCallback?: () => void;
}) => {
	// if (optionTitle || options || currentOption)
	// 	assert(
	// 		optionTitle && options && currentOption,
	// 		"If you want to use options, you must provide optionTitle, options and currentOption"
	// 	);

	return (
		<div className={styles.Container}>
			<h2 className={styles.Title}>{title}</h2>
			<div className={styles.PageOptions}>
				{options.length > 0 && (
					<select
						className={styles.Select}
						value={currentOption}
						onChange={(e) => optionsCallback(e.target.value)}
					>
						{options.map((option) => (
							<option className={styles.Options} key={option} value={option}>
								{option}
							</option>
						))}
					</select>
				)}
				{settings && <SettingsButton onClick={settingsCallback} />}
			</div>
		</div>
	);
};

export default PageHeader;
