import React from "react";
import styles from "./style.module.sass";
import SettingsButton from "../SettingsButton";

const PageHeader = ({
	title,
	optionTitle,
	currentOptions,
	options = [],
	optionsCallback = (option) => {},
	settings = false,
	settingsCallback = () => {},
	multiselect = false,
}: {
	title: string;
	optionTitle?: string;
	currentOptions?: Array<string>;
	options?: string[];
	optionsCallback?: (option: string) => void;
	settings?: boolean;
	settingsCallback?: () => void;
	multiselect?: boolean;
}) => {
	// if (optionTitle || options || currentOption)
	// 	assert(
	// 		optionTitle && options && currentOption,
	// 		"If you want to use options, you must provide optionTitle, options and currentOption"
	// 	);

	console.log(currentOptions);
	console.log(options);

	return (
		<div className={styles.Container}>
			<h2 className={styles.Title}>{title}</h2>
			<div className={styles.PageOptions}>
				{options.length > 0 && (
					<select
						className={styles.Select}
						onChange={(e) => optionsCallback(e.target.value)}
					>
						{options.map((option, i) => (
							<option
								className={`${styles.Options} ${
									currentOptions?.includes(option) ? styles.Selected : ""
								}`}
								key={option}
								value={option}
							>
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
