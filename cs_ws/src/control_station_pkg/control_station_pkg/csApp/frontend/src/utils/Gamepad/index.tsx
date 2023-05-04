export interface GamepadControllerState {
	controller: Gamepad | null;
	isConnected: boolean;
	buttons: readonly boolean[];
	axes: readonly number[];
}

class GamepadController {
	private isConnected: boolean;
	private gamepad: Gamepad | null;

	constructor() {
		if (navigator.getGamepads().length > 0) {
			this.gamepad = navigator.getGamepads()[0];
			this.isConnected = true;
		} else {
			this.isConnected = false;
			this.gamepad = null;
		}

		const gamepadHandler = (e: GamepadEvent, connecting: boolean) => {
			// Case 1: No gamepad connected, and a gamepad is connecting
			if (!this.gamepad && connecting) {
				this.gamepad = e.gamepad;
				this.isConnected = connecting;
			} else if (this.gamepad && !connecting) {
				const gamepads = navigator.getGamepads();
				// Case 2: A gamepad is connected, and a gamepad is disconnecting
				if (gamepads.length > 0) {
					this.gamepad = gamepads[0];
					this.isConnected = true;
					// Case 3: No gamepad is connected, and a gamepad is disconnecting
				} else {
					this.gamepad = null;
					this.isConnected = false;
				}
			}
		};

		window.addEventListener(
			"gamepadconnected",
			function (e) {
				gamepadHandler(e, true);
			},
			false
		);
		window.addEventListener(
			"gamepaddisconnected",
			function (e) {
				gamepadHandler(e, false);
			},
			false
		);
	}

	public getGamepad(): Gamepad | null {
		return this.gamepad;
	}

	public getIsConnected(): boolean {
		return this.isConnected;
	}

	public getState(): GamepadControllerState {
		this.gamepad = navigator.getGamepads()[0];
		const state: GamepadControllerState = {
			controller: this.gamepad,
			isConnected: this.isConnected,
			buttons: this.gamepad
				? this.gamepad.buttons.map((button) => button.pressed).slice(0, 17)
				: [],
			axes: this.gamepad ? this.gamepad.axes : [],
		};

		return state;
	}
}

export default GamepadController;
