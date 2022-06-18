###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_Kyocera_KC2520Z-4Pin_2.5x2.0mm")

newPart.addTag("kicadDesc", "https://global.kyocera.com/prdct/electro/product/pdf/clock_z_xz_e.pdf")
newPart.addTag("kicadTags", "2.5mm 2mm SMD")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_Kyocera_KC2520Z-4Pin_2.5x2.0mm.wrl")

OOMP.parts.append(newPart)