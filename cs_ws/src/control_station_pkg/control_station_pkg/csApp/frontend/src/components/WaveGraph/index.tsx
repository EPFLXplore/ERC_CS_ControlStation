import React, { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";
import styles from "./style.module.sass";
Chart.register(...registerables);

interface GraphProps {
	pointsFirstWave: { x: number; y: number }[];
	pointsSecondWave: { x: number; y: number }[];
	percentage: number;
	mainComponent: string;
}

export const WaveGraph: React.FC<GraphProps> = ({
	pointsFirstWave,
	pointsSecondWave,
	percentage,
	mainComponent,
}) => {
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
						labels: pointsFirstWave.map((_, index) => index.toString()),
						datasets: [
							{
								label: "1st Graph",
								data: pointsFirstWave.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "blue",
							},
							{
								label: "2nd Graph",
								data: pointsSecondWave.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "red",
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
	}, [pointsFirstWave, pointsSecondWave]);

	return (
		<div className={styles.GraphContainer}>
			<p className={styles.text}>
				{percentage}%, {mainComponent}
			</p>
			<canvas ref={chartRef} />
		</div>
	);
};
