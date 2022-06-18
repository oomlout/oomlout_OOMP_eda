###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_Cree-XHP35")

newPart.addTag("kicadDesc", "http://www.cree.com/~/media/Files/Cree/LED-Components-and-Modules/XLamp/Data-and-Binning/ds--XHP35.pdf")
newPart.addTag("kicadTags", "LED Cree XHP35")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-XHP35.wrl")

OOMP.parts.append(newPart)