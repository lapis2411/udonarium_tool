from xml.etree.ElementTree import Element, SubElement, ElementTree

class TableElement:
    def make_table_element(self) :
        table = Element("game-table")
        table.set('name','initial table')
        table.set('width','20')
        table.set('height','15')
        table.set('gridSize','50')
        table.set('imageIdentifier','testTableBackgroundImage_image')
        table.set('backgroundImageIdentifier','imageIdentifier')
        table.set('backgroundFilterType','')
        table.set('selected','false')
        table.set('gridType','0')
        table.set('gridColor','#000000e6')
        return table