export const roundToTwoDecimals = (num: number, decimals = 2) => {
	return Math.round(num * 10 ** 2) / 10 ** 2;
};

export function angle(cx: number, cy: number, ex: number, ey: number) {
	var dy = ey - cy;
	var dx = ex - cx;
	var theta = Math.atan2(dy, dx); // range (-PI, PI]
	theta *= 180 / Math.PI; // rads to degs, range (-180, 180]
	//if (theta < 0) theta = 360 + theta; // range [0, 360)
	return theta;
}
