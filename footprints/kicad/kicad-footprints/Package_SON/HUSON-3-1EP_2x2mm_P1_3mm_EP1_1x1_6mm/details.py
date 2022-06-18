###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SON")
newPart.addTag("oompIndex", "HUSON-3-1EP_2x2mm_P1.3mm_EP1.1x1.6mm")

newPart.addTag("kicadDesc", "HUSON, 3 Pin, SOT1061 (Ref: https://assets.nexperia.com/documents/data-sheet/PMEG2020CPA.pdf)")
newPart.addTag("kicadTags", "huson nolead SOT1061")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SON.3dshapes/HUSON-3-1EP_2x2mm_P1.3mm_EP1.1x1.6mm.wrl")

OOMP.parts.append(newPart)