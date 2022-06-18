###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SSOP-14_5.3x6.2mm_P0.65mm")

newPart.addTag("kicadDesc", "SSOP14: plastic shrink small outline package; 14 leads; body width 5.3 mm; (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot337-1_po.pdf)")
newPart.addTag("kicadTags", "SSOP 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-14_5.3x6.2mm_P0.65mm.wrl")

OOMP.parts.append(newPart)