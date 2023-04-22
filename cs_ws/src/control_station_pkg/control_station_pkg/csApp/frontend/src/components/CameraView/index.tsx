import React, { useEffect } from "react";
import styles from "./style.module.sass";
import DefaultImage from "../../assets/images/NoCam.png";
import useCameraSelector from "../../hooks/cameraHooks";
import { Cameras } from "../../utils/cameras.type";

const CameraView = ({ camera }: { camera: Cameras }) => {
	const [image] = useCameraSelector(camera);

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
