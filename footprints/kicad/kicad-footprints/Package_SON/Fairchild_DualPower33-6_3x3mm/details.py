###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "Fairchild_DualPower33-6_3x3mm")

newPart.addTag("kicadDesc", "Fairchild Power33 MOSFET package, 3x3mm (see https://www.fairchildsemi.com/datasheets/FD/FDMC8032L.pdf)")
newPart.addTag("kicadTags", "mosfet")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Fairchild_DualPower33-6_3x3mm.wrl")

OOMP.parts.append(newPart)