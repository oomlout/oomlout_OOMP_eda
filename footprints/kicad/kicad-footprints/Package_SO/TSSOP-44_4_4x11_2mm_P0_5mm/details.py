###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TSSOP-44_4.4x11.2mm_P0.5mm")

newPart.addTag("kicadDesc", "TSSOP44: plastic thin shrink small outline package; 44 leads; body width 4.4 mm (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot510-1_po.pdf)")
newPart.addTag("kicadTags", "SSOP 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSSOP-44_4.4x11.2mm_P0.5mm.wrl")

OOMP.parts.append(newPart)