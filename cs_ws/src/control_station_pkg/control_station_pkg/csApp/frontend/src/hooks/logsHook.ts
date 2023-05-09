import React from "react";
import { useEffect, useState } from "react";

export type Log = {
	time: string;
	type: string;
	message: string;
};

function useLogs() {
	const [logs, setLogs] = useState<Log[]>([]);
	const [filters, setFilters] = React.useState<string[]>([]);
	const [filteredLogs, setFilteredLogs] = React.useState<Log[]>([]);

	useEffect(() => {
		let logsSocket = new WebSocket("ws://" + window.location.host + "/ws/csApp/log/");

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

		logsSocket.onopen = () => {
			console.log("logs socket opened");
			const newLog = {
				time: new Date().toLocaleString(),
				type: "info",
				message: "Logs websocket was opened",
			};
			setLogs([...logs, newLog]);
		};

		logsSocket.onmessage = (e) => {
			const newLog = JSON.parse(e.data);
			console.log(e);
			setLogs([...logs, newLog]);
		};

		logsSocket.onclose = () => {
			console.log("logs socket closed");
			const newLog = {
				time: new Date().toLocaleString(),
				type: "error",
				message: "Logs websocket was closed",
			};
			setLogs([...logs, newLog]);
		};

		logsSocket.onerror = (e) => {
			console.log("logs socket error");
			const newLog = {
				time: new Date().toLocaleString(),
				type: "error",
				message: "Logs websocket error: " + e,
			};
			setLogs([...logs, newLog]);
		};
	}, []);

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
