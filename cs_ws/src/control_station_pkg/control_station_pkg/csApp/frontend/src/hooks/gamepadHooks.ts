import { useState, useEffect } from "react";
import GamepadController, { GamepadControllerState } from "../utils/Gamepad";
import { Task } from "../utils/tasks.type";

export enum GamepadCommandState {
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

function useGamepad(mode: string, selectorCallback?: () => void) {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [gamepad, setGamepad] = useState<GamepadController | null>(null);
	const [gamepadState, setGamepadState] = useState<GamepadControllerState | null>(null);
	const [gamepadCommandState, setGamepadCommandState] = useState<GamepadCommandState>(
		GamepadCommandState.UI
	);
	const [OS, setOS] = useState(getOS());
	const [gamepadFocus, setGamepadFocus] = useState(0);

	const focusableElements = document.querySelectorAll(
		'button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])'
	);

	let [controlUpdate, setControlUpdate] = useState<NodeJS.Timeout | undefined>(undefined);
	let [sendUpdate, setSendUpdate] = useState<NodeJS.Timeout | undefined>(undefined);

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

		gamepadSocket.onerror = (e) => {
			console.log("Gamepad Socket Error");
		};

		setSocket(gamepadSocket);
	}, []);

	useEffect(() => {
		if (sendUpdate) clearInterval(sendUpdate);

		setSendUpdate(
			setInterval(() => {
				if (
					gamepad?.getGamepad() &&
					gamepad.getIsConnected() &&
					socket?.readyState === WebSocket.OPEN &&
					gamepadCommandState === GamepadCommandState.CONTROL
				) {
					console.log("Sending Gamepad State");
					const stateSent = {
						axes: gamepad.getState().axes,
						buttons: gamepad.getState().buttons,
						id: gamepad.getState().controller?.id ?? "",
						mode: mode,
					};
					console.log(stateSent);
					socket?.send(JSON.stringify(stateSent));
				}
			}, 200)
		);

		if (controlUpdate) clearInterval(controlUpdate);

		setControlUpdate(
			setInterval(() => {
				if (gamepad?.getGamepad() && gamepad.getIsConnected()) {
					// Detect Gamepad Commands
					if (gamepadCommandState === GamepadCommandState.UI) {
						if (
							(gamepad.getState().buttons[9] && OS === "Windows") ||
							(gamepad.getState().buttons[7] && OS === "Linux")
						) {
							console.log("Gamepad Command State: CONTROL");
							setGamepadCommandState(GamepadCommandState.CONTROL);
						}

						if (
							(gamepad.getState().buttons[8] && OS === "Windows") ||
							(gamepad.getState().buttons[6] && OS === "Linux")
						) {
							console.log("Gamepad Command: Custom Selector");
							selectorCallback?.();
						}

						if (
							(gamepad.getState().buttons[15] && OS === "Windows") ||
							(gamepad.getState().axes[6] > 0 && OS === "Linux")
						) {
							nextItem();
							console.log(gamepadFocus);
						}

						if (gamepad.getState().buttons[0]) {
							console.log("Gamepad Command: Enter");
							(focusableElements[gamepadFocus] as HTMLElement).click();
						}
					} else if (gamepadCommandState === GamepadCommandState.CONTROL) {
						if (
							(gamepad.getState().buttons[9] && OS === "Windows") ||
							(gamepad.getState().buttons[7] && OS === "Linux")
						) {
							console.log("Gamepad Command State: UI");
							setGamepadCommandState(GamepadCommandState.UI);
						}

						if (
							(gamepad.getState().buttons[8] && OS === "Windows") ||
							(gamepad.getState().buttons[6] && OS === "Linux")
						) {
							console.log("Gamepad Command: Custom Selector");
							selectorCallback?.();
						}
					}
				}
			}, 150)
		);
	}, [socket, gamepadCommandState, gamepadFocus, mode]);

	useEffect(() => {
		requestAnimationFrame(update);
	}, [gamepad]);

	function nextItem() {
		console.log(focusableElements);
		(focusableElements[(gamepadFocus + 1) % focusableElements.length] as HTMLElement).focus();
		setGamepadFocus((gamepadFocus + 1) % focusableElements.length);
	}

	return [gamepad, gamepadState, gamepadCommandState] as const;
}

export default useGamepad;



/*

Gamepad Profile

0738-2221-Mad Catz Saitek Pro Flight X-56 Rhino Stick
0738-a221-Mad Catz Saitek Pro Flight X-56 Rhino Throttle

Linux, firefox
buttons: 17
axes: 7
min [-1,1,-1,1,-1,-1,-1]
max [1,-1,1,-1,1,1,1]
zero [0,0,0,0,0,0,0]

UI
move buttons 10 11 12 13 //Up right down left
select buttons 0
back buttons 4
change mode buttons 1

Nav
Up/Down : axes 1
Left/Right : axes 0

HD
Inverse
x: axes 1
y: axes 0
z: buttons 10 12
pitch: axes 5
roll: buttons 5 + axes 1
yaw: buttons 5 + axes 0
gripper : buttons 0 4
speed : Throttle axes 1

Forward
Motor 1: axes 5
Motor 2: axes 1
Motor 3: buttons 5 + axes 1
Motor 4: axes 0
Motor 5: buttons 10 12
Motor 6: buttons 5 + axes 0
Grinder: buttons 0 4
Speed: Throttle axes 1


*/