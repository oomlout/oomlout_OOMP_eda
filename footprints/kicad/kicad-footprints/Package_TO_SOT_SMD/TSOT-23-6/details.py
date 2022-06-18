###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "TSOT-23-6")

newPart.addTag("kicadDesc", "TSOT, 6 Pin (https://www.jedec.org/sites/default/files/docs/MO-193D.pdf variant AA), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "TSOT TO_SOT_SMD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/TSOT-23-6.wrl")

OOMP.parts.append(newPart)