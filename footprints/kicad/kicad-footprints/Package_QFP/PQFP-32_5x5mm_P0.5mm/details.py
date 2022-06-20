###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "PQFP-32_5x5mm_P0.5mm")
newPart.addTag("oompName", "kicad-footprints/Package_QFP/PQFP-32_5x5mm_P0.5mm")

newPart.addTag("kicadDesc", "PQFP, 32 Pin (https://www.ti.com/lit/ds/symlink/ads127l01.pdf#page=87), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "PQFP QFP")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/PQFP-32_5x5mm_P0.5mm.wrl")

OOMP.parts.append(newPart)