import React from "react";
import styles from "./style.module.sass";

function SettingsModal({
	open = false,
	title = "Settings",
	children,
	onClose,
}: {
	open?: boolean;
	title?: string;
	children: React.ReactNode[];
	onClose?: () => void;
}) {
	if (!open) return <></>;

	return (
		<div className={styles.Background} onClick={onClose}>
			<div className={styles.Modal}>
				<h1>{title}</h1>
				<div className={styles.CloseButton} onClick={onClose}></div>
				<div className={styles.Container}>{children}</div>
			</div>
		</div>
	);
}

export default SettingsModal;
