###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_R-PWQFN-N28_EP2.1x3.1mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 28 Pin (http://www.ti.com/lit/ds/symlink/tps51363.pdf#page=29), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_R-PWQFN-N28_EP2.1x3.1mm.wrl")

OOMP.parts.append(newPart)