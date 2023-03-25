import { useState, useEffect } from "react";

function useMenuSelector(item: number) {
	const [menusOpen, setIsOpen] = useState<Array<boolean>>(new Array(item).fill(false));

	/**
	 * Allow only one menu to be open at a time
	 * @param index the index of the menu to open, all other menus will be closed (`-1` to close all)
	 */
	function openMenu(index: number): void {
		if (!menusOpen[index]) {
			setIsOpen(menusOpen.map((menu, i) => (i === index ? true : false)));
		}
	}

	return [menusOpen, openMenu] as const;
}

export default useMenuSelector;
