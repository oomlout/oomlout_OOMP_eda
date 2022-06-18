###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TSSOP-4_4.4x5mm_P4mm")

newPart.addTag("kicadDesc", "TSSOP, 4 Pin (https://www.onsemi.com/pub/Collateral/MDB8S-D.PDF#page=4), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "TSSOP SO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-4_4.4x5mm_P4mm.wrl")

OOMP.parts.append(newPart)