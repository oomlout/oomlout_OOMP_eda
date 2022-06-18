###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TSOP-I-28_11.8x8mm_P0.55mm")

newPart.addTag("kicadDesc", "TSOP I, 28 pins, 18.8x8mm body, 0.55mm pitch, IPC-calculated pads (http://ww1.microchip.com/downloads/en/devicedoc/doc0807.pdf)")
newPart.addTag("kicadTags", "TSOP I 28 pins")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TSOP-I-28_11.8x8mm_P0.55mm.wrl")

OOMP.parts.append(newPart)