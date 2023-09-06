import { useEffect, useRef, useState } from "react";
import roverWheelsImage from "../../assets/images/icons/rover_wheels.svg";

const WheelsIndicator = ({ wheelsOrientation }: { wheelsOrientation: number[] }) => {
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
				drawWheels(ctx, image, wheelsOrientation);
			}
		}
	}, [image, imageWidth, imageHeight, wheelsOrientation]);

	return <canvas ref={canvasRef} width={100} height={100} />;
};

const drawWheels = (
	ctx: CanvasRenderingContext2D,
	image: HTMLImageElement,
	wheelsOrientation: number[]
) => {
	const margin = 25;

	ctx.clearRect(0, 0, ctx.canvas.width, ctx.canvas.height);
	ctx.save();

	ctx.translate(margin, margin);
	ctx.rotate(wheelsOrientation[0]);
	ctx.fillStyle = "#FFFFFF";
	ctx.rect(-10, -20, 15, 30);
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.translate(ctx.canvas.width - 20, margin);
	ctx.rotate(wheelsOrientation[1]);
	ctx.rect(-10, -20, 15, 30);
	ctx.fillStyle = "#FFFFFF";
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.translate(ctx.canvas.width - 20, ctx.canvas.height - 15);
	ctx.rotate(wheelsOrientation[2]);
	ctx.rect(-10, -20, 15, 30);
	ctx.fillStyle = "#FFFFFF";
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.translate(margin, ctx.canvas.height - 15);
	ctx.rotate(wheelsOrientation[3]);
	ctx.rect(-10, -20, 15, 30);
	ctx.fillStyle = "#FFFFFF";
	ctx.fill();

	ctx.restore();
	ctx.save();

	ctx.drawImage(image, 50 - 799 / 22, 50 - 951 / 22, 799 / 11, 951 / 11);
	ctx.restore();
};

export default WheelsIndicator;
