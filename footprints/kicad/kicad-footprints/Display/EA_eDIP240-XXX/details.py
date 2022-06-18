###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Display")
newPart.addTag("oompIndex", "EA_eDIP240-XXX")

newPart.addTag("kicadDesc", "LCD graphical display LED backlight 240x128 http://www.lcd-module.com/fileadmin/eng/pdf/grafik/edip240-7e.pdf")
newPart.addTag("kicadTags", "LCD graphical display LED backlight 240x128")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Display.3dshapes/EA_eDIP240-XXX.wrl")

OOMP.parts.append(newPart)