import React from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import WorkInProgress from "../../components/WorkInProgress";

export default () => {
	return (
		<div className="page">
			<Background />
			<BackButton />
			<WorkInProgress />
		</div>
	);
};
