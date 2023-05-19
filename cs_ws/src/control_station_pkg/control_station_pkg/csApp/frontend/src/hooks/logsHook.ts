import React from "react";
import { useEffect, useState } from "react";

export type Log = {
	time: string;
	type: string;
	message: string;
};

const getType = (type: number): string => {
	switch(type) {
		case 0:
			return 'info'
		case 1:
			return 'data'
		case 2:
			return 'warning'
		case 3:
			return 'error'
		default:
			return 'info'
	}
}

function useLogs() {
	let logBuffer: Log[]= []
	const [logs, setLogs] = useState<Log[]>([]);
	const [filters, setFilters] = React.useState<string[]>([]);
	const [filteredLogs, setFilteredLogs] = React.useState<Log[]>([]);
	const [socket, setSocket] = useState<WebSocket>(new WebSocket("ws://127.0.0.1:8000/ws/csApp/log/"));

	useEffect(() => {
		let logsSocket = new WebSocket("ws://127.0.0.1:8000/ws/csApp/log/");
		setSocket(logsSocket);

		setTimeout(() => {
			if (logsSocket.readyState !== WebSocket.OPEN) {
				let test_logs = require("../pages/logs/test_logs.json") as Log[];
				test_logs = [
					...test_logs,
					{
						time: new Date().toLocaleString(),
						type: "error",
						message: "Test logs loaded because the websocket took too long to connect",
					},
				];
				setLogs(test_logs);
			}
		}, 10000);
	}, []);

	useEffect(() => {
		socket.onopen = () => {
			console.log("logs socket opened");
			const newLog = {
				time: new Date().toLocaleString(),
				type: "info",
				message: "Logs websocket was opened",
			};
			setLogs([...logs, newLog]);
		};

		socket.onmessage = (e) => {
			console.log(new Date().toLocaleString());
			const newLog = JSON.parse(e.data);
			const formattedNewLog = {
				time: new Date().toLocaleString(),
				type: getType(newLog.type),
				message: newLog.message
			}
			logBuffer.push(formattedNewLog)
			setLogs([...logBuffer]);
		};

		socket.onclose = () => {
			console.log("logs socket closed");
			const newLog = {
				time: new Date().toLocaleString(),
				type: "error",
				message: "Logs websocket was closed",
			};
			setLogs([...logs, newLog]);
		};

		socket.onerror = (e) => {
			console.log("logs socket error");
			const newLog = {
				time: new Date().toLocaleString(),
				type: "error",
				message: "Logs websocket error: " + e,
			};
			setLogs([...logs, newLog]);
		};
	}, [socket]);

	const filterLogs = (types: string[]) => {
		if (types.length === 0) setFilteredLogs(logs);
		else setFilteredLogs(logs.filter((log) => types.includes(log.type)));
	};

	const changeFilter = (type: string, add: boolean) => {
		if (add) {
			if (!filters.includes(type)) setFilters([...filters, type]);
		} else {
			setFilters(filters.filter((filter) => filter !== type));
		}
	};

	useEffect(() => {
		filterLogs(filters);
	}, [filters, logs]);

	return [filteredLogs, changeFilter] as const;
}

export default useLogs;
