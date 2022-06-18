###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_S-PWQFN-N100_EP5.5x5.5mm")

newPart.addTag("kicadDesc", "http://www.ti.com/general/docs/lit/getliterature.tsp?baseLiteratureNumber=szza059&fileType=pdf,http://www.ti.com/lit/ds/sllse76m/sllse76m.pdf")
newPart.addTag("kicadTags", "MultiRow QFN")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_S-PWQFN-N100_EP5.5x5.5mm.wrl")

OOMP.parts.append(newPart)