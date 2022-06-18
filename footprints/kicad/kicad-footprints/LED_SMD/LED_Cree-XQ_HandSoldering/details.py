###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_SMD")
newPart.addTag("oompIndex", "LED_Cree-XQ_HandSoldering")

newPart.addTag("kicadDesc", "LED Cree-XQ handsoldering pads http://www.cree.com/~/media/Files/Cree/LED-Components-and-Modules/XLamp/Data-and-Binning/ds-XQB.pdf")
newPart.addTag("kicadTags", "LED Cree XQ")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_SMD.3dshapes/LED_Cree-XQ.wrl")

OOMP.parts.append(newPart)