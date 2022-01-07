import os
import time
import pyautogui
import subprocess
import cv2

#ToDo: Write setup-function, where the templates are being created. 1. Use snipping tool, to screenshot the needed areas (the auctioneer and the start button) -> watch out for .png and .jpg endings!! 2. Opportunity to adjust the klicking position after matching the template.


def start_wow(path):
    subprocess.Popen(path)
    time.sleep(10)
    print("Wow client started.")
    #ToDo: Is there a opportunity to check if the Wow-client started?
    return


def kill_wow():
    # ToDo: Kill the window via process killing
    pyautogui.keyDown('alt')
    pyautogui.press('f4')
    pyautogui.keyUp('alt')

def relogg_wow():
    pyautogui.press('enter')
    time.sleep(0.5)
    pyautogui.write("/logout")
    time.sleep(0.5)
    pyautogui.press('enter')
    time.sleep(2)
    pyautogui.press('enter')
    # ToDo: Verify if successfully logged back in
    time.sleep(10)


def login_wow():
    username = 'lettuceisnotenou'
    password = 'RAgenefeiNAb'
    pyautogui.write(username)
    time.sleep(1)
    pyautogui.press('tab')
    pyautogui.write(password)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(4)
    # ToDo: Maybe implement a opportunity to choose the character by name
    # Take the default character
    pyautogui.press('enter')
    time.sleep(10)
    print("Successfully logged in.")
    return


def match_template(img, template, debug=False):
    '''methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
               cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]'''

    method = cv2.TM_CCOEFF
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    if debug:
        temp_h, temp_w = template.shape
        bottom_right = (location[0] + temp_w, location[1] + temp_h)
        cv2.rectangle(img2, location, bottom_right, 255, 1)
        cv2.imshow('Match', img2)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    return location


def open_ah_window(window_capture):
    screenshot = cv2.cvtColor(window_capture.get_screenshot(), cv2.COLOR_BGR2GRAY)
    screenshot2 = screenshot.copy()
    auctioneer_location = match_template(screenshot, cv2.imread('templates/auctioneer_1280_800.JPG', 0))
    auctioneer_location = window_capture.get_screen_position((auctioneer_location[0] + 50, auctioneer_location[1] + 50))
    pyautogui.moveTo(auctioneer_location)
    pyautogui.rightClick()
    time.sleep(3)
    #ToDo: Abfrage machen, ob Ah Fenster erfolgreich geöffnet wurde -> Template matching
    return screenshot


def start_ah_scan(window_capture):
    #ToDo: Is there a possibility to gain the scan data without frequently restarting the client? Possible: Through logout: "/logout"
    screenshot = cv2.cvtColor(window_capture.get_screenshot(), cv2.COLOR_BGR2GRAY)
    start_location = match_template(screenshot, cv2.imread('templates/start_scan_1280_800.JPG', 0))
    start_location = window_capture.get_screen_position((start_location[0] + 10, start_location[1] + 10))
    pyautogui.moveTo(start_location)
    pyautogui.leftClick()
    for i in range(720):
        # ToDo: Implement another possibility to check, whether the scan has finished (e.g. over the elapsed scanning percentage)
        time.sleep(1)
        print("Elapsed scan time: " + str(i))
    return

