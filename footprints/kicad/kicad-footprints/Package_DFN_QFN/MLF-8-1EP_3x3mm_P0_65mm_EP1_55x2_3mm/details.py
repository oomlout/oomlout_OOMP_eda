###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm")

newPart.addTag("kicadDesc", "8-Pin ePad 3mm x 3mm MLF - 3x3x0.85 mm Body (see Microchip datasheet http://ww1.microchip.com/downloads/en/DeviceDoc/mic5355_6.pdf)")
newPart.addTag("kicadTags", "DFN MLF 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/MLF-8-1EP_3x3mm_P0.65mm_EP1.55x2.3mm.wrl")

OOMP.parts.append(newPart)