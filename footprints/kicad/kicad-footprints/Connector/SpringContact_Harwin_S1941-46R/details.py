###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector")
newPart.addTag("oompIndex", "SpringContact_Harwin_S1941-46R")

newPart.addTag("kicadDesc", "7.25mm SMT Multi-directional Spring Contact (T+R), https://cdn.harwin.com/pdfs/S1941R.pdf")
newPart.addTag("kicadTags", "spring contact emi emc shield")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector.3dshapes/SpringContact_Harwin_S1941-46R.wrl")

OOMP.parts.append(newPart)