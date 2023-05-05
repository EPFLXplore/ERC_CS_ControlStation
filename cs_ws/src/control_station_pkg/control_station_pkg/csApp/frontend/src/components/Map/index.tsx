import styles from "./style.module.sass";
import map from "../../assets/images/mars_yard_2022.png";
import React, { useState, useEffect, useRef } from "react";

type Point = {
	x: number;
	y: number;
};

type Goal = {
	x: number;
	y: number;
	o: number;
};

type Props = {
	origin: Point;
};

//Dimensions of the map in meters
const YARD_WIDTH_M = 39;
const YARD_LENGTH_M = 47;

var mapCTX: CanvasRenderingContext2D | null;
var mapOrigin: Point;
var pointSpacing: number;

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

				const fontSize = 12;
				ctx.font = `${fontSize}px Arial`;
				ctx.strokeStyle = "white";

				pointSpacing = Math.floor(canvas.width / YARD_LENGTH_M);

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
						ctx.arc(x, y, 1.5, 0, 2 * Math.PI);
						ctx.fill();
					}
					for (let y = gridOriginY; y <= canvas.height; y += pointSpacing) {
						ctx.beginPath();
						ctx.arc(x, y, 1.5, 0, 2 * Math.PI);
						ctx.fill();
					}
				}
				for (let x = gridOriginX; x >= 0; x -= pointSpacing) {
					for (let y = gridOriginY; y >= 0; y -= pointSpacing) {
						ctx.beginPath();
						ctx.arc(x, y, 1.5, 0, 2 * Math.PI);
						ctx.fill();
					}
					for (let y = gridOriginY; y <= canvas.height; y += pointSpacing) {
						ctx.beginPath();
						ctx.arc(x, y, 1.5, 0, 2 * Math.PI);
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

export const drawPoint = (goal: Goal) => {
	if (mapCTX) {
		let sideLength: number = 10;

		let yaw: number = goal.o;
		let x_px: number = goal.x * pointSpacing + mapOrigin.x;
		let y_px: number = -goal.y * pointSpacing + mapOrigin.y;

		let p1 = [x_px, y_px + sideLength];
		let p2 = [x_px, y_px - sideLength];
		let p3 = [x_px + 2 * sideLength, y_px];

		//======= rotation of p1 and p2 around {x_px, y_px} by yaw ========//

		// Convert the angle from degrees to radians
		let angle = (-yaw * Math.PI) / 180;

		// Rotate p1 around (x_px, y_px)
		let x1 = (p1[0] - x_px) * Math.cos(angle) - (p1[1] - y_px) * Math.sin(angle) + x_px;
		let y1 = (p1[0] - x_px) * Math.sin(angle) + (p1[1] - y_px) * Math.cos(angle) + y_px;

		// Rotate p2 around (x_px, y_px)
		let x2 = (p2[0] - x_px) * Math.cos(angle) - (p2[1] - y_px) * Math.sin(angle) + x_px;
		let y2 = (p2[0] - x_px) * Math.sin(angle) + (p2[1] - y_px) * Math.cos(angle) + y_px;

		// Rotate p3 around (x_px, y_px)
		let x3 = (p3[0] - x_px) * Math.cos(angle) - (p3[1] - y_px) * Math.sin(angle) + x_px;
		let y3 = (p3[0] - x_px) * Math.sin(angle) + (p3[1] - y_px) * Math.cos(angle) + y_px;

		// Define the points of the triangle
		p1 = [x1, y1];
		p2 = [x2, y2];
		p3 = [x3, y3];

		// Begin the path and set the starting point to p1
		mapCTX.beginPath();
		mapCTX.moveTo(p1[0], p1[1]);

		// Draw lines from p1 to p2, p2 to p3, and from p3 back to p1
		mapCTX.lineTo(p2[0], p2[1]);
		mapCTX.lineTo(p3[0], p3[1]);
		mapCTX.lineTo(p1[0], p1[1]);

		// Fill the triangle with the given color
		mapCTX.fillStyle = "red";
		mapCTX.fill();
	}
};

const drawPointFromNav = (goal: Goal) => {
	if (mapCTX) {
		let p1: [number, number] = [0, 0];
		let p2: [number, number] = [0, 0];
		let sideLength: number = 20;

		let yaw: number = goal.o;
		let x_px: number = goal.x * pointSpacing + mapOrigin.x;
		let y_px: number = -goal.y * pointSpacing + mapOrigin.y;

		// top point of the triangle
		// here and later on, adding x_px and y_px is done to reposition the triangle correctly on the map (shifting)
		mapCTX.moveTo(sideLength * Math.cos(yaw) + x_px, sideLength * Math.sin(yaw) + y_px);

		// p1 and p2 are the points of the two other angles of the triangle
		if (Math.abs(yaw) == Math.PI / 2) {
			p1 = [x_px - 5, y_px];
			p2 = [x_px + 5, y_px];
		} else {
			let tan: number = Math.round(Math.tan(yaw) * 100) / 100; // two decimal precision
			let factor: number = Math.round((5 / Math.sqrt(tan * tan + 1)) * 100) / 100;

			p1 = [factor * -tan + x_px, factor + y_px];
			p2 = [factor * tan + x_px, -factor + y_px];
		}

		// draw triangle
		// JS draws two lines from the moveTo() method (see above) to the points p1 and p2 and then fills up the drawn object
		mapCTX.lineTo(p1[0], p1[1]);
		mapCTX.lineTo(p2[0], p2[1]);
		mapCTX.fill();

		// draw new segment of the path
		mapCTX.lineTo(x_px, y_px);
		mapCTX.strokeStyle = "#008000";
		mapCTX.fillStyle = "#008000";
		mapCTX.stroke();
	}
};

export default Map;
