from xml.etree.ElementTree import Element, SubElement, ElementTree

class DiceElement:
    def make_table_element(self, pos_x, pos_y) :
        dice = Element("dice-symbol")
        dice.set('location.name','table')
        dice.set('location.x',pos_x)
        dice.set('location.y',pos_y)
        dice.set('posZ','0')
        dice.set('face','1')
        dice.set('owner','')
        dice.set('rotate','0')

        dice_symbol_name =  Element("data")
        dice_symbol_name.set('name','dice-symbol')
        dice_symbol_name.append(self._make_image_element())
        dice_symbol_name.append(self._make_common_element())
        dice_symbol_name.append(self._make_detail_element())

        dice.append(dice_symbol_name)
        return dice
    
    def _make_image_element(self):
        image = Element("data")
        image.set('name','image')
        for i in range(1,7):
            dice_surface = SubElement(image, "data")
            dice_surface.set('type','image')
            dice_surface.set('name',str(i))
            dice_surface.text = r"./assets/images/dice/6_dice/6_dice["+str(i)+"].png"
        return image
    
    def _make_common_element(self):
        common = Element("data")
        common.set('name','common')
        common_name = SubElement(common, "data")
        common_name.set('name','name')
        common_name.text = 'D6'
        common_size = SubElement(common, "data")
        common_size.set('name','size')
        common_size.text = '1'
        return common

    def _make_detail_element(self):
        detail = Element("data")
        detail.set('name','detail')
        return detail
