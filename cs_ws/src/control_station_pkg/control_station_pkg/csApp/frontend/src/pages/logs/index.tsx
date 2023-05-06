import React, { useEffect, useRef } from "react";
import BackButton from "../../components/BackButton";
import Background from "../../components/Background";
import styles from "./style.module.sass";
import LogFilter from "../../components/LogFilter";
import { Themes } from "../../utils/themes";
import useLogs from "../../hooks/logsHook";

export default () => {
	const [mode, setMode] = React.useState("logs");
	const bottomRef = useRef<HTMLDivElement | null>(null);
	const [logs, changeFilter] = useLogs();

	useEffect(() => {
		// 👇️ scroll to bottom every time messages change
		bottomRef.current?.scrollIntoView({ behavior: "smooth" });
	}, [logs]);

	const getColorType = (type: string) => {
		switch (type) {
			case "info":
				return styles.Info;
			case "warning":
				return styles.Warning;
			case "error":
				return styles.Error;
			default:
				return styles.Data;
		}
	};

	if (mode === "logs") {
		return (
			<div className="page center">
				<Background />
				<BackButton />
				<div className={styles.TabContainer}>
					<div className={styles.TabHeader}>
						<div
							className={`${styles.TabButton} ${styles.Active}`}
							onClick={() => setMode("logs")}
						>
							Logs
						</div>
						<div
							className={`${styles.TabButton} ${styles.Inactive}`}
							onClick={() => setMode("console")}
						>
							Console
						</div>
					</div>
					<div className={styles.TabContent}>
						<div className={styles.LogFilters}>
							<LogFilter
								name="Info"
								color={Themes.GREY}
								onActivate={() => {
									changeFilter("info", true);
								}}
								onDisactivate={() => {
									changeFilter("info", false);
								}}
							/>
							<LogFilter
								name="Data"
								color={Themes.BROWN}
								onActivate={() => {
									changeFilter("data", true);
								}}
								onDisactivate={() => {
									changeFilter("data", false);
								}}
							/>
							<LogFilter
								name="Warning"
								color={Themes.ORANGE}
								onActivate={() => {
									changeFilter("warning", true);
								}}
								onDisactivate={() => {
									changeFilter("warning", false);
								}}
							/>
							<LogFilter
								name="Error"
								color={Themes.RED}
								onActivate={() => {
									changeFilter("error", true);
								}}
								onDisactivate={() => {
									changeFilter("error", false);
								}}
							/>
						</div>
						<div className={styles.Logs}>
							{logs.map((log) => (
								<div className={styles.Log}>
									<div className={styles.LogTime}>[{log.time}]</div>
									<div className={`${styles.LogType} ${getColorType(log.type)}`}>
										{log.type}
									</div>
									<div className={styles.LogMessage}>{log.message}</div>
								</div>
							))}
							<div ref={bottomRef}></div>
						</div>
					</div>
				</div>
			</div>
		);
	} else {
		return (
			<div className="page center">
				<Background />
				<BackButton />
				<div className={styles.TabContainer}>
					<div className={styles.TabHeader}>
						<div
							className={`${styles.TabButton} ${styles.Inactive}`}
							onClick={() => setMode("logs")}
						>
							Logs
						</div>
						<div
							className={`${styles.TabButton} ${styles.Active}`}
							onClick={() => setMode("console")}
						>
							Console
						</div>
					</div>
					<div className={styles.TabContent}></div>
				</div>
			</div>
		);
	}
};
