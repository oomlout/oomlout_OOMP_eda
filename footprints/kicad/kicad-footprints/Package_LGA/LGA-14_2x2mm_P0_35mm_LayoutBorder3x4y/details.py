###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y")

newPart.addTag("kicadDesc", "LGA, 14 Pin (http://www.st.com/resource/en/datasheet/lis2dh.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "LGA NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-14_2x2mm_P0.35mm_LayoutBorder3x4y.wrl")

OOMP.parts.append(newPart)