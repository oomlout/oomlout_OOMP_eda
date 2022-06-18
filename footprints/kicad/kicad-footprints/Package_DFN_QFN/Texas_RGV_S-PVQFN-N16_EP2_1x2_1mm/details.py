###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_RGV_S-PVQFN-N16_EP2.1x2.1mm")

newPart.addTag("kicadDesc", "QFN, 16 Pin (http://www.ti.com/lit/ds/symlink/ina3221.pdf#page=44), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_RGV_S-PVQFN-N16_EP2.1x2.1mm.wrl")

OOMP.parts.append(newPart)