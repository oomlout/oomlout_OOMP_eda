###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Heatsink")
newPart.addTag("oompIndex", "Heatsink_Fischer_FK224xx2201_25x8.3mm")

newPart.addTag("kicadDesc", "25x8.3mm Heatsink, 18K/W, TO-220, https://www.fischerelektronik.de/web_fischer/en_GB/$catalogue/fischerData/PR/FK224_220_1_/datasheet.xhtml?branch=heatsinks")
newPart.addTag("kicadTags", "heatsink TO-220")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Heatsink.3dshapes/Heatsink_Fischer_FK2242201_25x8.3mm.wrl")

OOMP.parts.append(newPart)