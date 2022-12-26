import csv
import TextToImage as t2i
from PIL import Image

info_end_text = 'position_info_end'
card_data_start_text = 'data_start'
base_img_path = r"C:\Reposytory\python\easy_udonarium_env\Input\test_back.jpg"
output_path = r"C:\Reposytory\python\easy_udonarium_env\Output"
# WANT: 1行目infoからどこに何の情報があるか切り分ける
def make_image_makers(filename) :
    text_write_infos = []
    print_info = []
    with open(filename, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        text_write_infos = _get_image_infos(csvreader)
        print_info = _get_card_info(csvreader)


    for card in print_info:
        counter = 0
        img = Image.open(base_img_path).copy()
        out = output_path + "\\" + card[counter] + '.png'
        for info in text_write_infos:
            counter += 1
            img = info.add_text_to_image(img, card[counter])
        print(out)
        img.save(out)

def _get_image_infos(csv_data):
    t2i_infos = []
    start = 1
    for row in csv_data:
        if start == 1 :
            start = 0 
            continue
        if row[0] == info_end_text:
            break
        info = _decode_as_image_maker(row)
        t2i_infos.append(info)
    return t2i_infos

def _get_card_info(csv_data):
    card_infos = []
    start = 0
    for row in csv_data:
        if start == 0 or row[0] == card_data_start_text:
            start = 1 if row[0] == card_data_start_text else 0
            continue
        card_infos.append(row)
    return card_infos


def _decode_as_image_maker(row):
    name        = row[0]
    font_size   = row[1]
    font_color_r = row[4]
    font_color_g = row[5]
    font_color_b = row[6]
    pos_x       = row[2]
    pos_y       = row[3]
    text_to_image = t2i.TextToImage(name, font_size, font_color_r,font_color_g,font_color_b, pos_x, pos_y)
    return text_to_image

make_image_makers(r'C:\Reposytory\python\easy_udonarium_env\Input\card_info.csv')