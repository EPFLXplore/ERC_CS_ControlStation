import { useEffect, useRef, useState } from "react";
import roverWheelsImage from "../../assets/images/icons/rover_wheels.svg";

const WheelsIndicator = ({ wheelsOrientation, driving_state, steering_state }: { wheelsOrientation: number[]; driving_state: boolean[]; steering_state: boolean[]; }) => {
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
		img.src = roverWheelsImage;
	}, [roverWheelsImage]);

	useEffect(() => {
		console.log("use effect draw grid called");
		// Draw the grid on the canvas
		const canvas = canvasRef.current;
		if (canvas && image) {
			const ctx = canvas.getContext("2d");

			if (ctx) {
				drawWheels(ctx, image, wheelsOrientation, driving_state, steering_state);
			}
		}
	}, [image, imageWidth, imageHeight, wheelsOrientation]);

	return <canvas ref={canvasRef} width={100} height={100} />;
};

const drawWheels = (
	ctx: CanvasRenderingContext2D,
	image: HTMLImageElement,
	wheelsOrientation: number[],
	driving_state: boolean[],
	steering_state: boolean[]
) => {
	const margin = 25;

	ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
	ctx.save();

	ctx.translate(margin, margin);
	ctx.rotate(wheelsOrientation[0]);
	ctx.fillStyle = driving_state[0] ? "#FFFFFF" : "#FF0000";
	ctx.fillRect(-10, -20, 15, 30);

	ctx.beginPath();
	ctx.fillStyle = steering_state[0] ? "#FFFFFF" : "#FF0000";
	ctx.arc(0, -5, 5, 0, 2 * Math.PI);
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.translate(ctx.canvas.width - 20, margin);
	ctx.rotate(wheelsOrientation[1]);
	ctx.fillStyle = driving_state[1] ? "#FFFFFF" : "#FF0000";
	ctx.fillRect(-10, -20, 15, 30);

	ctx.beginPath();
	ctx.fillStyle = steering_state[1] ? "#FFFFFF" : "#FF0000";
	ctx.arc(-5, -5, 5, 0, 2 * Math.PI);
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.translate(ctx.canvas.width - 20, ctx.canvas.height - 15);
	ctx.rotate(wheelsOrientation[2]);
	ctx.fillStyle = driving_state[2] ? "#FFFFFF" : "#FF0000";
	ctx.fillRect(-10, -20, 15, 30);

	ctx.beginPath();
	ctx.fillStyle = steering_state[2] ? "#FFFFFF" : "#FF0000";
	ctx.arc(-5, -4, 5, 0, 2 * Math.PI);
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.translate(margin, ctx.canvas.height - 15);
	ctx.rotate(wheelsOrientation[3]);
	ctx.fillStyle = driving_state[3] ? "#FFFFFF" : "#FF0000";
	ctx.fillRect(-10, -20, 15, 30);

	ctx.beginPath();
	ctx.fillStyle = steering_state[3] ? "#FFFFFF" : "#FF0000";
	ctx.arc(0, -5, 5, 0, 2 * Math.PI);
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.drawImage(image, 50 - 799 / 22, 50 - 951 / 22, 799 / 11, 951 / 11);
	ctx.restore();
};

export default WheelsIndicator;
