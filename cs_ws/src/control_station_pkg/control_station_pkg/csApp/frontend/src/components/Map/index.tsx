import styles from "./style.module.sass";
import map from "../../assets/images/mars_yard_2023.png";
import roverIconImage from "../../assets/images/icons/rover_icon.svg";
import roverGoalIconImage from "../../assets/images/icons/rover_goal.svg";
import roverTempGoalIconImage from "../../assets/images/icons/rover_goal_temp.svg";
import { useState, useEffect, useRef } from "react";
import { roundToTwoDecimals } from "../../utils/maths";

type Point = {
	x: number;
	y: number;
	o: number;
};

type Props = {
	origin: Point;
};

//Dimensions of the map in meters
const YARD_WIDTH_M = 39;
const YARD_LENGTH_M = 49;

var mapCTX: CanvasRenderingContext2D | null;
var mapOrigin: Point;
var pointSpacing: number;

const Map = ({
	origin,
	trajectory,
	goals,
	tempGoal,
	onMapClick,
	onMapDrag,
}: {
	origin: Point;
	trajectory: Point[];
	goals: Point[];
	tempGoal: Point | undefined;
	onMapClick?: (x: number, y: number) => void;
	onMapDrag?: (x: number, y: number) => void;
}) => {
	const canvasRef = useRef<HTMLCanvasElement>(null);
	const [image, setImage] = useState<HTMLImageElement>();
	const [roverIcon, setRoverIcon] = useState<HTMLImageElement>(new Image());
	const [roverGoalIcon, setRoverGoalIcon] = useState<HTMLImageElement>(new Image());
	const [roverTempGoalIcon, setRoverTempGoalIcon] = useState<HTMLImageElement>(new Image());
	const [imageWidth, setImageWidth] = useState<number>(0);
	const [imageHeight, setImageHeight] = useState<number>(0);
	const [mouseDown, setMouseDown] = useState<boolean>(false);

	useEffect(() => {
		// Load the image and set its width and height
		const img = new Image();
		img.onload = () => {
			setImage(img);
			setImageWidth(img.width);
			setImageHeight(img.height);
		};
		img.src = map;

		// Load the rover icon
		const rover = new Image();
		rover.onload = () => {
			setRoverIcon(rover);
		};
		rover.src = roverIconImage;

		// Load the rover goal icon
		const roverGoal = new Image();
		roverGoal.onload = () => {
			setRoverGoalIcon(roverGoal);
		};
		roverGoal.src = roverGoalIconImage;

		// Load the rover temp goal icon
		const roverTempGoal = new Image();
		roverTempGoal.onload = () => {
			setRoverTempGoalIcon(roverTempGoal);
		};
		roverTempGoal.src = roverTempGoalIconImage;
	}, [map]);

	useEffect(() => {
		console.log("use effect draw grid called");
		// Draw the grid on the canvas
		const canvas = canvasRef.current;
		if (canvas && image) {
			const ctx = canvas.getContext("2d");
			mapCTX = ctx;

			if (ctx) {
				drawMap(canvas, ctx, image, origin);
				drawTrajectory(trajectory, roverIcon);
				goals.forEach((goal: Point) => drawGoal(goal, "#0E6655", roverGoalIcon));
				if (tempGoal) drawGoal(tempGoal, "#1F618D", roverTempGoalIcon);
			}
		}
	}, [image, imageWidth, imageHeight, trajectory, goals, tempGoal]);

	return (
		<div className={styles.Map}>
			<div className={styles.MapContainer}>
				<canvas
					ref={canvasRef}
					width={imageWidth}
					height={imageHeight}
					style={{ maxWidth: "100%" }}
					onMouseDown={(e) => {
						setMouseDown(true);
						if (canvasRef.current) {
							const { x, y } = getMousePos(canvasRef.current, e);
							if (onMapClick)
								onMapClick(
									roundToTwoDecimals(x / pointSpacing),
									roundToTwoDecimals(-y / pointSpacing)
								);
						}
					}}
					onMouseUp={(e) => {
						setMouseDown(false);
					}}
					onMouseMove={(e) => {
						if (canvasRef.current && mouseDown) {
							const { x, y } = getMousePos(canvasRef.current, e);
							if (onMapDrag)
								onMapDrag(
									roundToTwoDecimals(x / pointSpacing),
									roundToTwoDecimals(-y / pointSpacing)
								);
						}
					}}
				/>
			</div>
		</div>
	);
};

function getMousePos(canvas: HTMLCanvasElement, evt: any) {
	var rect = canvas.getBoundingClientRect(), // abs. size of element
		scaleX = canvas.width / rect.width, // relationship bitmap vs. element for x
		scaleY = canvas.height / rect.height; // relationship bitmap vs. element for y

	return {
		x: (evt.clientX - rect.left) * scaleX - mapOrigin.x, // scale mouse coordinates after they have
		y: (evt.clientY - rect.top) * scaleY - mapOrigin.y, // been adjusted to be relative to element
	};
}

const rotatePoint = (angle: number, point: number[], x_px: number, y_px: number) => {
	let x = (point[0] - x_px) * Math.cos(angle) - (point[1] - y_px) * Math.sin(angle) + x_px;
	let y = (point[0] - x_px) * Math.sin(angle) + (point[1] - y_px) * Math.cos(angle) + y_px;

	return [x, y];
};

const drawMap = (
	canvas: HTMLCanvasElement,
	ctx: CanvasRenderingContext2D,
	image: CanvasImageSource,
	origin: Point
) => {
	// Clear the canvas
	ctx.clearRect(0, 0, canvas.width, canvas.height);

	// Draw the image as the background
	ctx.drawImage(image, 0, 0, canvas.width, canvas.height);

	// Set the origin of the grid
	const gridOriginX = origin.x;
	const gridOriginY = canvas.height - origin.y;
	mapOrigin = { x: gridOriginX, y: gridOriginY, o: 0 };

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
};

export const drawGoal = (goal: Point, color: string, image?: CanvasImageSource) => {
	if (mapCTX) {
		let yaw: number = goal.o;
		let x_px: number = goal.x * pointSpacing + mapOrigin.x;
		let y_px: number = -goal.y * pointSpacing + mapOrigin.y;

		// Convert the angle from degrees to radians
		let angle = (-yaw * Math.PI) / 180;

		if (image) {
			// Draw the rover
			mapCTX.translate(x_px, y_px);
			mapCTX.rotate(angle);
			mapCTX.drawImage(image, -818 / 32, -818 / 32, 818 / 16, 818 / 16);
			// mapCTX.drawImage(image, -1589 / 40, -1485 / 40, 1589 / 20, 1485 / 20);
			mapCTX.rotate(-angle);
			mapCTX.translate(-x_px, -y_px);
		} else {
			//set the three points of the triangle to be drawn before rotation
			let p1 = [x_px - 20, y_px + 14];
			let p2 = [x_px - 20, y_px - 14];
			let p3 = [x_px + 20, y_px];

			//======= rotation of p1, p2 and p2 around {x_px, y_px} by yaw ========//

			// Define the rotated points of the triangle
			p1 = rotatePoint(angle, p1, x_px, y_px);
			p2 = rotatePoint(angle, p2, x_px, y_px);
			p3 = rotatePoint(angle, p3, x_px, y_px);

			// Begin the path and set the starting point to p1
			mapCTX.beginPath();
			mapCTX.moveTo(p1[0], p1[1]);

			// Draw lines from p1 to p2, p2 to p3, and from p3 back to p1
			mapCTX.lineTo(p2[0], p2[1]);
			mapCTX.lineTo(p3[0], p3[1]);
			mapCTX.lineTo(p1[0], p1[1]);

			// Fill the triangle with the given color
			mapCTX.fillStyle = color;
			mapCTX.fill();
			mapCTX.strokeStyle = "#EAEDED";
			mapCTX.lineWidth = 2;
			mapCTX.stroke();
		}
	}
};

export const drawTrajectory = (points: Point[], icon: CanvasImageSource) => {
	if (mapCTX && points.length > 1) {
		mapCTX.strokeStyle = "red";
		mapCTX.lineWidth = 4;
		mapCTX.beginPath();

		// Calculate the pixel coordinates of the first point
		const startPoint = points[0];
		let startX = startPoint.x * pointSpacing + mapOrigin.x;
		let startY = -startPoint.y * pointSpacing + mapOrigin.y;
		mapCTX.moveTo(startX, startY);

		// Draw lines to connect subsequent points
		for (let i = 1; i < points.length; i++) {
			const currentPoint = points[i];
			let currentX = currentPoint.x * pointSpacing + mapOrigin.x;
			let currentY = -currentPoint.y * pointSpacing + mapOrigin.y;
			mapCTX.lineTo(currentX, currentY);
		}

		// Draw the trajectory lines
		mapCTX.stroke();

		// Call drawGoal on the last point
		drawGoal(points[points.length - 1], "#004466", icon);
	}
};

export default Map;
