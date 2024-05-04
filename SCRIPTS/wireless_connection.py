import routeros_api
import time
import curses
import json

def main(stdscr):

    data = []

    with open('arp_table.json', "r") as file:
        data = json.load(file)

    curses.start_color()
    curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_BLACK)
    
    stdscr.clear()
    curses.curs_set(0)
    stdscr.addstr(0, 0, "Connected Devices To Rover:")
    stdscr.refresh()

    connection = routeros_api.RouterOsApiPool('169.254.55.1', username='admin', password='',
                                            plaintext_login=True)
    api = connection.get_api()

    store_clients = []
    wireless_clients = []

    try:

        while True:
            wireless_clients = api.get_resource('/interface/wireless/registration-table').get()

            if(len(wireless_clients) != len(store_clients)):
                store_clients = wireless_clients
                stdscr.clear()
                stdscr.addstr(0, 0, "Connected Devices To Rover:")
                stdscr.refresh()
            else:
                store_clients = wireless_clients        


            if(len(store_clients) != 0):
        
                for idx, device in enumerate(store_clients):
                    signal_strength_ch0 = int(device.get('signal-strength-ch0'))
                    ip = device.get('last-ip')
                    mac_address_or_name = device.get('mac-address')
                    tx_rate = device.get('tx-rate')
                    rx_rate = device.get('rx-rate')

                    if mac_address_or_name in data:
                        mac_address_or_name = data[mac_address_or_name]

                    # depending on the strength of the signal, we use different colors
                    if(signal_strength_ch0 >= -42):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"███", curses.color_pair(1))
                        stdscr.addstr(2 * idx + 2, 67, f"███", curses.color_pair(2))
                        stdscr.addstr(2 * idx + 2, 70, f"███    ", curses.color_pair(3))

                    elif(signal_strength_ch0 <= -43 and signal_strength_ch0 >= -47):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"███", curses.color_pair(1))
                        stdscr.addstr(2 * idx + 2, 67, f"███", curses.color_pair(2))
                        stdscr.addstr(2 * idx + 2, 70, f"██     ", curses.color_pair(3))

                    elif(signal_strength_ch0 <= -48 and signal_strength_ch0 >= -50):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"███", curses.color_pair(1))
                        stdscr.addstr(2 * idx + 2, 67, f"███", curses.color_pair(2))
                        stdscr.addstr(2 * idx + 2, 70, f"█       ", curses.color_pair(3))

                    elif(signal_strength_ch0 <= -51 and signal_strength_ch0 >= -55):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"███", curses.color_pair(1))
                        stdscr.addstr(2 * idx + 2, 67, f"███     ", curses.color_pair(2))
                    
                    elif(signal_strength_ch0 <= -56 and signal_strength_ch0 >= -60):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"███", curses.color_pair(1))
                        stdscr.addstr(2 * idx + 2, 67, f"██      ", curses.color_pair(2))

                    elif(signal_strength_ch0 <= -61 and signal_strength_ch0 >= -65):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"███", curses.color_pair(1))
                        stdscr.addstr(2 * idx + 2, 67, f"█       ", curses.color_pair(2))

                    elif(signal_strength_ch0 <= -66 and signal_strength_ch0 >= -70):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"███     ", curses.color_pair(1))

                    elif(signal_strength_ch0 <= -71 and signal_strength_ch0 >= -75):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"██      ", curses.color_pair(1))

                    elif(signal_strength_ch0 <= -76 and signal_strength_ch0 >= -80):
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: {signal_strength_ch0} dBm")
                        stdscr.addstr(2 * idx + 2, 64, f"█       ", curses.color_pair(1))

                    else:
                        stdscr.addstr(2 * idx + 2, 0, f"{ip} / {mac_address_or_name} => Signal Strength: very low...")
                    
                    stdscr.addstr(2 * idx + 2, 77, f"tx-rate: {tx_rate} / rx-rate: {rx_rate}")
                    stdscr.refresh()

            else:
                stdscr.clear()
                stdscr.addstr(0, 0, "No devices connected to Rover")
                stdscr.refresh()


            time.sleep(1)

    except KeyboardInterrupt:
        print('Ctrl+C pressed. Exiting...')
    finally:
        connection.disconnect()


if __name__ == "__main__":
    curses.wrapper(main)


   