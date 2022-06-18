###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "PQFP-132_24x24mm_P0.635mm_i386")
newPart.addTag("oompName", "kicad-footprints/Package_QFP/PQFP-132_24x24mm_P0.635mm_i386")

newPart.addTag("kicadDesc", "PQFP, 132 pins, 24mm sq body, 0.635mm pitch, Intel 386EX (https://www.intel.com/content/dam/www/public/us/en/documents/packaging-databooks/packaging-chapter-02-databook.pdf, http://www.nxp.com/docs/en/application-note/AN4388.pdf)")
newPart.addTag("kicadTags", "PQFP 132 Intel 386EX")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/PQFP-132_24x24mm_P0.635mm_i386.wrl")

OOMP.parts.append(newPart)