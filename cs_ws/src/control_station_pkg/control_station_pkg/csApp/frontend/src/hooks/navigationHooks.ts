import React, { useEffect, useState } from "react";
import { drawGoal } from "../components/Map";
import { Point, getDistance } from "../utils/maths";
import { getCookie } from "../utils/requests";
import path from "path";
import simplify from "simplify-js";

export type Goal = Point & { id: string };

export const useGoalTracker = () => {
	const [goals, setGoals] = useState<Goal[]>([]);
	const [savedGoals, setSavedGoals] = useState<Goal[]>([
		// { x: -9.77, y: 5.59, o: 0, id: 1 },
		// { x: -11.67, y: 17.43, o: 0, id: 2 },
		// { x: -14.55, y: 11.66, o: 0, id: 3 },
		// { x: -15.24, y: 5.31, o: 0, id: 4 },
		// { x: -3.43, y: 9.67, o: 0, id: 5 },
		// { x: -0.66, y: 6.1, o: 0, id: 6 },
		// { x: 4.96, y: 11.7, o: 0, id: 7 },
		// { x: 5.29, y: 19.04, o: 0, id: 8 },
		// { x: 13.22, y: 18.18, o: 0, id: 9 },
		// { x: 17.54, y: 9.39, o: 0, id: 10 },
		// { x: 4.14, y: 27.16, o: 0, id: 11 },
		// { x: 11.43, y: 28.91, o: 0, id: 12 },
		// { x: -0.84, y: 22.44, o: 0, id: 13 },
		// { x: -9.6, y: 27.71, o: 0, id: 14 },
		// { x: 10.65, y: 7.25, o: 0, id: 15 },
		{ x: 3.83, y: 9.1, o: 0, id: "W1" },
		{ x: -9.9, y: 13.49, o: 0, id: "W2" },
		{ x: -0.2, y: 19.57, o: 0, id: "W3" },
		{ x: -6.99, y: 25.22, o: 0, id: "W4" },
		{ x: 5.44, y: 25.42, o: 0, id: "W5" },
		{ x: 10.46, y: 16.29, o: 0, id: "W6" },
		{ x: 13.85, y: 10.86, o: 0, id: "W7" },
		{ x: 12.45, y: 21.27, o: 0, id: "W8" },
		{ x: -6.87, y: 26.6, o: 0, id: "X1" },
	]);
	const [tempGoal, setTempGoal] = useState<Goal>();

	const addSavedGoal = (x: number, y: number, o: number, id: string) => {
		setSavedGoals([...savedGoals, { x, y, o, id }]);
	};

	const addGoal = (x: number, y: number, o: number) => {
		const id = Date.now().toString(); //Generate a unique id for the goal
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

	const removeGoal = (id: string) => {
		const newGoals = goals.filter((goal) => goal.id !== id);
		setGoals(newGoals);
	};

	const removeSavedGoal = (id: string) => {
		const newGoals = savedGoals.filter((goal) => goal.id !== id);
		setSavedGoals(newGoals);
	};

	return {
		goals,
		addGoal,
		removeGoal,
		resetGoals,

		tempGoal,
		setTempGoal,

		savedGoals,
		addSavedGoal,
		setSavedGoals,
		removeSavedGoal,
	};
};

export function useNavigation(successCallback?: () => void) {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [currentPosition, setCurrentPosition] = useState([0,0,0]);
	const [currentOrientation, setCurrentOrientation] = useState([0, 0, 0]);
	const [wheelsPosition, setWheelsPosition] = useState([0, 0, 0, 0]);
	const [linearVelocity, setLinearVelocity] = useState([0, 0, 0]);
	const [angularVelocity, setAngularVelocity] = useState([0, 0, 0]);
	const [trajectoryPoints, setTrajectoryPoints] = useState<(Point | {x: number; y: number})[]>([]);
	const [pathPoints, setPathPoints] = useState<Point[]>([]);
	const [showPath, setShowPath] = useState<boolean>(true);
	const [driving_state, setDrivingState] = useState<string[]>(["False", "False", "False", "False"]);
	const [steering_state, setSteeringState] = useState<string[]>(["False", "False", "False", "False"]);
	const [info, setInfo] = useState<string>("Welcome in Autonomous Navigation Mode");
	const [displacement, setDisplacement] = useState<string>("normal");
	const [routeLeft, setRouteLeft] = useState<number>(0);

	useEffect(() => {
		let navigationSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/info_nav/");

		navigationSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);
			const pathPoints = data.path.map((element: number[]) => {
				return {
					x: element[0],
					y: element[1],
					o: 0,
				}
			})
			
			setCurrentPosition(data.position);
			setCurrentOrientation(data.orientation);
			setWheelsPosition(data.steering_wheel_ang);
			setLinearVelocity(data.linVel);
			setAngularVelocity(data.angVel);
			setTrajectoryPoints((prevPoints) => {
				if(prevPoints.length > 1000) {
					return [
						...simplify(prevPoints, 0.3, false),
						{
							x: data.position[0],
							y: data.position[1],
							o: data.orientation[2],
						},]
				} else {
					return [
					...prevPoints,
					{
						x: data.position[0],
						y: data.position[1],
						o: data.orientation[2],
					},]
				}
			});
			setPathPoints((prev) => {
				if(prev.length > 0 && pathPoints.length === 0) {
					successCallback && successCallback()
				}
				return pathPoints;
			});
			setDrivingState(data.driving_wheel_state);
			setSteeringState(data.steering_wheel_state);
			setInfo(data.info);
			setDisplacement(data.displacement_mode);
			setRouteLeft(pathPoints.reduce((acc: [number, Point], curr: Point) => [acc[0] + getDistance(acc[1], curr), curr]));
		};

		navigationSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(navigationSocket);
	}, []);

	const initPos = (point: Point) => {
		const csrftoken = getCookie("csrftoken");
		let formData = new FormData();
		formData.append("x", point.x.toString());
		formData.append("y", point.y.toString());
		formData.append("yaw", point.o.toString());

		let request = new Request(
			"http://127.0.0.1:8000/csApp/navigation/nav_starting_point",
			{
				method: "POST",
				headers: {
					"X-CSRFToken": csrftoken ?? "",
				},
				body: formData,
			}
		);

		fetch(request)
			.then((res) => res.json())
			.then((data) => console.log(data))
			.catch((err) => console.log(err));
	};

	return [
		currentPosition,
		currentOrientation,
		wheelsPosition,
		linearVelocity,
		angularVelocity,
		trajectoryPoints,
		pathPoints,
		showPath,
		setShowPath,
		initPos,
		driving_state,
		steering_state,
		info,
		displacement,
		routeLeft
	] as const;
}
