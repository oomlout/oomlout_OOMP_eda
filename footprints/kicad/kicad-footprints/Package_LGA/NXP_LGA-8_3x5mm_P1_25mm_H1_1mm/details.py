###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "NXP_LGA-8_3x5mm_P1.25mm_H1.1mm")

newPart.addTag("kicadDesc", "NXP  LGA, 8 Pin (https://www.nxp.com/docs/en/data-sheet/MPL3115A2.pdf#page=42), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "NXP LGA NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/NXP_LGA-8_3x5mm_P1.25mm_H1.1mm.wrl")

OOMP.parts.append(newPart)