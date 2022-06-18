###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TSOP-I-32_18.4x8mm_P0.5mm_Reverse")

newPart.addTag("kicadDesc", "TSOP I, 32 pins, 18.4x8mm body (http://www.futurlec.com/Datasheet/Memory/628128.pdf), reverse mount")
newPart.addTag("kicadTags", "TSOP I 32 reverse")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSOP-I-32_18.4x8mm_P0.5mm_Reverse.wrl")

OOMP.parts.append(newPart)