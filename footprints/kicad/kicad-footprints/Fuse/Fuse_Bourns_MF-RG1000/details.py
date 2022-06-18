###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fuse")
newPart.addTag("oompIndex", "Fuse_Bourns_MF-RG1000")

newPart.addTag("kicadDesc", "PTC Resettable Fuse, Ihold = 10.0A, Itrip=17.0A, http://www.bourns.com/docs/Product-Datasheets/mfrg.pdf")
newPart.addTag("kicadTags", "ptc resettable fuse polyfuse THT")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_Bourns_MF-RG1000.wrl")

OOMP.parts.append(newPart)