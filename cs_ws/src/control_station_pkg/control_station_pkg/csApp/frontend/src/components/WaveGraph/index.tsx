import React, { useEffect, useRef } from "react";
import { Chart, registerables } from "chart.js";
Chart.register(...registerables);

interface GraphProps {
	pointsFirstWave: { x: number; y: number }[];
	pointsSecondWave: { x: number; y: number }[];
}

export const WaveGraph: React.FC<GraphProps> = ({ pointsFirstWave, pointsSecondWave }) => {
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
								label: "Wave Graph",
								data: pointsFirstWave.map((point) => ({ x: point.x, y: point.y })),
								fill: false,
								borderColor: "blue",
							},
							{
								label: "Wave Graph",
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

	return <canvas ref={chartRef} />;
};
