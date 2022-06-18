###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_DIP-8")

newPart.addTag("kicadDesc", "Oscillator, DIP8,http://cdn-reichelt.de/documents/datenblatt/B400/OSZI.pdf")
newPart.addTag("kicadTags", "oscillator")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_DIP-8.wrl")

OOMP.parts.append(newPart)