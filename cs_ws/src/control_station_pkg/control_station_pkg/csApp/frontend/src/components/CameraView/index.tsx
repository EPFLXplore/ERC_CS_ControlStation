import styles from "./style.module.sass";
import DefaultImage from "../../assets/images/NoCam.png";

const CameraView = ({ images }: { images: Array<string> }) => {
	console.assert(images.length <= 4, "Only 4 images max are supported");

	if (images.length === 0) {
		console.log("No images");
		return (
			<div className={styles.Container}>
				<img src={DefaultImage} alt="Camera" className={styles.Image} />
			</div>
		);
	} else if (images.length === 1) {
		return (
			<div className={styles.Container}>
				<img src={images[0] ?? DefaultImage} alt="Camera" className={styles.Image} />
			</div>
		);
	} else if (images.length === 2) {
		return (
			<div className={styles.Container}>
				<img src={images[0] ?? DefaultImage} alt="Camera" className={styles.Half} />
				<img src={images[1] ?? DefaultImage} alt="Camera" className={styles.Half} />
			</div>
		);
	} else if (images.length === 3) {
		return (
			<div className={styles.Container}>
				<img src={images[0] ?? DefaultImage} alt="Camera" className={styles.Quarter} />
				<img src={images[1] ?? DefaultImage} alt="Camera" className={styles.Quarter} />
				<img src={images[2] ?? DefaultImage} alt="Camera" className={styles.Quarter} />
			</div>
		);
	} else if (images.length === 4) {
		return (
			<div className={styles.Container}>
				<img src={images[0] ?? DefaultImage} alt="Camera" className={styles.Quarter} />
				<img src={images[1] ?? DefaultImage} alt="Camera" className={styles.Quarter} />
				<img src={images[2] ?? DefaultImage} alt="Camera" className={styles.Quarter} />
				<img src={images[3] ?? DefaultImage} alt="Camera" className={styles.Quarter} />
			</div>
		);
	}

	return (
		<div className={styles.Container}>
			<img src={DefaultImage} alt="Camera" className={styles.Image} />
		</div>
	);
};

export default CameraView;
