###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "Zetex_SM8")

newPart.addTag("kicadDesc", "Zetex,  SMD, 8 pin package (http://datasheet.octopart.com/ZDT6758TA-Zetex-datasheet-68057.pdf)")
newPart.addTag("kicadTags", "Zetex SM8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/Zetex_SM8.wrl")

OOMP.parts.append(newPart)