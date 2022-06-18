###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "Heraeus_TO-92-2")

newPart.addTag("kicadDesc", "TO-92 2-pin variant by Heraeus, drill 0.75mm (http://www.produktinfo.conrad.com/datenblaetter/175000-199999/181293-da-01-de-TO92_Temperatursensor_PT1000_32209225.pdf)")
newPart.addTag("kicadTags", "to-92")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/Heraeus_TO-92-2.wrl")

OOMP.parts.append(newPart)