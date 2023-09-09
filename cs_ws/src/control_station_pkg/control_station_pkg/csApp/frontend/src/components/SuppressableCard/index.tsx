import { useState } from "react";
import { FaTimes } from "react-icons/fa";
import styles from "./style.module.sass";

interface Props {
	key: string;
	x: number;
	y: number;
	o: number;
	removeGoal: (index: string) => void;
}

function Card({ key, x, y, o, removeGoal }: Props) {
	const [visible, setVisible] = useState(true);

	const handleDismiss = () => {
		setVisible(false);
		removeGoal(key);
	};

	return (
		<>
			{visible && (
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
		</>
	);
}

export default Card;
