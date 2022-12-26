from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

class TextToImage:
    def __init__(self, name, font_size, font_color_r,font_color_g,font_color_b, pos_x, pos_y):
        self.name       = name
        self.font_size  = int(font_size)
        self.font_color = (int(font_color_r), int(font_color_g), int(font_color_b))
        self.pos_x      = int(pos_x)
        self.pos_y      = int(pos_y)
        self.font_path = r"C:\Reposytory\python\easy_udonarium_env\Input\uzura.ttf"

    # def __init__(self, font_size, font_color, pos_x, pos_y, font_path):
    #     self.font_size  = font_size
    #     self.font_color = font_color
    #     self.pos_x      = pos_x
    #     self.pos_y      = pos_y
    #     self.font_path  = font_path

    def add_text_to_image(self, img, text):
        position = (self.pos_x, self.pos_y)

        font = ImageFont.truetype(self.font_path, self.font_size)
        draw = ImageDraw.Draw(img)

        draw.text(position, text, self.font_color, font=font)

        return img

    def print_info(self):
        print(self.name  )
        print(self.font_size  )
        print(self.font_color )
        print(self.pos_x      )
        print(self.pos_y      )
        print(self.font_path  )


if __name__ == '__main__':
    print("this is module. dont excute")
# def add_text_to_image(img, text,  font_size, font_color, height, width, max_length=740, font_path=r'C:\Reposytory\python\easy_udonarium_env\ImageMaker\test\test_back.jpg'):
#     position = (width, height)
#     font = ImageFont.truetype(font_path, font_size)
#     draw = ImageDraw.Draw(img)

#     draw.text(position, text, font_color, font=font)

#     return img


# base_img = Image.open(base_img_path).copy()

# card_text = "金+2"
# font_path = r'C:\Reposytory\python\easy_udonarium_env\ImageMaker\test\uzura.ttf'
# font_size = 80
# height = 244
# width = 380
# # img = add_text_to_image(base_img, card_text, font_path, font_size, font_color, height, width)


# font_color = (253, 197, 66)
# cost_font_size = 40
# cost_y = 50
# cost_x = 440
# img = add_text_to_image(base_img, "20\n3", font_path, font_size, font_color, cost_y, cost_x)
# img = add_text_to_image(base_img, "20\n3", font_path, font_size, font_color, 630, 50)
# img.save(r'C:\Reposytory\python\easy_udonarium_env\ImageMaker\test\test.png')