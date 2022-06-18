###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "VSSOP-10_3x3mm_P0.5mm")

newPart.addTag("kicadDesc", "VSSOP, 10 Pin (http://www.ti.com/lit/ds/symlink/ads1115.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "VSSOP SO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/VSSOP-10_3x3mm_P0.5mm.wrl")

OOMP.parts.append(newPart)