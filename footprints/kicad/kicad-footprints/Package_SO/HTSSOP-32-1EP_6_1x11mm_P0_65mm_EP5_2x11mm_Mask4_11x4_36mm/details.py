###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm_Mask4.11x4.36mm")

newPart.addTag("kicadDesc", "HTSSOP32: plastic thin shrink small outline package; 32 leads; body width 6.1 mm; lead pitch 0.65 mm (see NXP SSOP-TSSOP-VSO-REFLOW.pdf and sot487-1_po.pdf)")
newPart.addTag("kicadTags", "SSOP 0.65 PowerPAD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HTSSOP-32-1EP_6.1x11mm_P0.65mm_EP5.2x11mm.wrl")

OOMP.parts.append(newPart)