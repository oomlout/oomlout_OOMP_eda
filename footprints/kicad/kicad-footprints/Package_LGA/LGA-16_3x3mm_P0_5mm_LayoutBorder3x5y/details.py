###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y")

newPart.addTag("kicadDesc", "LGA, 16 Pin (http://www.st.com/resource/en/datasheet/lis331hh.pdf), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "LGA NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/LGA-16_3x3mm_P0.5mm_LayoutBorder3x5y.wrl")

OOMP.parts.append(newPart)