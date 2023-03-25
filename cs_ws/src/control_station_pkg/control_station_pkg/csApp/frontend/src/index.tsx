import React from "react";
import ReactDOM from "react-dom/client";

import "./styles/_global.sass";
import "./styles/_typography.sass";

import * as serviceWorkerRegistration from "./serviceWorkerRegistration";
import reportWebVitals from "./reportWebVitals";

import { Provider } from "react-redux";
import store from "./redux";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import { Home, Menu, Navigation, HandlingDevice, Science, Camera, Logs, NotFound } from "./pages";
import { Mode } from "./utils/mode.type";

const router = createBrowserRouter([
	{
		path: "/",
		element: <Home />,
	},
	{
		path: "/menu",
		element: <Menu />,
	},
	{
		path: "/navigation/auto",
		element: <Navigation mode={Mode.AUTONOMOUS} />,
	},
	{
		path: "/navigation/semi-auto",
		element: <Navigation mode={Mode.SEMI_AUTONOMOUS} />,
	},
	{
		path: "/navigation/manual",
		element: <Navigation mode={Mode.MANUAL} />,
	},
	{
		path: "/handlingDevice/auto",
		element: <HandlingDevice mode={Mode.AUTONOMOUS} />,
	},
	{
		path: "/handlingDevice/manual",
		element: <HandlingDevice mode={Mode.MANUAL} />,
	},
	{
		path: "/science/data",
		element: <Science />,
	},
	{
		path: "/science/drill",
		element: <Science />,
	},
	{
		path: "/camera",
		element: <Camera />,
	},
	{
		path: "/logs",
		element: <Logs />,
	},
	{
		path: "*",
		element: <NotFound />,
	},
]);

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(
	<React.StrictMode>
		<Provider store={store}>
			<RouterProvider router={router} />
		</Provider>
	</React.StrictMode>
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://cra.link/PWA
serviceWorkerRegistration.register();

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
