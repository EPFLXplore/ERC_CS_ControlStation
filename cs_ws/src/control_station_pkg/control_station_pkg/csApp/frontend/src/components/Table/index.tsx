import React, { useEffect, useRef } from "react";
import styles from "./style.module.sass";
import { Sensor } from "../../utils/sensor.type";

interface TableProps {
	values: number[];
	sensorType: Sensor;
}

const NPKComponents = ["Phosphate", "Azote", "Potassium"];
const ALLComponents = ["Humidity", "Temp", "Elec", "PH"];

export const Table = ({ values, sensorType }: TableProps) => {
	let lines: { id: string; content: number }[];

	if (sensorType === Sensor.NPK) {
		lines = values.map((value, index) => ({
			id: NPKComponents[index],
			content: value,
		}));
	} else {
		lines = values.map((value, index) => ({
			id: ALLComponents[index],
			content: value,
		}));
	}

	return (
		<div>
			<h2 className={styles.title}>{sensorType}</h2>
			<table className={styles.table}>
				<thead>
					<tr>
						<th>
							<text>Element</text>
						</th>
						<th>
							<text>Value</text>
						</th>
					</tr>
				</thead>
				<tbody>
					{lines.map((line) => (
						<tr key={line.id}>
							<td>
								<text>{line.id}</text>
							</td>
							<td>
								<text>{line.content}</text>
							</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
};
