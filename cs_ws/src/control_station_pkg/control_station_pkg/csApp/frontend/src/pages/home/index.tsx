import React from "react";
import { useNavigate } from "react-router-dom";
import Background from "../../components/Background";
import Button from "../../components/Button";
import Logo from "../../components/Logo";
import { Size } from "../../utils/size.type";
import { Themes } from "../../utils/themes";
import styles from "./style.module.sass";
import MenuBookRoundedIcon from "@mui/icons-material/MenuBookRounded";
import AddToDriveRoundedIcon from "@mui/icons-material/AddToDriveRounded";

export default () => {
	const navigate = useNavigate();

	return (
		<div className="page">
			<Background />
			<div className={styles.header}>
				<Logo size={Size.LARGE} />
			</div>
			<div className={styles.body}>
				<Button
					size={Size.LARGE}
					radius={20}
					text="Start Rover"
					theme={Themes.DARK}
					outline
					onClick={() => navigate("/menu")}
				/>
			</div>
			<div className={styles.footer}>
				<Button
					size={Size.MEDIUM}
					radius={15}
					text="Documentation"
					theme={Themes.DARK}
					icon={<MenuBookRoundedIcon />}
					onClick={() =>
						window.open(
							"https://hospitable-taste-374.notion.site/Xplore-Wiki-for-Software-Engineers-and-Roboticists-5615d07f70814ab0b3901beb31920236",
							"_blank"
						)
					}
				/>
				<Button
					size={Size.MEDIUM}
					radius={15}
					text="Drive"
					theme={Themes.DARK}
					icon={<AddToDriveRoundedIcon />}
					onClick={() =>
						window.open(
							"https://drive.google.com/drive/folders/0AEpe4eawL6pdUk9PVA",
							"_blank"
						)
					}
				/>
			</div>
		</div>
	);
};
