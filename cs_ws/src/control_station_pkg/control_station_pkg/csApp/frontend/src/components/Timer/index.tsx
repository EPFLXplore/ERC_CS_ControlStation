import React, { useEffect, useState } from "react";
import styles from "./style.module.sass";
import { Status } from "../../utils/status.type";
import PlayArrowIcon from "@mui/icons-material/PlayArrowRounded";
import PauseIcon from "@mui/icons-material/PauseRounded";
import Replay10Icon from "@mui/icons-material/Replay10Rounded";
import PersonIcon from "@mui/icons-material/PersonRounded";
import PeopleAltRoundedIcon from "@mui/icons-material/PeopleAltRounded";
import {
	Battery2Bar,
	Battery0Bar,
	Battery1Bar,
	Battery3Bar,
	Battery4Bar,
	Battery5Bar,
	Battery6Bar,
	BatteryFullRounded,
} from "@mui/icons-material";
import { Size } from "../../utils/size.type";
import useTimer from "../../hooks/timerHooks";

const Timer = ({
	end,
	onFinished,
	status = Status.IDLE,
	connection = 1,
	battery = 100,
	size = Size.LARGE,
}: {
	end: EpochTimeStamp;
	onFinished?: () => void;
	status?: Status;
	connection?: number;
	battery?: number;
	size?: Omit<Size, Size.MEDIUM>;
}) => {
	const [minutes, seconds, active, changeTime, setActive] = useTimer(onFinished);
	const [controls, setControls] = useState(false);

	//SMALL SIZE TIMER
	if (size === Size.SMALL)
		return (
			<div
				className={styles.timerSmall}
				onMouseEnter={() => {
					setControls(true);
				}}
				onMouseLeave={() => setControls(false)}
			>
				<div className={styles.time}>
					<input
						type="text"
						maxLength={2}
						value={timeRepresentation(minutes, active)}
						onFocus={(e) => {
							e.target.value = "";
							setActive(false);
						}}
						onBlur={(e) => {
							if (e.target.value === "") {
								changeTime(0, seconds);
							}
							setActive(true);
						}}
						onChange={(e) => changeTime(parseInt(e.target.value), seconds)}
						className={styles.input}
					/>
					<p className={styles.comma}>:</p>
					<input
						type="text"
						maxLength={2}
						value={timeRepresentation(seconds, active)}
						onFocus={(e) => {
							e.target.value = "";
							setActive(false);
						}}
						onBlur={(e) => {
							if (e.target.value === "") {
								changeTime(minutes, 0);
							}
							setActive(true);
						}}
						onChange={(e) => changeTime(minutes, parseInt(e.target.value))}
						className={styles.input}
					/>
					<p className={styles.status} />
				</div>
				{controls && (
					<div className={styles.controls}>
						<button className={styles.button} onClick={() => setActive(!active)}>
							{active ? (
								<PauseIcon className={styles.icon} />
							) : (
								<PlayArrowIcon className={styles.icon} />
							)}
						</button>
						<button
							className={styles.button}
							onClick={() => changeTime(minutes, seconds + 10)}
						>
							<Replay10Icon className={styles.icon} />
						</button>
					</div>
				)}
			</div>
		);

	//LARGE SIZE TIMER
	return (
		<div className={styles.timer}>
			<div className={styles.batteryInfos}>
				<p className={styles.battery}>{battery}%</p>
				<div className={styles.batteryIcon}>{getBatteryState(battery)}</div>
			</div>
			<div className={styles.timeInfos}>
				<div className={styles.time}>
					<input
						type="text"
						maxLength={2}
						value={timeRepresentation(minutes, active)}
						onFocus={(e) => {
							e.target.value = "";
							setActive(false);
						}}
						onBlur={(e) => {
							if (e.target.value === "") {
								changeTime(0, seconds);
							}
							setActive(true);
						}}
						onChange={(e) => changeTime(parseInt(e.target.value), seconds)}
						className={styles.input}
					/>
					<p className={styles.comma}>:</p>
					<input
						type="text"
						maxLength={2}
						value={timeRepresentation(seconds, active)}
						onFocus={(e) => {
							e.target.value = "";
							setActive(false);
						}}
						onBlur={(e) => {
							if (e.target.value === "") {
								changeTime(minutes, 0);
							}
							setActive(true);
						}}
						onChange={(e) => changeTime(minutes, parseInt(e.target.value))}
						className={styles.input}
					/>
					<p className={styles.status} />
				</div>
				<div className={styles.controls}>
					<button className={styles.button} onClick={() => setActive(!active)}>
						{active ? (
							<PauseIcon className={styles.icon} />
						) : (
							<PlayArrowIcon className={styles.icon} />
						)}
					</button>
					<button
						className={styles.button}
						onClick={() => changeTime(minutes, seconds + 10)}
					>
						<Replay10Icon className={styles.icon} />
					</button>
				</div>
			</div>
			<div className={styles.connections}>
				<p className={styles.connectionsText}>{connection}</p>
				<div className={styles.connectionsIcon}>
					{connection > 1 ? (
						<PeopleAltRoundedIcon className={styles.icon} />
					) : (
						<PersonIcon className={styles.icon} />
					)}
				</div>
			</div>
		</div>
	);
};

export default Timer;

////////////////////////////METHODS///////////////////////////

const timeRepresentation = (time: number, active = true) => {
	if (time < 10 && active) {
		return `0${time}`;
	} else {
		return time.toString();
	}
};

const getBatteryState = (battery: number) => {
	if (battery < 12.5) {
		return <Battery0Bar className={styles.icon} />;
	} else if (battery < 25) {
		return <Battery1Bar className={styles.icon} />;
	} else if (battery < 37.5) {
		return <Battery2Bar className={styles.icon} />;
	} else if (battery < 50) {
		return <Battery3Bar className={styles.icon} />;
	} else if (battery < 62.5) {
		return <Battery4Bar className={styles.icon} />;
	} else if (battery < 75) {
		return <Battery5Bar className={styles.icon} />;
	} else if (battery < 87.5) {
		return <Battery6Bar className={styles.icon} />;
	} else {
		return <BatteryFullRounded className={styles.icon} />;
	}
};
