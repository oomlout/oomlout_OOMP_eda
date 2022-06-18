###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Mini-Circuits")
newPart.addTag("oompIndex", "Mini-Circuits_MMM168_LandPatternPL-225")

newPart.addTag("kicadDesc", "Footprint for Mini-Circuits case MMM168, Land pattern PL-225, vias included, (case drawing: https://ww2.minicircuits.com/case_style/MMM168.pdf, land pattern drawing: https://ww2.minicircuits.com/pcb/98-pl225.pdf)")
newPart.addTag("kicadTags", "pl-225")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_MMM168.wrl")

OOMP.parts.append(newPart)