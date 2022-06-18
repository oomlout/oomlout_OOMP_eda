###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_SMD_SeikoEpson_SG210-4Pin_2.5x2.0mm")

newPart.addTag("kicadDesc", "SMD Crystal Oscillator Seiko Epson SG-210 https://support.epson.biz/td/api/doc_check.php?mode=dl&lang=en&Parts=SG-210SED, 2.5x2.0mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal oscillator")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_SMD_SeikoEpson_SG210-4Pin_2.5x2.0mm.wrl")

OOMP.parts.append(newPart)