const menuLinks = {
	Navigation: [
		{
			name: "Autopilot",
			url: "/navigation/auto",
		},
		// {
		// 	name: "Semiautopilot",
		// 	url: "/navigation/semi-auto",
		// },
		{
			name: "Manual",
			url: "/manual-control?defaultMode=nav",
		},
	],
	Science: [
		{
			name: "Data",
			url: "/science/data",
		},
		{
			name: "Drill",
			url: "/science/drill",
		},
	],
	"Handling Device": [
		{
			name: "Autopilot",
			url: "/handlingDevice/auto",
		},
		{
			name: "Manual",
			url: "/manual-control?defaultMode=hd",
		},
	],
	Information: [
		{
			name: "Logs",
			url: "/logs",
		},
		{
			name: "Camera",
			url: "/camera",
		},
	],
};

export default menuLinks;
