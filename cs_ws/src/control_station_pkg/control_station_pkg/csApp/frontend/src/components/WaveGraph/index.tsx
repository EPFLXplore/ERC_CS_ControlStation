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
								label: "Current measure",
								data: measure.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "red",
							},
							{
								label: "Closest candidate",
								data: pointsSecondWave.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "#6F8FAF",
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
								max: 10,
								min: 0,
							},
						},
						animation: {
							duration: 0,
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
				<h3>
					{candidates[0].percentage}%, {candidates[0].element}
				</h3>
			</div>
			<canvas ref={chartRef} />
		</div>
	);
};
