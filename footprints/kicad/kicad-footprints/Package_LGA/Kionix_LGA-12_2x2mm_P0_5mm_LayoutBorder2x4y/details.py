###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "Kionix_LGA-12_2x2mm_P0.5mm_LayoutBorder2x4y")

newPart.addTag("kicadDesc", "Kionix  LGA, 12 Pin (http://kionixfs.kionix.com/en/document/TN008-PCB-Design-Guidelines-for-2x2-LGA-Sensors.pdf#page=4), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "Kionix LGA NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/Kionix_LGA-12_2x2mm_P0.5mm_LayoutBorder2x4y.wrl")

OOMP.parts.append(newPart)