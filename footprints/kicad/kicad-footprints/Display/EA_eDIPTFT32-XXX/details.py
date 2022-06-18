###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display")
newPart.addTag("oompIndex", "EA_eDIPTFT32-XXX")

newPart.addTag("kicadDesc", "TFT-graphic display 320x240 16 bit colour with led backlight http://www.lcd-module.com/fileadmin/eng/pdf/grafik/ediptft32-ae.pdf")
newPart.addTag("kicadTags", "TFT-graphic display 320x240 16 bit colour with led backlight")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA_eDIPTFT32-XXX.wrl")

OOMP.parts.append(newPart)