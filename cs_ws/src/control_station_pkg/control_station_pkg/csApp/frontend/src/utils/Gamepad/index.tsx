import exp from "constants";
import { stat } from "fs";

export interface GamepadControllerState {
	controller: Gamepad | null;
	isConnected: boolean;
	buttons: readonly boolean[];
	axes: readonly number[];
	//profile: DeviceProfile;
}

export interface DeviceProfile {
	//il faudrais donner le gamepad au device profile pour qu'il puisse le lire
	//gamepad : Gamepad;
	name: String;
	OS: String;
	webBrowser: String;
	buttons: number;
	axes: number;
	minAxisRange: number[];
	maxAxisRange: number[];
	zeroAxisRange: number[];
	remapingButtons: number[];
	remapingAxes: number[];
}

const defaultProfile: DeviceProfile = {
	name: "default",
	OS: "default",
	webBrowser: "default",
	buttons: 17,
	axes: 7,
	minAxisRange: [-1, -1, -1, -1, -1, -1, -1],
	maxAxisRange: [1, 1, 1, 1, 1, 1, 1],
	zeroAxisRange: [0, 0, 0, 0, 0, 0, 0],
	remapingButtons: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16],
	remapingAxes: [0, 1, 2, 3, 4, 5, 6],
};

const xboxProfile: DeviceProfile = {
	name: "045e-0b12-Microsoft Xbox One X pad",
	OS: "linux",
	webBrowser: "firefox",
	buttons: 11,
	axes: 8,
	minAxisRange: [-1, -1, -1, -1, -1, -1, -1, -1],
	maxAxisRange: [1, 1, 1, 1, 1, 1, 1, 1],
	zeroAxisRange: [0, 0, -1, 0, 0, -1, 0, 0],
	remapingButtons: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
	remapingAxes: [0, 1, 2, 3, 4, 5, 6, 7],
};

export interface Binding {
	// a besoin du gamepad pour l'update
	prev_value: number;
	current_value: number;
	update(gamepad: Gamepad): void; // la fonction update est identique pour chaque binding, elle doit pouvoir etre def ici
	isPositiveTrigger(): boolean;
	isNegativeTrigger(): boolean;
	getValue(): number;
}

export class BindingButton implements Binding {
	button_index: number;
	prev_value: number;
	current_value: number;

	constructor(button_index: number) {
		this.button_index = button_index;
		this.prev_value = 0;
		this.current_value = 0;
	}

	public isPositiveTrigger() {
		return this.current_value > 0 && this.prev_value == 0;
	}

	public isNegativeTrigger() {
		return false; //can't be negative trigger
	}

	public getValue() {
		return this.current_value;
	}

	public update(gamepad: Gamepad) {
		this.prev_value = this.current_value;
		//TODO
	}
}

export class BindingAxis implements Binding {
	axis_index: number;
	prev_value: number;
	current_value: number;
	activationZone: number;

	constructor(axis_index: number, activationZone: number) {
		this.axis_index = axis_index;
		this.prev_value = 0;
		this.current_value = 0;
		this.activationZone = activationZone;
	}

	public isPositiveTrigger() {
		return this.current_value > this.activationZone && this.prev_value <= this.activationZone;
	}

	public isNegativeTrigger() {
		return this.current_value < -this.activationZone && this.prev_value >= -this.activationZone;
	}

	public getValue() {
		return this.current_value;
	}

	public update(gamepad: Gamepad) {
		this.prev_value = this.current_value;
		//TODO
	}
}

export class BindingComposite implements Binding {
	button1_index: number;
	button2_index: number;
	prev_value: number;
	current_value: number;

	constructor(button1_index: number, button2_index: number) {
		this.button1_index = button1_index;
		this.button2_index = button2_index;
		this.prev_value = 0;
		this.current_value = 0;
	}

	public isPositiveTrigger() {
		return this.current_value > 0 && this.prev_value === 0;
	}

	public isNegativeTrigger() {
		return this.current_value > 0 && this.prev_value === 0;
	}

	public getValue() {
		return this.current_value;
	}

	public update(gamepad: Gamepad) {
		this.prev_value = this.current_value;
		//TODO
	}
}

/*

UI
		move buttons 10 11 12 13 //Up right down left
		select buttons 0
		back buttons 4
		change mode buttons 1

NAV
		Up/Down : axes 1
		Left/Right : axes 0
		change mode

HD
		change mode
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
export enum ActionTriggerMode {
	positive,
	negative,
	value,
}
export class Action {
	name: string;
	activationMode: ActionTriggerMode;
	bindings: Array<Binding>;

	constructor(name: string, activationMode: ActionTriggerMode, bindings: Array<Binding>) {
		this.name = name;
		this.activationMode = activationMode;
		this.bindings = bindings;
	}

	public isTriggered() {
		switch (this.activationMode) {
			case ActionTriggerMode.positive:
				return this.bindings.some((binding) => binding.isPositiveTrigger());
			case ActionTriggerMode.negative:
				return this.bindings.some((binding) => binding.isNegativeTrigger());
			case ActionTriggerMode.value:
				return true;
		}
	}

	public getValue() {
		return this.bindings.reduce((acc, binding) => acc + binding.getValue(), 0);
	}
}

export interface actionManager {
	//UI
	UI_move_up_down: Array<Binding>;
	UI_move_right_left: Array<Binding>;
	UI_select: Array<Binding>;
	UI_back: Array<Binding>;
	UI_change_mode: Array<Binding>;

	//HD
	HD_change_mode: Array<Binding>;
	//HD Inverse
	HD_inverse_x: Array<Binding>;
	HD_inverse_y: Array<Binding>;
	HD_inverse_z: Array<Binding>;
	HD_inverse_pitch: Array<Binding>;
	HD_inverse_roll: Array<Binding>;
	HD_inverse_yaw: Array<Binding>;
	HD_inverse_gripper: Array<Binding>;
	//HD Forward
	HD_forward_motor1: Array<Binding>;
	HD_forward_motor2: Array<Binding>;
	HD_forward_motor3: Array<Binding>;
	HD_forward_motor4: Array<Binding>;
	HD_forward_motor5: Array<Binding>;
	HD_forward_motor6: Array<Binding>;
	HD_forward_gripper: Array<Binding>;
}

/*const defaultActionManager : actionManager = {
	UI_move_up_down: [new BindingAxis(1, 0.5)],

}*/

// export interface DeviceRemaping {
// 	os: string;
// 	navigator: string;
// 	name: string;
// 	gamepad: GamepadControllerState;
// 	buttons: number;
// 	axes: number;
// 	buttonsOrder: number[];
// 	axesOrder: number[];
// 	axesMin: number[];
// 	axesMax: number[];
// 	axesZero: number[];
// 	RemapingButtons(): number[];
// 	RemapingAxes(): number[];
// }

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

Gamepad + OS + browser
Gamepad seulement (remap fait)

Connect device
FindProfile by name if not found select default profile


Action / InputAction
	Binding Array



ActionProfile : 

		name : Gamepad Xbox ou Playstation
		Trigger function on value != 0 ?
		performed




AxisComposite
ButtonAxis

*/
