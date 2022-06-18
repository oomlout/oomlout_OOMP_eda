###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TSSOP-64_8x14mm_P0.4mm")

newPart.addTag("kicadDesc", "TSSOP, 64 Pin (JEDEC MO-153 Var JD https://www.jedec.org/document_search?search_api_views_fulltext=MO-153), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "TSSOP SO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-64_8x14mm_P0.4mm.wrl")

OOMP.parts.append(newPart)