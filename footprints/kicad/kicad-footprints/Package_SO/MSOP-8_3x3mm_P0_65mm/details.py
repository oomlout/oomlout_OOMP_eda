###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "MSOP-8_3x3mm_P0.65mm")

newPart.addTag("kicadDesc", "MSOP, 8 Pin (https://www.jedec.org/system/files/docs/mo-187F.pdf variant AA), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "MSOP SO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/MSOP-8_3x3mm_P0.65mm.wrl")

OOMP.parts.append(newPart)