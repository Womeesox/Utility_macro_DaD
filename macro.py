from pynput import Button, Controller
from time import sleep
import mss

time_between_clicks = 1.0

mouse = Controller()

merchants_tab_button_position = ()
quest_button_position = ()

"""
# merchant_name: [merchants_tab_screen_pos, amount_of_quest_groups, ...]
0: screen position 2 element tuple of the merchant in merchants tab
1: amount of quest groups of the merchant
"""
merchant_info_dict = {}

def click_on_pos(pos):
    mouse.position = pos
    mouse.click(Button.left, 1)

def scan_quests():
    click_on_pos(merchant_info_dict)
    sleep(time_between_clicks)

    for merchant in merchant_info_dict:
        click_on_pos(merchant_info_dict[merchant][0])
        sleep(time_between_clicks)
        click_on_pos(quest_button_position)
        
