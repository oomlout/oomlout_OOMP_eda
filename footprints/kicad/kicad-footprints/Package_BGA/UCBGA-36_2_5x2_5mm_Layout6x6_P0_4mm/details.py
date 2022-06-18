###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "UCBGA-36_2.5x2.5mm_Layout6x6_P0.4mm")

newPart.addTag("kicadDesc", "UCBGA-36, 6x6 raster, 2.5x2.5mm package, pitch 0.4mm; https://www.latticesemi.com/view_document?document_id=213")
newPart.addTag("kicadTags", "BGA 36 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UCBGA-36_2.5x2.5mm_Layout6x6_P0.4mm.wrl")

OOMP.parts.append(newPart)