###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm")

newPart.addTag("kicadDesc", "HTSSOP28: plastic thin shrink small outline package; 28 leads; body width 4.4 mm; thermal pad")
newPart.addTag("kicadTags", "TSSOP HTSSOP 0.65 thermal pad")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm.wrl")

OOMP.parts.append(newPart)