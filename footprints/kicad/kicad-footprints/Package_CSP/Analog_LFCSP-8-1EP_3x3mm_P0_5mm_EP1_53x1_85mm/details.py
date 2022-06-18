###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "Analog_LFCSP-8-1EP_3x3mm_P0.5mm_EP1.53x1.85mm")

newPart.addTag("kicadDesc", "LFCSP, exposed pad, Analog Devices (http://www.analog.com/media/en/technical-documentation/data-sheets/ADL5542.pdf)")
newPart.addTag("kicadTags", "LFCSP 8 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/LFCSP-8-1EP_3x3mm_P0.5mm_EP1.53x1.85mm.wrl")

OOMP.parts.append(newPart)