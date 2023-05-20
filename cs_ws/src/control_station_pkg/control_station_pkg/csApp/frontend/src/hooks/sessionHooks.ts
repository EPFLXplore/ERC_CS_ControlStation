import React from "react";
import { useState, useEffect } from "react";

function useSession() {
	const [socket, setSocket] = useState<WebSocket | null>(null);
	const [userCount, setUserCount] = React.useState<number>(0);

	useEffect(() => {
		let sessionSocket = new WebSocket("ws://" + window.location.host + "/ws/csApp/session/");

		sessionSocket.onmessage = (e) => {
			const data = JSON.parse(e.data);
			setUserCount(data.nb_users);
		};

		sessionSocket.onerror = (e) => {
			console.log(e);
			setSocket(null);
		};

		setSocket(sessionSocket);
	}, []);

	return [userCount] as const;
}

export default useSession;
