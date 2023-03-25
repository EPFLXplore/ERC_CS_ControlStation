import { createBoard } from "@wixc3/react-board";
import NotFound from "../../pages/notFound";

export default createBoard({
	name: "NotFound",
	Board: () => (
		<div>
			<NotFound />
		</div>
	),
});
