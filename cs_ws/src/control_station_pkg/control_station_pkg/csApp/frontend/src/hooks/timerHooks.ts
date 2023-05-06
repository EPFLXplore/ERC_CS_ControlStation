import { useState, useEffect } from "react";

function useTimer(onFinished?: () => void) {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [minutes, setMinutes] = useState(0); // minutes left
	const [seconds, setSeconds] = useState(0); // seconds left
	const [finished, setFinished] = useState(false);
	const [active, _setActive] = useState(true);
	let interval: NodeJS.Timer;

	// Set up websocket
	useEffect(() => {
		let timerSocket = new WebSocket("ws://" + window.location.host + "/ws/csApp/timer/");
		setSocket(timerSocket);

		timerSocket.onmessage = (e) => {
			const { active, hours, minutes, seconds } = JSON.parse(e.data);
			_setActive(active);
			_changeTime(hours * 60 + minutes, seconds);
		};
	}, []);

	// Set up timer time
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

	// Set up interval of one second for update
	useEffect(() => {
		if (!finished && active) {
			interval = setTimeout(() => getTime(), 1000);
		}

		return () => clearTimeout(interval);
	}, [finished, active, minutes, seconds]);

	// Private function to change time
	const _changeTime = (minutes: number, seconds: number) => {
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

	// Public function to change time through websocket if available
	const changeTime = (minutes: number, seconds: number) => {
		if (socket?.readyState === WebSocket.OPEN) {
			socket?.send(
				JSON.stringify({
					minutes: minutes,
					seconds: seconds,
					active: active,
				})
			);
		} else {
			_changeTime(minutes, seconds);
		}
	};

	// Public function to change active through websocket if available
	const setActive = (active: boolean) => {
		if (socket?.readyState === WebSocket.OPEN) {
			socket?.send(
				JSON.stringify({
					minutes: minutes,
					seconds: seconds,
					active: active,
				})
			);
		} else {
			_setActive(active);
		}
	};

	// Call onFinished if timer is finished
	useEffect(() => {
		if (finished && onFinished) {
			onFinished();
		}
	}, [finished, onFinished]);

	return [minutes, seconds, active, changeTime, setActive] as const;
}

export default useTimer;
