import styles from "./style.module.sass";
import DefaultImage from "../../assets/images/NoCam.png";

const CameraView = ({ image }: { image: string }) => {

	return (
		<div
			style={{
				backgroundImage: `url(${DefaultImage})`,
				backgroundRepeat: "no-repeat",
				backgroundPosition: "center",
				backgroundSize: "cover",
			}}
			className={styles.Container}
		>
			{image && <img src={image} alt="Camera" className={styles.Image} />}
		</div>
	);
};

export default CameraView;
