###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Mini-Circuits")
newPart.addTag("oompIndex", "Mini-Circuits_HF1139_LandPatternPL-230")

newPart.addTag("kicadDesc", "Footprint for Mini-Circuits case HF1139 (https://ww2.minicircuits.com/case_style/HF1139.pdf) following land pattern PL-230, including GND vias (https://ww2.minicircuits.com/pcb/98-pl230.pdf)")
newPart.addTag("kicadTags", "Mini-Circuits PL-230")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Mini-Circuits.3dshapes/Mini-Circuits_HF1139.wrl")

OOMP.parts.append(newPart)