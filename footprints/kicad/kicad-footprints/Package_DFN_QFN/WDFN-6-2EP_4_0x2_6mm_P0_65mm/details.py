###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "WDFN-6-2EP_4.0x2.6mm_P0.65mm")
newPart.addTag("oompName", "kicad-footprints/Package_DFN_QFN/WDFN-6-2EP_4.0x2.6mm_P0.65mm")

newPart.addTag("kicadDesc", "WDFN, 6 pin, 4.0x2.6, 0.65P; Two exposed pads, (https://www.onsemi.com/pub/Collateral/511BZ.PDF)")
newPart.addTag("kicadTags", "DFN 0.65P dual flag")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/WDFN-6-2EP_4.0x2.6mm_P0.65mm.wrl")

OOMP.parts.append(newPart)