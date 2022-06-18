###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "UCBGA-81_4x4mm_Layout9x9_P0.4mm")

newPart.addTag("kicadDesc", "UCBGA-81, 9x9 raster, 4x4mm package, pitch 0.4mm; https://www.latticesemi.com/view_document?document_id=213")
newPart.addTag("kicadTags", "BGA 81 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UCBGA-81_4x4mm_Layout9x9_P0.4mm.wrl")

OOMP.parts.append(newPart)