###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transformer_SMD")
newPart.addTag("oompIndex", "Pulse_PA2006NL")

newPart.addTag("kicadDesc", "SMT Gate Drive Transformer, 1:1, 11.8x8.8x4.0mm (https://productfinder.pulseeng.com/products/datasheets/P663.pdf)")
newPart.addTag("kicadTags", "pulse pa2006nl pa0186nl")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Pulse_PA2006NL.wrl")

OOMP.parts.append(newPart)