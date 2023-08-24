import React, { useEffect, useState } from "react";
import { drawGoal } from "../components/Map";
import { drawTrajectory } from "../components/Map";

type Goal = { id: number; x: number; y: number; o: number };
type Point = { x: number; y: number; o: number };

export const useGoalTracker = () => {
	const [goals, setGoals] = useState<Goal[]>([]);

	const getCookie = (name: string): string | null => {
		let cookieValue = null;
		if (document.cookie && document.cookie !== "") {
			const cookies = document.cookie.split(";");
			for (let i = 0; i < cookies.length; i++) {
				const cookie = cookies[i].trim();
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) === name + "=") {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	};

	const addGoal = (x: number, y: number, o: number) => {
		if (x.toString() !== "NaN" && y.toString() !== "NaN" && o.toString() !== "NaN") {
			const id = Date.now(); //Generate a unique id for the goal
			setGoals([...goals, { id, x, y, o }]);
			const csrftoken = getCookie("csrftoken");

			let formData = new FormData();
			formData.append("x", x.toString());
			formData.append("y", y.toString());
			formData.append("yaw", o.toString());

			let request = new Request("http://127.0.0.1:8000/csApp/navigation/add_goal_nav", {
				method: "POST",
				headers: {
					"X-CSRFToken": csrftoken ?? "",
				},
				body: formData,
			});

			fetch(request)
				.then((res) => res.json())
				.then((data) => console.log(data))
				.catch((err) => console.log(err));

			// let formData = new FormData();
			// 								formData.append("x",  x.toString());
			// 								formData.append('y',  y.toString());
			// 								formData.append('yaw', o.toString());

			// 								let request = new Request('http://127.0.0.1:8000/csApp/navigation/add_goal_nav', {method: 'POST',
			// 																	body: formData,
			// 																	headers: {"X-CSRFToken": csrftoken ?? ''}})
			// 								fetch(request)
			// 									.then(response => response.json())
			// 									.then(result => {})
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
			drawGoal({ x: goal.x, y: goal.y, o: goal.o }, "red");
		});
	}, [goals]);

	return { goals, addGoal, removeGoal, resetGoals };
};

export function useNavigation() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [currentPosition, setCurrentPosition] = useState([0, 0, 0]);
	const [currentOrientation, setCurrentOrientation] = useState([0, 0, 0]);
	const [wheelsPosition, setWheelsPosition] = useState([0, 0, 0, 0]);
	const [linearVelocity, setLinearVelocity] = useState([0, 0, 0]);
	const [angularVelocity, setAngularVelocity] = useState([0, 0, 0]);
	const [trajectoryPoints, setTrajectoryPoints] = useState<Point[]>([]);

	useEffect(() => {
		let navigationSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/info_nav/");

		navigationSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);

			setCurrentPosition(data.position);
			setCurrentOrientation(data.orientation);
			setWheelsPosition(data.wheel_ang);
			setLinearVelocity(data.linVel);
			setAngularVelocity(data.angVel);
			setTrajectoryPoints((prevPoints) => [
				...prevPoints,
				{
					x: data.position[0],
					y: data.position[1],
					o: data.orientation[2],
				},
			]);
			drawTrajectory(trajectoryPoints);
		};

		navigationSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(navigationSocket);
	}, []);

	return [
		currentPosition,
		currentOrientation,
		wheelsPosition,
		linearVelocity,
		angularVelocity,
	] as const;
}
