###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_S-PWQFN-N32_EP2.8x2.8mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 32 Pin (https://www.ti.com/lit/ds/symlink/bq25703a.pdf#page=90), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PWQFN-N32_EP2.8x2.8mm.wrl")

OOMP.parts.append(newPart)