import { createBoard } from "@wixc3/react-board";
import Home from "../../pages/home";

export default createBoard({
	name: "Home",
	Board: () => (
		<div>
			<Home />
		</div>
	),
});
