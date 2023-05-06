import { useState, useEffect } from "react";
import GamepadController, { GamepadControllerState } from "../utils/Gamepad";

function useGamepad() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [gamepad, setGamepad] = useState<GamepadController | null>(null);
	const [gamepadState, setGamepadState] = useState<GamepadControllerState | null>(null);

	const update = () => {
		if (gamepad?.getGamepad() && gamepad.getIsConnected()) {
			setGamepadState(gamepad.getState());
		}
		requestAnimationFrame(update);
	};

	useEffect(() => {
		const gamepad = new GamepadController();
		setGamepad(gamepad);

		let gamepadSocket = new WebSocket("ws://" + window.location.host + "/ws/csApp/gamepad/");

		setSocket(gamepadSocket);
	}, []);

	useEffect(() => {
		requestAnimationFrame(update);
	}, [gamepad]);

	setInterval(() => {
		if (gamepad?.getGamepad() && gamepad.getIsConnected()) {
			const stateSent = {
				axes: gamepad.getState().axes,
				buttons: gamepad.getState().buttons,
				id: gamepad.getState().controller?.id ?? "",
			};
			console.log(stateSent);
			if (socket?.readyState === WebSocket.OPEN) socket?.send(JSON.stringify(stateSent));
		}
	}, 50);

	return [gamepad, gamepadState] as const;
}

export default useGamepad;
