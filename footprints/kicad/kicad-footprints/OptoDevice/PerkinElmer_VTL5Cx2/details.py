###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "OptoDevice")
newPart.addTag("oompIndex", "PerkinElmer_VTL5Cx2")

newPart.addTag("kicadDesc", "Axial Vactrol (http://www.qsl.net/wa1ion/vactrol/vactrol.pdf)")
newPart.addTag("kicadTags", "vactrol")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/OptoDevice.3dshapes/PerkinElmer_VTL5Cx2.wrl")

OOMP.parts.append(newPart)