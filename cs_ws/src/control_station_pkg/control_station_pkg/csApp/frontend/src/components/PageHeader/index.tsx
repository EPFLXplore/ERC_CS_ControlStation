import React from "react";
import styles from "./style.module.sass";
import SettingsButton from "../SettingsButton";
import Multiselect from "multiselect-react-dropdown";
import arrow from "../../assets/images/icons/arrow.svg";

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
	optionsCallback?: (options: string) => void;
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
					<Multiselect
						id="multiselect"
						options={options}
						selectedValues={currentOptions}
						onSelect={(selectedList, selectedItem) => optionsCallback(selectedItem)}
						onRemove={(selectedList, removedItem) => optionsCallback(removedItem)}
						showCheckbox={true}
						showArrow={true}
						hidePlaceholder={true}
						isObject={false}
						selectionLimit={4}
						style={stylesSelector}
						customArrow={<img src={arrow} alt="arrow" />}
					/>
				)}
				{settings && <SettingsButton onClick={settingsCallback} />}
			</div>
		</div>
	);
};

const stylesSelector = {
	optionContainer: {
		// To change css for option container
		border: "2px solid",
	},
	option: {
		// To change css for dropdown options
		color: "white",
		background: "#0D0D0D",
	},
	searchBox: {
		// To change css for search box
		border: "none",
		width: "320px",
	},
	inputField: {
		// To change input field position or margin
		width: "100px",
	},
	chips: {
		// To change css chips(Selected options)
		background: "#8C6746",
		fontSize: "20px",
	},
};

export default PageHeader;
