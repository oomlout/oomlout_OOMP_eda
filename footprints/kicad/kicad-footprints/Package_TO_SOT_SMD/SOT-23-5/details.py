###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_SMD")
newPart.addTag("oompIndex", "SOT-23-5")

newPart.addTag("kicadDesc", "SOT, 5 Pin (https://www.jedec.org/sites/default/files/docs/Mo-178c.PDF variant AA), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "SOT TO_SOT_SMD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_SMD.3dshapes/SOT-23-5.wrl")

OOMP.parts.append(newPart)