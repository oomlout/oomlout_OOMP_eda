###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transformer_SMD")
newPart.addTag("oompIndex", "Pulse_PA2004NL")

newPart.addTag("kicadDesc", "SMT Gate Drive Transformer, 1:1:1, 8.6x6.7x3.6mm (https://productfinder.pulseeng.com/products/datasheets/P663.pdf)")
newPart.addTag("kicadTags", "pulse pa2004nl pa0264nl")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Pulse_PA2004NL.wrl")

OOMP.parts.append(newPart)