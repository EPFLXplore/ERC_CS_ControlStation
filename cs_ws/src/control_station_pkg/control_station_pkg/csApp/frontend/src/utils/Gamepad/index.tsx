export interface GamepadControllerState {
	controller: Gamepad | null;
	isConnected: boolean;
	buttons: readonly boolean[];
	axes: readonly number[];
}

export interface DeviceRemaping {
	os: string;
	navigator: string;
	name: string;
	gamepad: GamepadControllerState;
	buttons: number;
	axes: number;
	buttonsOrder: number[];
	axesOrder: number[];
	axesMin: number[];
	axesMax: number[];
	axesZero: number[];
	RemapingButtons(): number[];
	RemapingAxes(): number[];
}

export interface DeviceProfile {
	mainDevice: DeviceRemaping;
	othersDevices: DeviceRemaping[];
	//UI
	moveButtons: number[];
	selectButtons: number[];
	backButtons: number[];
	changeModeButtons: number[];
	//Nav
	upDownAxes: number;
	leftRightAxes: number;
	//HD
	//Inverse
	inverseXAxes: number;
	inverseYAxes: number;
	inverseZAxes: number[];

}


class GamepadController {
	private isConnected: boolean;
	private gamepad: Gamepad | null;

	constructor() {
		if (navigator.getGamepads().length > 0 && navigator.getGamepads()[0]) {
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
default speed 1

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
