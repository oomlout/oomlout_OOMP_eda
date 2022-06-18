###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_LGA")
newPart.addTag("oompIndex", "AMS_LGA-10-1EP_2.7x4mm_P0.6mm")

newPart.addTag("kicadDesc", "LGA-10, http://ams.com/eng/content/download/951091/2269479/471718")
newPart.addTag("kicadTags", "lga land grid array")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_LGA.3dshapes/AMS_LGA-10-1EP_2.7x4mm_P0.6mm.wrl")

OOMP.parts.append(newPart)