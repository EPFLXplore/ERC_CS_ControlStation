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
						labels: [460,480,500,520,540,660,680,700,720,740,860,880,900,920,940],
						datasets: [
							{
								label: "Current measure",
								data: measure.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "red",
								stepped: false,
							},
							{
								label: "Closest candidate",
								data: pointsSecondWave.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "#6F8FAF",
								stepped: false,
							},
						],
					},
					options: {
						responsive: true,
						scales: {
							x: {
								display: true,
								title: {
									display: true,
									text: "Wavelength (nm)",
									color: "white",
									font: {
										size: 20,
									},
								},
							},
							y: {
								display: true,
								max: 10,
								min: 0,
								title: {
									display: true,
									text: "Reflectance (%)",
									color: "white",
									font: {
										size: 20,
									},
								},
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
