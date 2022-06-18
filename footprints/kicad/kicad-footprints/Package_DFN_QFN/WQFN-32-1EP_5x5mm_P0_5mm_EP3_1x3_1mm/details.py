###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm")
newPart.addTag("oompName", "kicad-footprints/Package_DFN_QFN/WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm")

newPart.addTag("kicadDesc", "QFN, 32-Leads, Body 5x5x0.8mm, Pitch 0.5mm, Thermal Pad 3.1x3.1mm; (see Texas Instruments LM25119 http://www.ti.com/lit/ds/symlink/lm25119.pdf)")
newPart.addTag("kicadTags", "WQFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WQFN-32-1EP_5x5mm_P0.5mm_EP3.1x3.1mm.wrl")

OOMP.parts.append(newPart)