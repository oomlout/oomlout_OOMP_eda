###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Mini-Circuits")
newPart.addTag("oompIndex", "Mini-Circuits_BK377_LandPatternPL-005")
newPart.addTag("oompName", "kicad-footprints/RF_Mini-Circuits/Mini-Circuits_BK377_LandPatternPL-005")

newPart.addTag("kicadDesc", "Footprint for Mini-Circuits case BK377 (https://ww2.minicircuits.com/case_style/BK276.pdf) according to land-pattern PL-005, including GND vias (https://ww2.minicircuits.com/pcb/98-pl005.pdf)")
newPart.addTag("kicadTags", "Mini-circuits VCXO JTOS PL-005")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_BK377.wrl")

OOMP.parts.append(newPart)