###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "TerminalBlock_Phoenix")
newPart.addTag("oompIndex", "TerminalBlock_Phoenix_PT-1,5-3-5.0-H_1x03_P5.00mm_Horizontal")

newPart.addTag("kicadDesc", "Terminal Block Phoenix PT-1,5-3-5.0-H, 3 pins, pitch 5mm, size 15x9mm^2, drill diamater 1.3mm, pad diameter 2.6mm, see http://www.mouser.com/ds/2/324/ItemDetail_1935161-922578.pdf, script-generated using https://github.com/pointhi/kicad-footprint-generator/scripts/TerminalBlock_Phoenix")
newPart.addTag("kicadTags", "THT Terminal Block Phoenix PT-1,5-3-5.0-H pitch 5mm size 15x9mm^2 drill 1.3mm pad 2.6mm")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/TerminalBlock_Phoenix.3dshapes/TerminalBlock_Phoenix_PT-1,5-3-5.0-H_1x03_P5.00mm_Horizontal.wrl")

OOMP.parts.append(newPart)