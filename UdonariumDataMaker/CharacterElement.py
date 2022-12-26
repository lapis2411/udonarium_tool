from xml.etree.ElementTree import Element, SubElement, ElementTree

class CharacterElement:
    def __init__ (self, player_name, image_path,x,y):
        self.player_name       = player_name
        self.image_path        = image_path
        self.x                 = x
        self.y                 = y


    # def __init__ (self):
    #     self.player_name    = 'player'
    #     self.image_path     = 'testCharacter_1_image'

    def make_character_snippet (self):
        e_character_root = Element("character")
        e_character_root.set('location.name','table')
        e_character_root.set('location.x',self.x)
        e_character_root.set('location.y',self.y)
        e_character_root.set('posZ','0')
        e_character_root.set('rotate','0')
        e_character_root.set('roll','0')
        e_character_root.append(self._make_character_element())
        e_character_root.append(self._make_chat_palette())
        return e_character_root


    def _make_character_element (self):
        e_character = Element("data")
        e_character.set('name','character')

        e_image = SubElement(e_character, "data")
        e_image.set('name','image')
        e_image_path = SubElement(e_image,'data')
        e_image_path.set('type','image')
        e_image_path.set('name','imageIdentifier')
        e_image_path.text = self.image_path

        e_common = SubElement(e_character, "data")
        e_common.set('name','common')
        e_player_name = SubElement(e_common, "data")
        e_player_name.set('name','name')
        e_player_name.text = self.player_name
        e_size = SubElement(e_common, "data")
        e_size.set('name','size')
        e_size.text = '1'

        e_detail = SubElement(e_character, "data")
        e_detail.set('name','detail')
        e_resource = SubElement(e_detail, "data")
        e_resource.set('name','resource')
        e_wealth = SubElement(e_resource, "data")
        e_wealth.set('type','numberResource')
        e_wealth.set('currentValue','0')
        e_wealth.set('name','wealth')
        e_wealth.text = '16'

        e_authority = SubElement(e_resource, "data")
        e_authority.set('type','numberResource')
        e_authority.set('currentValue','0')
        e_authority.set('name','authority')
        e_authority.text = '16'
        
        e_information = SubElement(e_detail, "data")
        e_information.set('name','information')
        e_explanation = SubElement(e_information, "data")
        e_explanation.set('type','note')
        e_explanation.set('name','explanation')
        
        e_memo = SubElement(e_information, "data")
        e_memo.set('type','note')
        e_memo.set('name','memo')

        return e_character

    def _make_chat_palette (self):
        e_chat_palette = Element("chat-palette")
        e_chat_palette.set('dicebot','')
        return e_chat_palette


