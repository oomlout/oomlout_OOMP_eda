###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "VSO-56_11.1x21.5mm_P0.75mm")

newPart.addTag("kicadDesc", "VSO56: plastic very small outline package; 56 leads (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot190-1_po.pdf)")
newPart.addTag("kicadTags", "SSOP 0.75")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/VSO-56_11.1x21.5mm_P0.75mm.wrl")

OOMP.parts.append(newPart)