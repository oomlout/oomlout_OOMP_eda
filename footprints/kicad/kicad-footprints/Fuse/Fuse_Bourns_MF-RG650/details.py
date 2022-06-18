###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fuse")
newPart.addTag("oompIndex", "Fuse_Bourns_MF-RG650")

newPart.addTag("kicadDesc", "PTC Resettable Fuse, Ihold = 6.5A, Itrip=11.1A, http://www.bourns.com/docs/Product-Datasheets/mfrg.pdf")
newPart.addTag("kicadTags", "ptc resettable fuse polyfuse THT")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_Bourns_MF-RG650.wrl")

OOMP.parts.append(newPart)