import React, { useEffect, useState } from "react";
import { drawGoal } from "../components/Map";
import { drawCurrentPosition } from "../components/Map";

type Goal = { id: number; x: number; y: number; o: number };

export const useGoalTracker = () => {
	const [goals, setGoals] = useState<Goal[]>([]);

	const addGoal = (x: number, y: number, o: number) => {
		if (x.toString() !== "NaN" && y.toString() !== "NaN" && o.toString() !== "NaN") {
			const id = Date.now(); //Generate a unique id for the goal
			setGoals([...goals, { id, x, y, o }]);
		}
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

export function useNavigationSelector() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	var currentPoint = { x: 0, y: 0, o: 0 };

	useEffect(() => {
		let navigationSocket = new WebSocket(
			"ws://" + window.location.host + "/ws/csApp/info_nav/"
		);

		navigationSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			currentPoint = { x: data.x, y: data.y, o: 0 }; //TODO: no o data rendered by the JSON
			drawCurrentPosition(currentPoint);
		};

		navigationSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(navigationSocket);
	}, []);

	return currentPoint;
}
