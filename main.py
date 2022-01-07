import process_auc_scan_data as pg
import handle_windows as hw
from window_capture import WindowCapture
import shutil
from datetime import datetime
import plot_data as pd

#pg.process_scan_folder('C:/Users/Mikey/PycharmProjects/AuctionBot_v2/scan_data/')

#pd.load_item('C:/Users/Mikey/PycharmProjects/AuctionBot_v2/processed_data/2021_11_20_10_17_44_data.json', "Froststoff")
pd.plot_prices(pd.load_specific_items('C:/Users/Mikey/PycharmProjects/AuctionBot_v2/processed_data/', "Froststoff"))

'''while True:
    round = 1
    print("Round: " + str(round))
    now = datetime.now()
    dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
    hw.start_wow('F:\Wow-Lab\WoW_Wotlk\Wow.exe')
    hw.login_wow()
    wow_client = WindowCapture('World of Warcraft')
    hw.open_ah_window(wow_client)
    hw.start_ah_scan(wow_client)
    hw.kill_wow()
    time.sleep(10)
    shutil.move('F:/Wow-Lab/WoW_Wotlk/WTF/Account/LETTUCEISNOTENOU/SavedVariables/Auc-ScanData.lua', 'scan_files/' + dt_string + ".lua")
    round = round + 1'''