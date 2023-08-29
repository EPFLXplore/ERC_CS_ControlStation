export const roundToTwoDecimals = (num: number, decimals = 2) => {
	return Math.floor(num * 10 ** decimals) / 10 ** decimals;
};

export function angle(cx: number, cy: number, ex: number, ey: number) {
	var dy = ey - cy;
	var dx = ex - cx;
	var theta = Math.atan2(dy, dx); // range (-PI, PI]
	theta *= 180 / Math.PI; // rads to degs, range (-180, 180]
	//if (theta < 0) theta = 360 + theta; // range [0, 360)
	return theta;
}

export const getDistance = (p1: Point, p2: Point) => {
	return Math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2);
};

export type Point = { x: number; y: number; o: number };
