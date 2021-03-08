#
from handlers import file_handler as fh
from handlers import gui_test_handler as gth


GUI_ELEMENTS_DIR = 'C:\\dev\\nanion_autogui_tester\\00_test_data\\button_imgs'

def init():

    # Resolution of a screen it was developed
    developer_resolution = (1920, 1080)
    screen_resolution = gth.get_screen_size()
    scrn_res_coef_x = developer_resolution[0] - screen_resolution[0]
    scrn_res_coef_y = developer_resolution[1] - screen_resolution[1]
    print(scrn_res_coef_x, scrn_res_coef_y)
    #TODO get screen resolution
    #TODO calculate difference

    global elements_imgs
    elements_imgs = fh.element_dict(GUI_ELEMENTS_DIR)
    print('Initialized')

def main():

    #TODO Start DC
    init()

    #! TESTCASE 1
    file_btn = gth.find_gui_element(fh.gui_element('file', elements_imgs))
    gth.cursor_move(file_btn)
    gth.click()
    print(file_btn)


if __name__ == "__main__":
    main()