import { useState } from "react";
import styles from "./style.module.sass";

const ButtonSelector = ({ availableButtons, buttonSelect }: {availableButtons: number[]; buttonSelect: (button: number) => void}) => {
    const [menu, setMenu] = useState<number>()

    if(menu === 0) {
	    return (
		    <div className={styles.container}>
                <div className={styles.Menu}>
                    <button onClick={() => setMenu(1)}>{"<"}</button>
                    <p>Tasks</p>
                    <button onClick={() => setMenu(1)}>{">"}</button>
                </div>
                <button
                    className={availableButtons[0] == 1 ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(100)}
                >
                    Switch A 1
                </button>
                <button
                    className={availableButtons[1] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(101)}
                >
                    Switch A 2
                </button>
                <button
                    className={availableButtons[2] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(102)}
                >
                    Switch A 3
                </button>
                <button
                    className={availableButtons[3] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(103)}
                >
                    Switch A 4
                </button>
                <button
                    className={availableButtons[4] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(104)}
                >
                    Switch A 5
                </button>
                <button
                    className={availableButtons[5] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(105)}
                >
                    Switch A 6
                </button>
                <button
                    className={availableButtons[6] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(106)}
                >
                    Switch A 7
                </button>
                <button
                    className={availableButtons[7] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(107)}
                >
                    Switch A 8
                </button>
                <button
                    className={availableButtons[8] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(108)}
                >
                    Switch A 9
                </button>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(109)}
                >
                    Switch A 10
                </button>
                <button
                    className={availableButtons[10] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(10)}
                >
                    Button Switch ON
                </button>
                <button
                    className={availableButtons[11] == 1 ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(11)}
                >
                    Metallic Plate
                </button>
                <button
                    className={availableButtons[12] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(12)}
                >
                    Magnet
                </button>
                <button
                    className={availableButtons[10] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(13)}
                >
                    Button Switch OFF
                </button>
                <button
                    className={availableButtons[13] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(20)}
                >
                    Voltmeter 1
                </button>
                <button
                    className={availableButtons[13] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(21)}
                >
                    Voltmeter 2
                </button>
                <button
                    className={availableButtons[14] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(30)}
                >
                    Ethernet Socket
                </button>
                <button
                    className={availableButtons[15] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(31)}
                >
                    Ethernet Cable
                </button>
                <button
                    className={styles.button}
                    onClick={() => buttonSelect(40)}
                >
                    Pick Rock
                </button>
                <button
                    className={styles.button}
                    onClick={() => buttonSelect(41)}
                >
                    Rassor Sample
                </button>
                <button
                    className={styles.button}
                    onClick={() => buttonSelect(70)}
                >
                    Align Panel B1
                </button>
                <button
                    className={styles.button}
                    onClick={() => buttonSelect(71)}
                >
                    Align Panel A
                </button>
                <button
                    className={styles.button}
                    onClick={() => buttonSelect(72)}
                >
                    Align Panel B2
                </button>
                <button
                    className={availableButtons[0] == 1 ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(110)}
                >
                    Switch A 1 OFF
                </button>
                <button
                    className={availableButtons[1] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(111)}
                >
                    Switch A 2 OFF
                </button>
                <button
                    className={availableButtons[2] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(112)}
                >
                    Switch A 3 OFF
                </button>
                <button
                    className={availableButtons[3] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(113)}
                >
                    Switch A 4 OFF
                </button>
                <button
                    className={availableButtons[4] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(114)}
                >
                    Switch A 5 OFF
                </button>
                <button
                    className={availableButtons[5] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(105)}
                >
                    Switch A 6 OFF
                </button>
                <button
                    className={availableButtons[6] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(116)}
                >
                    Switch A 7 OFF
                </button>
                <button
                    className={availableButtons[7] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(117)}
                >
                    Switch A 8 OFF
                </button>
                <button
                    className={availableButtons[8] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(118)}
                >
                    Switch A 9 OFF
                </button>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(119)}
                >
                    Switch A 10 OFF
                </button>
            </div>
        );
    } else {
        return (
            <div className={styles.container}>
                <div className={styles.Menu}>
                    <button onClick={() => setMenu(0)}>{"<"}</button>
                    <p>Positions</p>
                    <button onClick={() => setMenu(0)}>{">"}</button>
                </div>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(50)}
                >
                    Useless Home
                </button>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(51)}
                >
                    Optimal View (Home)
                </button>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(52)}
                >
                    Zero
                </button>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(53)}
                >
                    Face Ground
                </button>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(54)}
                >
                    Science Drop
                </button>
                <button
                    className={availableButtons[9] == 1  ? styles.button : styles.disabledButton}
                    onClick={() => buttonSelect(55)}
                >
                    Back
                </button>
            </div>
            );
    }
};

export default ButtonSelector;
