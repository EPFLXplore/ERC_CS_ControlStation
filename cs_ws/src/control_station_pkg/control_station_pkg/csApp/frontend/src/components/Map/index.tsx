import styles from "./style.module.sass";
import map from "../../assets/images/mars_yard_2022.png";
import React, { useState, useEffect, useRef } from "react";

type Point = {
	x: number;
	y: number;
};

type Props = {
	origin: Point;
};

var mapCTX: CanvasRenderingContext2D | null;
var mapOrigin: Point;
const pointSpacing: number = 30; // Change this to adjust the spacing between points of the grid

const Map: React.FC<Props> = ({ origin }) => {
	const canvasRef = useRef<HTMLCanvasElement>(null);
	const [image, setImage] = useState<HTMLImageElement>();
	const [imageWidth, setImageWidth] = useState<number>(0);
	const [imageHeight, setImageHeight] = useState<number>(0);

	useEffect(() => {
		// Load the image and set its width and height
		const img = new Image();
		img.onload = () => {
			setImage(img);
			setImageWidth(img.width);
			setImageHeight(img.height);
		};
		img.src = map;
	}, [map]);

	useEffect(() => {
		// Draw the grid on the canvas
		const canvas = canvasRef.current;
		if (canvas && image) {
			const ctx = canvas.getContext("2d");
			mapCTX = ctx;

			if (ctx) {
				// Clear the canvas
				ctx.clearRect(0, 0, canvas.width, canvas.height);

				// Draw the image as the background
				ctx.drawImage(image, 0, 0, canvas.width, canvas.height);

				// Set the origin of the grid
				const gridOriginX = origin.x;
				const gridOriginY = canvas.height - origin.y;
				mapOrigin = { x: gridOriginX, y: gridOriginY };

				const fontSize = 16;
				ctx.font = `${fontSize}px Arial`;
				ctx.strokeStyle = "white";

				// Draw the x-axis
				ctx.beginPath();
				ctx.strokeStyle = "white";
				ctx.moveTo(gridOriginX, 0);
				ctx.lineTo(gridOriginX, canvas.height);
				ctx.stroke();
				for (let x = gridOriginX + pointSpacing; x <= canvas.width; x += pointSpacing) {
					ctx.beginPath();
					ctx.moveTo(x, gridOriginY - 5);
					ctx.lineTo(x, gridOriginY + 5);
					ctx.stroke();
					const label = `${(x - gridOriginX) / pointSpacing}`;
					const labelWidth = ctx.measureText(label).width;
					ctx.fillStyle = "white";
					ctx.fillText(label, x - labelWidth / 2, gridOriginY + fontSize + 5);
				}
				for (let x = gridOriginX - pointSpacing; x >= 0; x -= pointSpacing) {
					ctx.beginPath();
					ctx.moveTo(x, gridOriginY - 5);
					ctx.lineTo(x, gridOriginY + 5);
					ctx.stroke();
					const label = `${(x - gridOriginX) / pointSpacing}`;
					const labelWidth = ctx.measureText(label).width;
					ctx.fillStyle = "white";
					ctx.fillText(label, x - labelWidth / 2, gridOriginY + fontSize + 5);
				}

				// Draw the y-axis
				ctx.beginPath();
				ctx.moveTo(0, gridOriginY);
				ctx.lineTo(canvas.width, gridOriginY);
				ctx.stroke();
				for (let y = gridOriginY - pointSpacing; y >= 0; y -= pointSpacing) {
					ctx.beginPath();
					ctx.moveTo(gridOriginX - 5, y);
					ctx.lineTo(gridOriginX + 5, y);
					ctx.stroke();
					const label = `${(gridOriginY - y) / pointSpacing}`;
					const labelWidth = ctx.measureText(label).width;
					ctx.fillStyle = "white";
					ctx.fillText(label, gridOriginX - labelWidth - 5, y + fontSize / 2);
				}
				for (let y = gridOriginY + pointSpacing; y <= canvas.height; y += pointSpacing) {
					ctx.beginPath();
					ctx.moveTo(gridOriginX - 5, y);
					ctx.lineTo(gridOriginX + 5, y);
					ctx.stroke();
					const label = `${(gridOriginY - y) / pointSpacing}`;
					const labelWidth = ctx.measureText(label).width;
					ctx.fillStyle = "white";
					ctx.fillText(label, gridOriginX - labelWidth - 5, y + fontSize / 2);
				}

				// Draw the grid points
				ctx.fillStyle = "white";
				for (let x = gridOriginX; x <= canvas.width; x += pointSpacing) {
					for (let y = gridOriginY; y >= 0; y -= pointSpacing) {
						ctx.beginPath();
						ctx.arc(x, y, 2, 0, 2 * Math.PI);
						ctx.fill();
					}
					for (let y = gridOriginY; y <= canvas.height; y += pointSpacing) {
						ctx.beginPath();
						ctx.arc(x, y, 2, 0, 2 * Math.PI);
						ctx.fill();
					}
				}
				for (let x = gridOriginX; x >= 0; x -= pointSpacing) {
					for (let y = gridOriginY; y >= 0; y -= pointSpacing) {
						ctx.beginPath();
						ctx.arc(x, y, 2, 0, 2 * Math.PI);
						ctx.fill();
					}
					for (let y = gridOriginY; y <= canvas.height; y += pointSpacing) {
						ctx.beginPath();
						ctx.arc(x, y, 2, 0, 2 * Math.PI);
						ctx.fill();
					}
				}
			}
		}
	}, [origin, image, imageWidth, imageHeight]);

	return (
		<div className={styles.Map}>
			<div className={styles.MapContainer}>
				<canvas
					ref={canvasRef}
					width={imageWidth}
					height={imageHeight}
					style={{ maxWidth: "100%" }}
				/>
			</div>
		</div>
	);
};

export const drawPoint = (x: number, y: number) => {
	if (mapCTX) {
		mapCTX.fillStyle = "red";
		mapCTX.beginPath();
		mapCTX.arc(
			x * pointSpacing + mapOrigin.x,
			-y * pointSpacing + mapOrigin.y,
			5,
			0,
			2 * Math.PI
		);
		mapCTX.fill();
	}
};

export default Map;
