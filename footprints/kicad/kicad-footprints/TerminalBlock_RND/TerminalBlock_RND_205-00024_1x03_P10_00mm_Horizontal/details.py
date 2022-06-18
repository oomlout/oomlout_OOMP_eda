###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TerminalBlock_RND")
newPart.addTag("oompIndex", "TerminalBlock_RND_205-00024_1x03_P10.00mm_Horizontal")

newPart.addTag("kicadDesc", "terminal block RND 205-00024, 3 pins, pitch 10mm, size 25x9mm^2, drill diamater 1.3mm, pad diameter 2.5mm, see http://cdn-reichelt.de/documents/datenblatt/C151/RND_205-00023_DB_EN.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_RND")
newPart.addTag("kicadTags", "THT terminal block RND 205-00024 pitch 10mm size 25x9mm^2 drill 1.3mm pad 2.5mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TerminalBlock_RND.3dshapes/TerminalBlock_RND_205-00024_1x03_P10.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)