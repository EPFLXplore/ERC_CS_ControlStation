import React, { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";
import styles from "./style.module.sass";
Chart.register(...registerables);

interface GraphProps {
	measure: { x: number; y: number }[];
	pointsSecondWave: { x: number; y: number }[];
	candidates: { percentage: number; element: string }[];
}

export const WaveGraph: React.FC<GraphProps> = ({ measure, pointsSecondWave, candidates }) => {
	const chartRef = useRef<HTMLCanvasElement | null>(null);
	const chartInstanceRef = useRef<Chart | null>(null);

	useEffect(() => {
		if (chartRef.current) {
			const ctx = chartRef.current.getContext("2d");

			if (ctx) {
				if (chartInstanceRef.current) {
					chartInstanceRef.current.destroy();
				}

				chartInstanceRef.current = new Chart(ctx, {
					type: "line",
					data: {
						labels: measure.map((_, index) => index.toString()),
						datasets: [
							{
								label: "Measure",
								data: measure.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "red",
							},
							{
								label: "Closest candidate",
								data: pointsSecondWave.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "blue",
							},
						],
					},
					options: {
						responsive: true,
						scales: {
							x: {
								display: true,
							},
							y: {
								display: true,
							},
						},
					},
				});
			}
		}

		return () => {
			if (chartInstanceRef.current) {
				chartInstanceRef.current.destroy();
			}
		};
	}, [measure, pointsSecondWave]);

	return (
		<div className={styles.GraphContainer}>
			<div className={styles.text}>
				<p>
					{candidates[0].percentage}%, {candidates[0].element}
				</p>
			</div>
			<canvas ref={chartRef} />
		</div>
	);
};
