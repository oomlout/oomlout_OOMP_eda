###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "DFN-14-1EP_3x4.5mm_P0.65mm_EP1.65x4.25mm")

newPart.addTag("kicadDesc", "14-lead very thin plastic quad flat, 3.0x4.5mm size, 0.65mm pitch (http://ww1.microchip.com/downloads/en/DeviceDoc/14L_VDFN_4_5x3_0mm_JHA_C041198A.pdf)")
newPart.addTag("kicadTags", "VDFN DFN 0.65mm")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/DFN-14-1EP_3x4.5mm_P0.65mm.wrl")

OOMP.parts.append(newPart)