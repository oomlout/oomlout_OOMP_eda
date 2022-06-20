###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm_ThermalVia")
newPart.addTag("oompName", "kicad-footprints/Package_DFN_QFN/Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm_ThermalVia")

newPart.addTag("kicadDesc", "Texas instruments QFN Package, datasheet: https://www.ti.com/lit/ds/symlink/tpsm53602.pdf")
newPart.addTag("kicadTags", "Texas instruments QFN")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Texas_B3QFN-14-1EP_5x5.5mm_P0.65mm.wrl")

OOMP.parts.append(newPart)