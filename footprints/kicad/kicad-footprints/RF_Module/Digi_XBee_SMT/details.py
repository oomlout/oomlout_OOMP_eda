###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_Module")
newPart.addTag("oompIndex", "Digi_XBee_SMT")

newPart.addTag("kicadDesc", "http://www.digi.com/resources/documentation/digidocs/pdfs/90002126.pdf http://ftp1.digi.com/support/documentation/90001020_F.pdf")
newPart.addTag("kicadTags", "Digi XBee SMT RF")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_Module.3dshapes/Digi_XBee_SMT.wrl")

OOMP.parts.append(newPart)