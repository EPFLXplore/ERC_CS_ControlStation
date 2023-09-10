import { useState } from "react";
import { FaTimes } from "react-icons/fa";
import styles from "./style.module.sass";

interface Props {
	isSavedGoal: boolean;
	key: string;
	id: string;
	x: number;
	y: number;
	o: number;
	removeGoal: (index: string) => void;
}

function Card({ isSavedGoal, key, id, x, y, o, removeGoal }: Props) {
	const [visible, setVisible] = useState(true);

	const handleDismiss = () => {
		setVisible(false);
		removeGoal(key);
	};

	return (
		<>
			{visible && !isSavedGoal && (
				<div className={styles.cardContainer}>
					<div className={styles.closeButton}>
						<FaTimes
							onClick={handleDismiss}
							style={{
								color: "white",
								cursor: "pointer",
								fontSize: 10,
							}}
						/>
					</div>
					<div>
						<p className={styles.cardText}>
							({x}, {y}, {o}°)
						</p>
					</div>
				</div>
			)}

			{visible && isSavedGoal && (
				<span
					style={{
						display: "flex",
						flexDirection: "row",
						justifyContent: "space-between",
						alignItems: "center",
						width: "100%",
						padding: "0 20% 0 20%",
					}}
				>
					<div className={styles.idContainer}>
						<p className={styles.idText}>{id}</p>
					</div>
					<div className={styles.cardContainer}>
						<div className={styles.closeButton}>
							<FaTimes
								onClick={handleDismiss}
								style={{
									color: "white",
									cursor: "pointer",
									fontSize: 10,
								}}
							/>
						</div>
						<p className={styles.cardText}>
							({x}, {y}, {o}°)
						</p>
					</div>
				</span>
			)}
		</>
	);
}

export default Card;
