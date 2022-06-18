###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_Cree-XH")

newPart.addTag("kicadDesc", "http://www.cree.com/~/media/Files/Cree/LED-Components-and-Modules/XLamp/Data-and-Binning/ds-XHB.pdf")
newPart.addTag("kicadTags", "LED Cree XH")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-XH.wrl")

OOMP.parts.append(newPart)