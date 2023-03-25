import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";

export default () => {
	const [mode, setMode] = React.useState("logs");

	if (mode === "logs") {
		return (
			<div className="page center">
				<Background />
				<BackButton />
				<h1>Logs</h1>
			</div>
		);
	} else {
		return (
			<div className="page center">
				<Background />
				<BackButton />
				<h1>Home</h1>
			</div>
		);
	}
};
