###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_USB")
newPart.addTag("oompIndex", "USB_A_Molex_67643_Horizontal")

newPart.addTag("kicadDesc", "USB type A, Horizontal, https://www.molex.com/pdm_docs/sd/676433910_sd.pdf")
newPart.addTag("kicadTags", "USB_A Female Connector receptacle")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_A_Molex_67643_Horizontal.wrl")

OOMP.parts.append(newPart)