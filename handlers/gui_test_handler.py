
import time
from PIL.ImageOps import grayscale
import pyautogui as gui
# from PIL import ImageGrab
# from functools import partial
# ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


gui.FAILSAFE = False

def get_screen_size():
    """[Get size of the screen]

    Returns:
        [tuple]: [screenWidth & screenHeigth]
    """
    return gui.size()

def cursor_move(coordinates):
    """[Move cursor to x/y coordinates]

    Args:
        coordinates ([tuple]): [x y coordinates]

    Returns:
        [type]: [description]
    """
    time.sleep(1)
    gui.moveTo(coordinates)
    time.sleep(1)

    return coordinates


def click(click_type = 'single'):
    """[Make mouse click]

    Args:
        click_type (str, optional): [Single / Double]. Defaults to 'single'.
    """
    if click_type == 'single':
        gui.click()
    else:
        gui.doubleClick()


def delay_s(seconds):
    """[Delay between clics/writes]

    Args:
        seconds ([int]): [Delay time in seconds]
    """
    time.sleep(seconds)


def enter_form_value(form_text):
    """[Enters value in a text field]

    Args:
        form_text ([str]): [Value to write]
    """
    gui.typewrite(form_text)


def find_gui_element(element_img_path):

    coordinates = gui.locateCenterOnScreen(element_img_path, grayscale=False)

    return coordinates


# def enapss_insert_pass_img_rec(password):
#     """[This is a more complicated way of unlocking Enpass.
#     Find text field and button by recognizing template imgs]
#     Args:
#         password ([str]): [Enpass Master password]
#     """
#     # Get coordinates of "Passford text input field"
#     for i in range(3):
#         psw_txt_field_coords = pag.locateCenterOnScreen('TEST/text_field.png') # must be .png
#         if psw_txt_field_coords is None:
#             print('Try {}'.format(i))
#         else:
#             break
#     # Get coordinates of textfield
#     x_psw, y_psw = psw_txt_field_coords
#     pag.leftClick(x_psw/2, y_psw/2)
#     pag.typewrite(password) # Write pass in text field
#     # Get coordinate os "Unlock" button
#     unlock_btn_coords = pag.locateCenterOnScreen('TEST/unlock_button.png')
#     x_btn, y_btn = unlock_btn_coords
#     pag.leftClick(x_btn/2, y_btn/2) # Click button









