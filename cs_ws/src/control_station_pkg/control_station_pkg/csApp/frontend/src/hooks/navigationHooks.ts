import React, { useEffect, useState } from "react";
import { drawPoint } from "../components/Map";

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
			drawPoint({ x: goal.x, y: goal.y, o: goal.o });
		});
	}, [goals]);

	return { goals, addGoal, removeGoal, resetGoals };
};
