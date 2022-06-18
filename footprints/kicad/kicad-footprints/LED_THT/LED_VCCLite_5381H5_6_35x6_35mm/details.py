###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "LED_THT")
newPart.addTag("oompIndex", "LED_VCCLite_5381H5_6.35x6.35mm")

newPart.addTag("kicadDesc", "Green 5381 Series LED VCCLite https://vcclite.com/wp-content/uploads/wpallimport/files/files/5381Series.pdf http://static.vcclite.com/pdf/Mounting%20Hole%20Pattern%202.pdf")
newPart.addTag("kicadTags", "Green 5381 Series LED")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/LED_THT.3dshapes/LED_VCCLite_5381H5_6.35x6.35mm.wrl")

OOMP.parts.append(newPart)