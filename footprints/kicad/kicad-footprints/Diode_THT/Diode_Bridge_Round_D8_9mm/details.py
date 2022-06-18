###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Diode_THT")
newPart.addTag("oompIndex", "Diode_Bridge_Round_D8.9mm")

newPart.addTag("kicadDesc", "4-lead round diode bridge package, diameter 8.9mm, pin pitch 5.08mm, see http://cdn-reichelt.de/documents/datenblatt/A400/W005M-W10M_SEP.PDF")
newPart.addTag("kicadTags", "diode bridge 8.9mm 8.85mm WOB pitch 5.08mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_Round_D8.9mm.wrl")

OOMP.parts.append(newPart)