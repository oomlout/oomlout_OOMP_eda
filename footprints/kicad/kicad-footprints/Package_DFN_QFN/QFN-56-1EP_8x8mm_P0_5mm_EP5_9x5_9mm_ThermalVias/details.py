###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "QFN-56-1EP_8x8mm_P0.5mm_EP5.9x5.9mm_ThermalVias")

newPart.addTag("kicadDesc", "QFN, 56 Pin (http://ww1.microchip.com/downloads/en/DeviceDoc/00001734B.pdf#page=50), generated with kicad-footprint-generator ipc_noLead_generator.py")
newPart.addTag("kicadTags", "QFN NoLead")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/QFN-56-1EP_8x8mm_P0.5mm_EP5.9x5.9mm.wrl")

OOMP.parts.append(newPart)