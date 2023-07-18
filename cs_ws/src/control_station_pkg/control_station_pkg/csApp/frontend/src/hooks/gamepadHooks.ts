import { useState, useEffect } from "react";
import GamepadController, { GamepadControllerState } from "../utils/Gamepad";

enum GamepadCommandState {
	UI,
	CONTROL,
}

function getOS() {
	const OS = navigator.platform;

	if (OS.includes("Win") || OS.includes("Android")) {
		return "Windows";
	}

	return "Linux";
}

function useGamepad() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [gamepad, setGamepad] = useState<GamepadController | null>(null);
	const [gamepadState, setGamepadState] = useState<GamepadControllerState | null>(null);
	// const [gamepadCommandState, setGamepadCommandState] = useState<GamepadCommandState>(
	// 	GamepadCommandState.UI
	// );

	let gamepadCommandState = GamepadCommandState.UI;
	console.log("Gamepad Started");

	const OS = getOS();
	let controlUpdate: NodeJS.Timer | undefined;

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

		if (controlUpdate) clearInterval(controlUpdate);

		controlUpdate = setInterval(() => {
			console.log(gamepadCommandState);
			if (gamepad?.getGamepad() && gamepad.getIsConnected()) {
				// Detect Gamepad Commands
				if (gamepadCommandState === GamepadCommandState.UI) {
					if (
						(gamepad.getState().buttons[9] && OS === "Windows") ||
						(gamepad.getState().buttons[7] && OS === "Linux")
					) {
						console.log("Gamepad Command State: CONTROL");
						// setGamepadCommandState(GamepadCommandState.CONTROL);
						gamepadCommandState = GamepadCommandState.CONTROL;
					}

					if (
						(gamepad.getState().buttons[15] && OS === "Windows") ||
						(gamepad.getState().axes[7] > 0 && OS === "Linux")
					) {
						console.log("Gamepad Command: Tab");
						dispatchEvent(new KeyboardEvent("keydown", { key: "Tab" }));
					}

					if (gamepad.getState().buttons[0]) {
						console.log("Gamepad Command: Enter");
						dispatchEvent(new KeyboardEvent("keydown", { key: "Enter" }));
					}
				} else if (gamepadCommandState === GamepadCommandState.CONTROL) {
					if (
						(gamepad.getState().buttons[9] && OS === "Windows") ||
						(gamepad.getState().buttons[7] && OS === "Linux")
					) {
						console.log("Gamepad Command State: UI");
						// setGamepadCommandState(GamepadCommandState.UI);
						gamepadCommandState = GamepadCommandState.UI;
					}
				}
			}
		}, 75);
	}, [socket]);

	useEffect(() => {
		requestAnimationFrame(update);
	}, [gamepad]);

	return [gamepad, gamepadState] as const;
}

export default useGamepad;
