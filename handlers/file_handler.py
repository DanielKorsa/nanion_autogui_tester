import os
import pprint

#GUI_ELEMENTS_DIR = 'C:\\dev\\nanion_autogui_tester\\00_test_data\\button_imgs'

def element_dict(dir_path):

    image_list = os.listdir(dir_path)
    #element_list = {}
    element_dict = {}
    for file in image_list:
        if file.endswith(".png"):
            element_dict [file.split('.')[0]] = {'path' : os.path.join(dir_path, file)}
            #element_dict[file.split('.')[0]] = os.path.join(dir_path, file)
            #element_list.append(element_dict)
            #? For creating a list
        else:
            continue

    return element_dict


#pprint.pprint(element_dict(GUI_ELEMENTS_DIR))

def gui_element(name, element_dict):

    if name in element_dict:
        return element_dict[name]['path']

    else:
        return AttributeError