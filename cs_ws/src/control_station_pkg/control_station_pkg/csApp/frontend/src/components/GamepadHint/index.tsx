import React from "react";
import useGamepad from "../../hooks/gamepadHooks";
import GamepadDisplay from "./GamepadDisplay";
import styles from "./style.module.sass";

const GamepadHint = ({}: {}) => {
	const [gamepad, gamepadState] = useGamepad();

	const calcDirectionVertical = (axe: number) => {
		// Up
		if (axe < -0.2) {
			return "up";
		}
		// Down
		if (axe > 0.2) {
			return "down";
		}

		return "";
	};

	const calcDirectionHorizontal = (axe: number) => {
		// Left
		if (axe < -0.2) {
			return "left";
		}
		// Right
		if (axe > 0.2) {
			return "right";
		}

		return "";
	};

	if (gamepad?.getGamepad() && gamepadState) {
		return (
			<div className={styles.Container}>
				<GamepadDisplay
					buttonDown={gamepadState.buttons[0]}
					buttonRight={gamepadState.buttons[1]}
					buttonLeft={gamepadState.buttons[2]}
					buttonUp={gamepadState.buttons[3]}
					directionUp={gamepadState.buttons[12]}
					directionDown={gamepadState.buttons[13]}
					directionLeft={gamepadState.buttons[14]}
					directionRight={gamepadState.buttons[15]}
					analogLeft={
						gamepadState.axes[0] > 0.3 ||
						gamepadState.axes[0] < -0.3 ||
						gamepadState.axes[1] > 0.3 ||
						gamepadState.axes[1] < -0.3
					}
					analogRight={
						gamepadState.axes[2] > 0.3 ||
						gamepadState.axes[2] < -0.3 ||
						gamepadState.axes[3] > 0.3 ||
						gamepadState.axes[3] < -0.3
					}
					analogLeftDirection={[
						calcDirectionHorizontal(gamepadState.axes[0]),
						calcDirectionVertical(gamepadState.axes[1]),
					]}
					analogRightDirection={[
						calcDirectionHorizontal(gamepadState.axes[2]),
						calcDirectionVertical(gamepadState.axes[3]),
					]}
					select={gamepadState.buttons[8]}
					start={gamepadState.buttons[9]}
					activeColor="#402921"
				/>
			</div>
		);
	} else {
		return null;
	}
};

export default GamepadHint;
