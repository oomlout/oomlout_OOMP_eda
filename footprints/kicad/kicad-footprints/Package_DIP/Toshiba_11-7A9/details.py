###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "Toshiba_11-7A9")

newPart.addTag("kicadDesc", "Toshiba 11-7A9 package, like 6-lead dip package with missing pin 5, row spacing 7.62 mm (300 mils), https://toshiba.semicon-storage.com/info/docget.jsp?did=1421&prodName=TLP3021(S)")
newPart.addTag("kicadTags", "Toshiba 11-7A9 DIL DIP PDIP 2.54mm 7.62mm 300mil")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/Toshiba_11-7A9.wrl")

OOMP.parts.append(newPart)