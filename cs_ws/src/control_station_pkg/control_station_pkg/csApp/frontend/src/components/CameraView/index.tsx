import styles from "./style.module.sass";
import DefaultImage from "../../assets/images/NoCam.png";

const CameraView = ({
	images,
	rotate = [false],
	setRotateCams,
}: {
	images: Array<string>;
	rotate?: boolean[];
	setRotateCams?: (rotate: boolean[]) => void;
}) => {
	console.assert(images.length <= 4, "Only 4 images max are supported");
	console.log(setRotateCams);

	if (images.length === 0) {
		console.log("No images");
		return (
			<div className={styles.Container}>
				<img
					src={DefaultImage}
					alt="Camera"
					className={rotate[0] ? styles.RotatedImage : styles.Image}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([!rotate[0]]);
						}
					}}
				/>
			</div>
		);
	} else if (images.length === 1) {
		return (
			<div className={styles.Container}>
				<img
					src={images[0] ?? DefaultImage}
					alt="Camera"
					className={rotate[0] ? styles.RotatedImage : styles.Image}
					onDoubleClick={() => {
						console.log("Clicked");
						if (setRotateCams) {
							setRotateCams([!rotate[0]]);
						}
					}}
				/>
			</div>
		);
	} else if (images.length === 2) {
		return (
			<div className={styles.Container}>
				<img
					src={images[0] ?? DefaultImage}
					alt="Camera"
					className={rotate[0] ? styles.RotatedHalf : styles.Half}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([!rotate[0], rotate[1]]);
						}
					}}
				/>
				<img
					src={images[1] ?? DefaultImage}
					alt="Camera"
					className={rotate[1] ? styles.RotatedHalf : styles.Half}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([rotate[0], !rotate[1]]);
						}
					}}
				/>
			</div>
		);
	} else if (images.length === 3) {
		return (
			<div className={styles.Container}>
				<img
					src={images[0] ?? DefaultImage}
					alt="Camera"
					className={rotate[0] ? styles.RotatedQuarter : styles.Quarter}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([!rotate[0], rotate[1], rotate[2]]);
						}
					}}
				/>
				<img
					src={images[1] ?? DefaultImage}
					alt="Camera"
					className={rotate[1] ? styles.RotatedQuarter : styles.Quarter}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([rotate[0], !rotate[1], rotate[2]]);
						}
					}}
				/>
				<img
					src={images[2] ?? DefaultImage}
					alt="Camera"
					className={rotate[2] ? styles.RotatedQuarter : styles.Quarter}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([rotate[0], rotate[1], !rotate[2]]);
						}
					}}
				/>
			</div>
		);
	} else if (images.length >= 4) {
		return (
			<div className={styles.Container}>
				<img
					src={images[0] ?? DefaultImage}
					alt="Camera"
					className={rotate[0] ? styles.RotatedQuarter : styles.Quarter}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([!rotate[0], rotate[1], rotate[2], rotate[3]]);
						}
					}}
				/>
				<img
					src={images[1] ?? DefaultImage}
					alt="Camera"
					className={rotate[1] ? styles.RotatedQuarter : styles.Quarter}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([rotate[0], !rotate[1], rotate[2], rotate[3]]);
						}
					}}
				/>
				<img
					src={images[2] ?? DefaultImage}
					alt="Camera"
					className={rotate[2] ? styles.RotatedQuarter : styles.Quarter}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([rotate[0], rotate[1], !rotate[2], rotate[3]]);
						}
					}}
				/>
				<img
					src={images[3] ?? DefaultImage}
					alt="Camera"
					className={rotate[3] ? styles.RotatedQuarter : styles.Quarter}
					onDoubleClick={() => {
						if (setRotateCams) {
							setRotateCams([rotate[0], rotate[1], rotate[2], !rotate[3]]);
						}
					}}
				/>
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
