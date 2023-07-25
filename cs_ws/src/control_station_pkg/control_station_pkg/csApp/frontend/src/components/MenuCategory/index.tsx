import React from "react";
import { Link } from "../../utils/link.type";
import styles from "./style.module.sass";

export default ({
	icon,
	name,
	links,
	open = true,
	setOpen,
}: {
	icon: string;
	name: string;
	links: Array<Link>;
	open?: boolean;
	setOpen: (open: boolean) => void;
}) => {
	if (links.length < 2) {
		return (
			<a className={`${styles.MenuCard} ${styles.Focusable}`} href={links[0].url}>
				<div className={styles.MenuCardIcon}>
					<img src={icon} alt={name} className={styles.MenuCardIcon} />
				</div>
				<h2 className={styles.MenuCardName}>{name}</h2>
			</a>
		);
	} else if (open) {
		return (
			<div className={styles.MenuCard} onClick={() => setOpen(false)}>
				<div className={styles.MenuCardIcon}>
					<img src={icon} alt={name} className={styles.MenuCardIcon} />
				</div>
				<div className={styles.MenuCardLinks}>
					<h2 className={styles.MenuCardTitle}>{name}</h2>
					{links.map((link, i) => (
						<a key={i} href={link.url} className={styles.Link}>
							{link.name}
						</a>
					))}
				</div>
			</div>
		);
	} else {
		return (
			<button
				className={`${styles.MenuCard} ${styles.Focusable}`}
				onClick={() => setOpen(true)}
			>
				<div className={styles.MenuCardIcon}>
					<img src={icon} alt={name} className={styles.MenuCardIcon} />
				</div>
				<h2 className={styles.MenuCardName}>{name}</h2>
			</button>
		);
	}
};
