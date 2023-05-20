import React, { useEffect, useRef } from "react";
import styles from "./style.module.sass";

interface TableProps {
	lines: { id: string; content: number }[];
}

export const Table = ({ lines }: TableProps) => {
	return (
		<table className={styles.table}>
			<thead>
				<tr>
					<th>Element</th>
					<th>Value</th>
				</tr>
			</thead>
			<tbody>
				{lines.map((line) => (
					<tr key={line.id}>
						<td>{line.id}</td>
						<td>{line.content}</td>
					</tr>
				))}
			</tbody>
		</table>
	);
};
