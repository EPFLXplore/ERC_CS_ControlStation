import React, { useEffect, useState } from "react";
import { drawGoal } from "../components/Map";
import { Point } from "../utils/maths";
import { getCookie } from "../utils/requests";

export type Goal = Point & { id: number };

export const useGoalTracker = () => {
	const [goals, setGoals] = useState<Goal[]>([]);
	const [tempGoal, setTempGoal] = useState<Goal>();

	const addGoal = (x: number, y: number, o: number) => {
		const id = Date.now(); //Generate a unique id for the goal
		setGoals([...goals, { id, x, y, o }]);
		const csrftoken = getCookie("csrftoken");

		let formData = new FormData();
		formData.append("x", x.toString());
		formData.append("y", y.toString());
		formData.append("yaw", o.toString());

		let request = new Request("http://127.0.0.1:8000/csApp/navigation/nav_goal", {
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
	};

	const resetGoals = () => {
		setGoals([]);

		const csrftoken = getCookie("csrftoken");

		let request = new Request("http://127.0.0.1:8000/csApp/navigation/nav_cancel", {
			method: "POST",
			headers: {
				"X-CSRFToken": csrftoken ?? "",
			},
		});

		fetch(request)
			.then((res) => res.json())
			.then((data) => console.log(data))
			.catch((err) => console.log(err));
	};

	const removeGoal = (id: number) => {
		const newGoals = goals.filter((goal) => goal.id !== id);
		setGoals(newGoals);
	};

	return { goals, addGoal, removeGoal, resetGoals, tempGoal, setTempGoal };
};

export function useNavigation() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [currentPosition, setCurrentPosition] = useState([-12.5, 20.5, 45]);
	const [currentOrientation, setCurrentOrientation] = useState([0, 0, 0]);
	const [wheelsPosition, setWheelsPosition] = useState([0, 0, 0, 0]);
	const [linearVelocity, setLinearVelocity] = useState([0, 0, 0]);
	const [angularVelocity, setAngularVelocity] = useState([0, 0, 0]);
	const [trajectoryPoints, setTrajectoryPoints] = useState<Point[]>([
		{ x: 0, y: 0, o: 0 },
		{ x: -12.5, y: 20.5, o: 45 },
	]);

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
		trajectoryPoints,
	] as const;
}
