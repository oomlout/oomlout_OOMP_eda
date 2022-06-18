###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-64_9.0x9.0mm_Layout10x10_P0.8mm")

newPart.addTag("kicadDesc", "BGA-64, 10x10 raster, 9x9mm package, pitch 0.8mm")
newPart.addTag("kicadTags", "BGA-64")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-64_9.0x9.0mm_Layout10x10_P0.8mm.wrl")

OOMP.parts.append(newPart)