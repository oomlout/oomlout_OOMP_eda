###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SO-4_4.4x3.6mm_P2.54mm")

newPart.addTag("kicadDesc", "4-Lead Plastic Small Outline (SO), see https://www.elpro.org/de/index.php?controller=attachment&id_attachment=339")
newPart.addTag("kicadTags", "SO SOIC 2.54")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SO-4_4.4x3.6mm_P2.54mm.wrl")

OOMP.parts.append(newPart)