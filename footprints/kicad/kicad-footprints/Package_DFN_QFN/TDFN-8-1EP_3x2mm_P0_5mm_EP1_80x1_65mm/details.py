###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm")

newPart.addTag("kicadDesc", "8-lead plastic dual flat, 2x3x0.75mm size, 0.5mm pitch (http://ww1.microchip.com/downloads/en/DeviceDoc/8L_TDFN_2x3_MN_C04-0129E-MN.pdf)")
newPart.addTag("kicadTags", "TDFN DFN 0.5mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/TDFN-8-1EP_3x2mm_P0.5mm_EP1.80x1.65mm.wrl")

OOMP.parts.append(newPart)