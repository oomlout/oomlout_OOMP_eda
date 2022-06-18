###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "PowerPAK_SO-8_Dual")

newPart.addTag("kicadDesc", "PowerPAK SO-8 Dual (https://www.vishay.com/docs/71655/powerpak.pdf, https://www.vishay.com/docs/72600/72600.pdf)")
newPart.addTag("kicadTags", "PowerPAK SO-8 Dual")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/PowerPAK_SO-8_Dual.wrl")

OOMP.parts.append(newPart)