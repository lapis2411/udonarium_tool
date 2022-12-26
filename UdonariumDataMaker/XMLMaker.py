from xml.etree.ElementTree import Element, SubElement, ElementTree
import xml.etree.ElementTree as ET
from xml.dom import minidom
import TableElement as TE
import CharacterElement as CE
import DiceElement as DE
import CardElement as CaE
import ImageConverter as ImgCon

data_output = r"C:\Reposytory\python\easy_udonarium_env\Output\Udonarium\data.xml"
data_output_root = r"C:\Reposytory\python\easy_udonarium_env\Output\Udonarium"
image_root = r"C:\Reposytory\python\easy_udonarium_env\Input\images"


root = Element("room")
te = TE.TableElement()
root.append(te.make_table_element())

ce = CE.CharacterElement('player1','testCharacter_1_image','0','375')
root.append(ce.make_character_snippet())
ce = CE.CharacterElement('player2','testCharacter_5_image','375','0')
root.append(ce.make_character_snippet())
ce = CE.CharacterElement('player3','testCharacter_4_image','925','375')
root.append(ce.make_character_snippet())
ce = CE.CharacterElement('player4','testCharacter_6_image','375','700')
root.append(ce.make_character_snippet())

de = DE.DiceElement()
root.append(de.make_table_element('300','375'))
root.append(de.make_table_element('400','375'))

def1 = ImgCon.convert(r"C:\Reposytory\python\easy_udonarium_env\Input\images\default_1.png", data_output_root)
def2 = ImgCon.convert(r"C:\Reposytory\python\easy_udonarium_env\Input\images\default_2.png", data_output_root)
cae = CaE.CardElement('default1', '400','600')
root.append(cae.make_card_stack([def1, def2], image_root ))

rough_string = ET.tostring(root, 'utf-8', short_empty_elements=False)
reparsed = minidom.parseString(rough_string)

with open(data_output, "w") as f:
    f.write(reparsed.toprettyxml(indent="  ", encoding='UTF-8').decode('utf-8'))