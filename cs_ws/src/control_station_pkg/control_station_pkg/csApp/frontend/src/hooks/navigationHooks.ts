import React, { useEffect, useState } from "react";
import { drawGoal } from "../components/Map";
import { drawCurrentPosition } from "../components/Map";

type Goal = { id: number; x: number; y: number; o: number };

export const useGoalTracker = () => {
	const [goals, setGoals] = useState<Goal[]>([]);

	const addGoal = (x: number, y: number, o: number) => {
		const id = Date.now(); //Generate a unique id for the goal
		setGoals([...goals, { id, x, y, o }]);
	};

	const resetGoals = () => {
		setGoals([]);
	};

	const removeGoal = (id: number) => {
		const newGoals = goals.filter((goal) => goal.id !== id);
		setGoals(newGoals);
	};

	useEffect(() => {
		goals.forEach((goal) => {
			drawGoal({ x: goal.x, y: goal.y, o: goal.o });
		});
	}, [goals]);

	return { goals, addGoal, removeGoal, resetGoals };
};

export function useNavigation() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [currentPosition, setCurrentPosition] = useState({ x: 0, y: 0, o: 0 });
	const [wheelsPosition, setWheelsPosition] = useState({ fl: 0, fr: 0, rl: 0, rr: 0 });
	const [linearVelocity, setLinearVelocity] = useState(0);
	const [angularVelocity, setAngularVelocity] = useState(0);

	useEffect(() => {
		let navigationSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/info_nav/");

		navigationSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setCurrentPosition({ x: data.x, y: data.y, o: 0 });
			setWheelsPosition({
				fl: data.ang_front_left_wheel,
				fr: data.ang_front_right_wheel,
				rl: data.ang_back_left_wheel,
				rr: data.ang_back_right_wheel,
			});
			setLinearVelocity(data.linVel);
			setAngularVelocity(data.angVel);
			drawCurrentPosition({ x: data.x, y: data.y, o: 0 });
		};

		navigationSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(navigationSocket);
	}, []);

	return [currentPosition, wheelsPosition] as const;
}
