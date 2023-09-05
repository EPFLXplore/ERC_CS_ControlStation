export const roundToTwoDecimals = (num: number, decimals = 2) => {
    return Math.round(num * (10 ** 2)) / (10 ** 2);
};