###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Transformer_SMD")
newPart.addTag("oompIndex", "Pulse_PA2002NL-PA2008NL-PA2009NL")

newPart.addTag("kicadDesc", "SMT Gate Drive Transformer, 1:1:1 or 2:1:1 or 2.5:1:1 or 1:1, 9.0x8.6x7.6mm (https://productfinder.pulseeng.com/products/datasheets/P663.pdf)")
newPart.addTag("kicadTags", "pulse pa2002nl pa2008nl pa2009nl p0544nl pa0184nl pa0297nl pa0510nl")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Transformer_SMD.3dshapes/Pulse_PA2002NL-PA2008NL-PA2009NL.wrl")

OOMP.parts.append(newPart)