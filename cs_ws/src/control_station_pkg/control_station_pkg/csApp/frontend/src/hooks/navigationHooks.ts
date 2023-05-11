import React, { useEffect, useState } from "react";
import { drawGoal } from "../components/Map";
import { drawCurrentPosition } from "../components/Map";

type Goal = { id: number; x: number; y: number; o: number };

export const useGoalTracker = () => {
	const [goals, setGoals] = useState<Goal[]>([]);

	const getCookie = (name: string): string | null => {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

	const addGoal = (x: number, y: number, o: number) => {
		const id = Date.now(); //Generate a unique id for the goal
		setGoals([...goals, { id, x, y, o }]);
		const csrftoken = getCookie('csrftoken');

		let formData = new FormData();
		formData.append("x",  x.toString());
		formData.append('y',  y.toString());
		formData.append('yaw', o.toString());

		let request = new Request("http://127.0.0.1:8000/csApp/navigation/add_goal_nav",
		{
			method: "POST",
			headers: {
				"X-CSRFToken": csrftoken ?? ''
			},
			body: formData,
		})

		fetch(request).then((res) => res.json()).then((data) => console.log(data));

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
			"ws://127.0.0.1:8000/ws/csApp/info_nav/"
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
