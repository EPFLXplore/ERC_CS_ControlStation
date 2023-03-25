class GamepadController {
	private isConnected: boolean;
	private gamepad: Gamepad | null;

	constructor() {
		this.isConnected = false;
		this.gamepad = null;

		const gamepadHandler = (e: GamepadEvent, connecting: boolean) => {
			if (!this.gamepad) {
				this.gamepad = e.gamepad;
				this.isConnected = connecting;
				return;
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
}

export default GamepadController;
