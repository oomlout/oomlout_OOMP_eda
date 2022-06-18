###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "BGA-121_9.0x9.0mm_Layout11x11_P0.8mm_Ball0.4mm_Pad0.35mm_NSMD")

newPart.addTag("kicadDesc", "121-ball, 0.8mm BGA (based on http://www.latticesemi.com/view_document?document_id=213)")
newPart.addTag("kicadTags", "BGA 0.8mm 9mm 121")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/BGA-121_9.0x9.0mm_Layout11x11_P0.8mm.wrl")

OOMP.parts.append(newPart)