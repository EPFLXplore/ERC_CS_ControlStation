import { useState, useEffect } from "react";
import GamepadController, { GamepadControllerState } from "../utils/Gamepad";

enum GamepadCommandState {
	UI,
	CONTROL,
}

function useGamepad() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [gamepad, setGamepad] = useState<GamepadController | null>(null);
	const [gamepadState, setGamepadState] = useState<GamepadControllerState | null>(null);
	const [gamepadCommandState, setGamepadCommandState] = useState<GamepadCommandState>(
		GamepadCommandState.UI
	);

	const update = () => {
		if (gamepad?.getGamepad() && gamepad.getIsConnected()) {
			setGamepadState(gamepad.getState());
		}
		requestAnimationFrame(update);
	};

	useEffect(() => {
		const gamepad = new GamepadController();
		setGamepad(gamepad);

		let gamepadSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/gamepad/");

		setSocket(gamepadSocket);
	}, []);

	useEffect(() => {
		setInterval(() => {
			if (
				gamepad?.getGamepad() &&
				gamepad.getIsConnected() &&
				socket?.readyState === WebSocket.OPEN &&
				gamepadCommandState === GamepadCommandState.CONTROL
			) {
				const stateSent = {
					axes: gamepad.getState().axes,
					buttons: gamepad.getState().buttons,
					id: gamepad.getState().controller?.id ?? "",
				};
				console.log(stateSent);
				socket?.send(JSON.stringify(stateSent));
			}
		}, 200);
	}, [socket]);

	useEffect(() => {
		requestAnimationFrame(update);
	}, [gamepad]);

	return [gamepad, gamepadState] as const;
}

export default useGamepad;
