###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "Texas_S-PDSO-N12")

newPart.addTag("kicadDesc", "http://www.ti.com/lit/ds/symlink/bq27441-g1.pdf")
newPart.addTag("kicadTags", "SON thermal pads")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/Texas_S-PDSO-N12.wrl")

OOMP.parts.append(newPart)