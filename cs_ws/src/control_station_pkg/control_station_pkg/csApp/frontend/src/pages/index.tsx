/***
 * This file is used to export all the pages in the application.
 * This is done to make it easier to import pages in other files.
 */

import Home from "./home";
import Navigation from "./navigation";
import HandlingDevice from "./handlingDevice";
import ManualTask from "./manualNavigation";
import Science from "./science";
import Logs from "./logs";
import Camera from "./camera";
import Menu from "./menu";
import NotFound from "./notFound";
import Drill from "./drill";

export const DefaultPage = () => <Home />;

export {
	Home,
	Navigation,
	HandlingDevice,
	ManualTask,
	Science,
	Logs,
	Camera,
	Menu,
	NotFound,
	Drill,
};
