###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-16-1EP_4x5mm_P0.5mm_EP2.44x4.34mm")

newPart.addTag("kicadDesc", "DHD Package; 16-Lead Plastic DFN (5mm x 4mm) (see Linear Technology 05081707_A_DHD16.pdf)")
newPart.addTag("kicadTags", "DFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-16-1EP_4x5mm_P0.5mm_EP2.44x4.34mm.wrl")

OOMP.parts.append(newPart)