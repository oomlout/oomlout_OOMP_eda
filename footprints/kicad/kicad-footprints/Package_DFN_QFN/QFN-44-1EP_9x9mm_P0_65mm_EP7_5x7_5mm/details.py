###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm")

newPart.addTag("kicadDesc", "44-Lead Plastic Quad Flat, No Lead Package - 9x9 mm Body [QFN]; see section 10.3 of https://www.parallax.com/sites/default/files/downloads/P8X32A-Propeller-Datasheet-v1.4.0_0.pdf")
newPart.addTag("kicadTags", "QFN 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-44-1EP_9x9mm_P0.65mm_EP7.5x7.5mm.wrl")

OOMP.parts.append(newPart)