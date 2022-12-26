from xml.etree.ElementTree import Element, SubElement, ElementTree
import hashlib

class CardElement:
    def __init__ (self, stack_name,x,y):
        self.stack_name        = stack_name
        self.x           = x
        self.y           = y

    def make_card_stack(self, front_name_list, back_name):
        stack_root = self._make_root()
        stack_root.append(self._make_card_stack_info())
        node = Element("node")
        node.set('name','cardRoot')
        for fp in front_name_list:
            node.append(self._make_single_card_info(fp, back_name))
        stack_root.append(node)
        return stack_root


    def _make_root (self):
        card_stack_root = Element("card-stack")
        card_stack_root.set('location.name','table')
        card_stack_root.set('location.x',self.x)
        card_stack_root.set('location.y',self.y)
        card_stack_root.set('posZ','0')
        card_stack_root.set('rotate','0')
        card_stack_root.set('zindex','10')
        card_stack_root.set('owner','')
        card_stack_root.set('isShowTotal','true')
        return card_stack_root

    def _make_card_stack_info (self):
        card_stack_info = Element("data")
        card_stack_info.set('name','card-stack')
        image = SubElement(card_stack_info, "data")
        image.set('name','image')
        image_idtf = SubElement(image, "data")
        image_idtf.set('type','image')
        image_idtf.set('name','imageIdentifier')
        common = SubElement(card_stack_info, "data")
        common.set('name','common')
        name_info = SubElement(common, "data")
        name_info.set('name','name')
        name_info.text = self.stack_name
        detail = SubElement(card_stack_info, "data")
        detail.set('name','detail')
        return card_stack_info
    
    def _make_single_card_info(self, front_path, back_path) :
        single_card_root = Element("card")
        single_card_root.set('location.name','table')
        single_card_root.set('location.x',str(int(self.x)+110))
        single_card_root.set('location.y',str(int(self.y)-20))
        single_card_root.set('posZ','0')
        single_card_root.set('rotate','0')
        single_card_root.set('zindex','10')
        single_card_root.set('owner','')
        single_card_root.set('isShowTotal','true')

        card = SubElement(single_card_root, "data")
        card.set('name','card')
        
        image = SubElement(card, "data")
        image.set('name','image')
        image_idtf = SubElement(image, "data")
        image_idtf.set('type','image')
        # image_idtf.set('name','imageIdentifier')
        image_frnt = SubElement(image, "data")
        image_frnt.set('type','image')
        image_frnt.set('name','front')
        image_frnt.text = front_path
        image_back = SubElement(image, "data")
        image_back.set('type','image')
        image_back.set('name','back')
        image_back.text = back_path

        common = SubElement(card, "data")
        common.set('name','common')
        name_info = SubElement(common, "data")
        name_info.set('name','name')
        name_info.text = 'card'
        size_info = SubElement(common, "data")
        size_info.set('name','size')
        size_info.text = '2'
        detail = SubElement(card, "data")
        detail.set('name','detail')
        return single_card_root

