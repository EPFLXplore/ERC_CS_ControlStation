import React, { useRef } from "react";
import styles from "./style.module.sass";
import map from "../../assets/images/mars_yard_2022.png";

const width_map = 950;
const height_map = 788.3;
const YARD_WIDTH_M = 39;
const YARD_LENGTH_M = 47;

const X_START_PX = 324;
const Y_START_PX = 711;

const Map = () => {
	const canvasRef = useRef<HTMLCanvasElement>(null);

	React.useEffect(() => {
		if (canvasRef.current) {
			drawMap(canvasRef.current);
		}
	}, []);

	return (
		<div className={styles.Map}>
			<div className={styles.MapContainer}>
				<canvas ref={canvasRef} className={styles.MapDisplay} width="1400" height="810" />
			</div>
		</div>
	);
};

//Solution: Have two canvas maybe
/** Have two canvas :
 * One where you draw the image and everything around it
 * One where we draw the quadrillage et le repère
 * modulariser ça pour que ce soit plus compréhensible
 */

const drawMap = (canvas: HTMLCanvasElement) => {
	const ctx = canvas.getContext("2d");
	if (!ctx) return;

	const img = new Image();
	img.src = map;

	img.onload = () => {
		ctx.drawImage(img, 0, 0, width_map, height_map); //Draw the image in the right place

		// starting point (light green rectangle)
		ctx.fillStyle = "rgba(0, 255, 0, 0.5)";
		ctx.fillRect(X_START_PX, Y_START_PX, 10, 10); // x, y, width, height
		// AR tag
		const Wt_X = X_START_PX + (0 * width_map) / YARD_WIDTH_M;
		const Wt_Y = Y_START_PX - (9 * height_map) / YARD_LENGTH_M;
		ctx.fillStyle = "rgba(0, 0, 255, 0.5)";
		ctx.fillRect(Wt_X, Wt_Y, 10, 10);
		// way points for NAV task
		// #1
		const WH_X = X_START_PX + (14.56 * width_map) / YARD_WIDTH_M;
		const WH_Y = Y_START_PX - (16.58 * height_map) / YARD_LENGTH_M;
		ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
		ctx.fillRect(WH_X, WH_Y, 10, 10);
		//let x_px = X_START_PX - y_next*width_map/YARD_WIDTH_M;
		//let y_px = START_Y_PX - x_next*height_map/YARD_LENGTH_M;
		// #2
		const WG_X = X_START_PX + (10.63 * width_map) / YARD_WIDTH_M;
		const WG_Y = Y_START_PX - (5.54 * height_map) / YARD_LENGTH_M;
		ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
		ctx.fillRect(WG_X, WG_Y, 10, 10);
		// #3
		const WQ_X = X_START_PX + (-3.12 * width_map) / YARD_WIDTH_M;
		const WQ_Y = Y_START_PX - (12.75 * height_map) / YARD_LENGTH_M;
		ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
		ctx.fillRect(WQ_X, WQ_Y, 10, 10);
		// #4
		const WC_X = X_START_PX + (3.67 * width_map) / YARD_WIDTH_M;
		const WC_Y = Y_START_PX - (19.0 * height_map) / YARD_LENGTH_M;
		ctx.fillStyle = "rgba(255, 0, 0, 0.5)";
		ctx.fillRect(WC_X, WC_Y, 10, 10);
		//ctx.fillStyle = 'rgba(0, 255, 0, 0.5)';
		ctx.fillStyle = "rgba(247, 202, 24, 1)";
		/* ===== DRAWING THE GRID + AXES ON THE NAV MAP ===== */
		// https://usefulangle.com/post/19/html5-canvas-tutorial-how-to-draw-graphical-coordinate-system-with-grids-and-axis

		ctx.fillStyle = "rgba(247, 202, 24, 1)";

		// move cursor to the starting point, to begin drawing line
		// pathContext.beginPath();
		// pathContext.moveTo(X_START_PX, Y_START_PX); // first line => moveTo()
		var grid_size = 21.27;
		var x_axis_distance_grid_lines = 33;
		var y_axis_distance_grid_lines = 15;
		var x_axis_starting_point = { number: 1, suffix: "" };
		var y_axis_starting_point = { number: 1, suffix: "" };
		// canvas width
		var canvas_width = canvas.width - 440;
		// canvas height
		var canvas_height = canvas.height - 30;
		// no of vertical grid lines
		var num_lines_x = Math.ceil(canvas_height / grid_size);
		// no of horizontal grid lines
		var num_lines_y = Math.floor(canvas_width / grid_size);

		// Draw grid points
		for (var i = 0; i < num_lines_y; i++) {
			for (var j = 0; j <= num_lines_x; j++) {
				ctx.beginPath();
				ctx.arc(i * grid_size, j * grid_size, 1.5, 0, 2 * Math.PI);
				ctx.fillStyle = "#FFFFFF";
				ctx.fill();
				ctx.closePath();
			}
		}

		// Draw grid lines along X-axis
		// for (var i = 0; i <= num_lines_x; i++) {
		// 	ctx.beginPath();
		// 	ctx.lineWidth = 1;

		// 	// If line represents X-axis draw in different color
		// 	if (i == x_axis_distance_grid_lines) {
		// 		ctx.setLineDash([]);
		// 		ctx.strokeStyle = "#000000";
		// 	} else {
		// 		// const totalSize = canvas_height / num_lines_y;
		// 		// ctx.setLineDash([totalSize / 2, totalSize / 2]);
		// 		ctx.strokeStyle = "#e9e9e9";
		// 	}

		// 	if (i == num_lines_x) {
		// 		ctx.moveTo(0, grid_size * i);
		// 		ctx.lineTo(canvas_width, grid_size * i);
		// 	} else {
		// 		ctx.moveTo(0, grid_size * i + 0.5);
		// 		ctx.lineTo(canvas_width, grid_size * i + 0.5);
		// 	}
		// 	ctx.stroke();
		// }

		// Draw grid lines along Y-axis
		// for (i = 0; i <= num_lines_y; i++) {
		// 	ctx.beginPath();
		// 	ctx.lineWidth = 1;

		// 	// If line represents Y-axis draw in different color
		// 	if (i == y_axis_distance_grid_lines) {
		// 		ctx.setLineDash([]);
		// 		ctx.strokeStyle = "#000000";
		// 	} else {
		// 		// const totalSize = canvas_width / num_lines_x;
		// 		// ctx.setLineDash([totalSize / 2, totalSize / 2]);
		// 		ctx.strokeStyle = "#e9e9e9";
		// 	}

		// 	if (i == num_lines_y) {
		// 		ctx.moveTo(grid_size * i, 0);
		// 		ctx.lineTo(grid_size * i, canvas_height);
		// 	} else {
		// 		ctx.moveTo(grid_size * i + 0.5, 0);
		// 		ctx.lineTo(grid_size * i + 0.5, canvas_height);
		// 	}
		// 	ctx.stroke();
		// }

		//TO DEBUG

		//Saves the original origin of the canvas
		ctx.save();

		//Translates the canvas and its origin
		ctx.translate(
			y_axis_distance_grid_lines * grid_size,
			x_axis_distance_grid_lines * grid_size
		);

		// Draw X-axis
		ctx.beginPath(); //starts a new path for the line
		ctx.lineWidth = 2; // sets the width of the line
		ctx.strokeStyle = "#FFFFFF"; //sets the color of the line
		ctx.moveTo(-y_axis_distance_grid_lines * grid_size, 0); //starting point
		ctx.lineTo(canvas_width - (y_axis_distance_grid_lines + 0.5) * grid_size, 0); //ending point
		ctx.stroke(); // draws the line on the canvas

		//Draw Y-axis
		ctx.beginPath();
		ctx.lineWidth = 2;
		ctx.strokeStyle = "#FFFFFF";
		ctx.moveTo(0, -x_axis_distance_grid_lines * grid_size);
		ctx.lineTo(0, canvas_height - (x_axis_distance_grid_lines - 0.5) * grid_size);
		ctx.stroke();

		//Ticks marks along the positive X-axis
		for (var i = 1; i < num_lines_y - y_axis_distance_grid_lines; i++) {
			ctx.beginPath();
			ctx.lineWidth = 1;
			ctx.strokeStyle = "#FFFFFF";
			// Draw a tick mark 6px long (-3 to 3)
			ctx.moveTo(grid_size * i + 0.5, -3);
			ctx.lineTo(grid_size * i + 0.5, 3);
			ctx.stroke();
			// Text value at that point
			ctx.font = "9px Arial";
			ctx.textAlign = "start";
			ctx.fillText(
				x_axis_starting_point.number * i + x_axis_starting_point.suffix,
				grid_size * i - 2,
				15
			);
		}
		// Ticks marks along the negative X-axis
		for (i = 1; i < y_axis_distance_grid_lines; i++) {
			ctx.beginPath();
			ctx.lineWidth = 1;
			ctx.strokeStyle = "#FFFFFF";
			// Draw a tick mark 6px long (-3 to 3)
			ctx.moveTo(-grid_size * i + 0.5, -3);
			ctx.lineTo(-grid_size * i + 0.5, 3);
			ctx.stroke();
			// Text value at that point
			ctx.font = "9px Arial";
			ctx.textAlign = "end";
			ctx.fillText(
				-x_axis_starting_point.number * i + x_axis_starting_point.suffix,
				-grid_size * i + 3,
				15
			);
		}
		// Ticks marks along the positive Y-axis
		// Positive Y-axis of graph is negative Y-axis of the canvas
		for (i = 1; i < num_lines_x - x_axis_distance_grid_lines; i++) {
			ctx.beginPath();
			ctx.lineWidth = 1;
			ctx.strokeStyle = "#FFFFFF";
			// Draw a tick mark 6px long (-3 to 3)
			ctx.moveTo(-3, grid_size * i + 0.5);
			ctx.lineTo(3, grid_size * i + 0.5);
			ctx.stroke();
			// Text value at that point
			ctx.font = "9px Arial";
			ctx.textAlign = "start";
			ctx.fillText(
				-y_axis_starting_point.number * i + y_axis_starting_point.suffix,
				8,
				grid_size * i + 3
			);
		}
		// Ticks marks along the negative Y-axis
		// Negative Y-axis of graph is positive Y-axis of the canvas
		for (i = 1; i < x_axis_distance_grid_lines; i++) {
			ctx.beginPath();
			ctx.lineWidth = 1;
			ctx.strokeStyle = "#FFFFFF";
			// Draw a tick mark 6px long (-3 to 3)
			ctx.moveTo(-3, -grid_size * i + 0.5);
			ctx.lineTo(3, -grid_size * i + 0.5);
			ctx.stroke();
			// Text value at that point
			ctx.font = "9px Arial";
			ctx.textAlign = "start";
			ctx.fillText(
				y_axis_starting_point.number * i + y_axis_starting_point.suffix,
				8,
				-grid_size * i + 3
			);
		}

		//restores the original position of the canvas
		ctx.restore();
	};
};

export default Map;
