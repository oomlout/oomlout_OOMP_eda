###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "WSON-8-1EP_3x3mm_P0.5mm_EP1.45x2.4mm_ThermalVias")

newPart.addTag("kicadDesc", "WSON, 8 Pin (https://www.ti.com/lit/ds/symlink/ina333.pdf#page=30), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "WSON NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/WSON-8-1EP_3x3mm_P0.5mm_EP1.45x2.4mm.wrl")

OOMP.parts.append(newPart)