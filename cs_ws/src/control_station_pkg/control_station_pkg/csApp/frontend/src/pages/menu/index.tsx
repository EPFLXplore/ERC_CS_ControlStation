import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import MenuCategory from "../../components/MenuCategory";
import Timer from "../../components/Timer";
import styles from "./style.module.sass";
import NavIcon from "../../assets/images/icons/nav_logo.png";
import ScienceIcon from "../../assets/images/icons/science_logo.png";
import HDIcon from "../../assets/images/icons/handling_device_logo.png";
import InformationIcon from "../../assets/images/icons/information_logo.png";
import useMenuSelector from "../../hooks/menuHooks";
import menuLinks from "./items";

export default () => {
	const [open, setOpen] = useMenuSelector(4);

	return (
		<div className={`page center`}>
			<Background />
			<BackButton />
			<h1 className={styles.MenuTitle}>Astra</h1>
			<div className={styles.Menu}>
				<MenuCategory
					icon={NavIcon}
					name={"Navigation"}
					links={menuLinks.Navigation}
					open={open[0]}
					setOpen={() => setOpen(0)}
				/>
				<MenuCategory
					icon={ScienceIcon}
					name={"Science"}
					links={menuLinks.Science}
					open={open[1]}
					setOpen={() => setOpen(1)}
				/>
				<MenuCategory
					icon={HDIcon}
					name={"Handling Device"}
					links={menuLinks["Handling Device"]}
					open={open[2]}
					setOpen={() => setOpen(2)}
				/>
				<MenuCategory
					icon={InformationIcon}
					name={"Information"}
					links={menuLinks.Information}
					open={open[3]}
					setOpen={() => setOpen(3)}
				/>
			</div>
			<Timer end={Date.now() + 10000} />
		</div>
	);
};
