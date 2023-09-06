import React from "react";
import { useState, useEffect } from "react";

function useSession() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [userCount, setUserCount] = React.useState<number>(0);
	const [roverState, setRoverState] = React.useState<number>(-1);
	const [subsystemState, setSubsystemState] = React.useState<number>(-1);

	useEffect(() => {
		let sessionSocket = new WebSocket("ws://" + window.location.host + "/ws/csApp/session/");

		sessionSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);
			setUserCount(data.nb_users);
			setRoverState(data.rover_state);
			setSubsystemState(data.subsystem_state);
		};

		sessionSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(sessionSocket);
	}, []);

	return [userCount, roverState, subsystemState] as const;
}

export default useSession;
