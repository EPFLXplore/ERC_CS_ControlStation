import { useState, useEffect } from "react";

function useTimer(onFinished?: () => void) {
	const [minutes, setMinutes] = useState(0); // minutes left
	const [seconds, setSeconds] = useState(0); // seconds left
	const [finished, setFinished] = useState(false);
	const [active, setActive] = useState(true);
	let interval: NodeJS.Timer;

	const getTime = (changeMinutes?: number, changeSeconds?: number) => {
		let newMinutes = changeMinutes || minutes;
		let newSeconds = changeSeconds || seconds;
		let time = newMinutes * 60000 + newSeconds * 1000;

		if (time <= 0) {
			setFinished(true);
			setMinutes(0);
			setSeconds(0);
			return;
		}

		if (active) time -= 1000;

		setMinutes(Math.floor((time / 1000 / 60) % 60));
		setSeconds(Math.floor((time / 1000) % 60));
		setFinished(false);
	};

	useEffect(() => {
		if (!finished && active) {
			interval = setTimeout(() => getTime(), 1000);
		}

		return () => clearTimeout(interval);
	}, [finished, active, minutes, seconds]);

	const changeTime = (minutes: number, seconds: number) => {
		if (minutes >= 0 && seconds >= 0 && seconds < 60) {
			clearTimeout(interval);
			getTime(minutes, seconds);
		} else if (minutes >= 0 && seconds >= 60) {
			clearTimeout(interval);
			getTime(
				minutes + Math.floor(seconds / 60),
				(seconds - Math.floor(seconds / 60) * 60) % 60
			);
		}
	};

	useEffect(() => {
		if (finished && onFinished) {
			onFinished();
		}
	}, [finished, onFinished]);

	return [minutes, seconds, active, changeTime, setActive] as const;
}

export default useTimer;
