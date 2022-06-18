###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm")

newPart.addTag("kicadDesc", "20-Lead Plastic Quad Flat, No Lead Package - 3x3 mm Body [QFN] with corner pads; see figure 8.2 of https://www.silabs.com/documents/public/data-sheets/efm8bb1-datasheet.pdf")
newPart.addTag("kicadTags", "QFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/SiliconLabs_QFN-20-1EP_3x3mm_P0.5mm_EP1.8x1.8mm.wrl")

OOMP.parts.append(newPart)