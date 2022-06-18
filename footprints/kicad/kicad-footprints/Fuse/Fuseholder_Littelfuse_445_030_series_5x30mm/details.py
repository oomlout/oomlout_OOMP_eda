###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Fuse")
newPart.addTag("oompIndex", "Fuseholder_Littelfuse_445_030_series_5x30mm")

newPart.addTag("kicadDesc", "Littelfuse clips, https://www.littelfuse.com/~/media/electronics/datasheets/fuse_clips/littelfuse_fuse_clip_100_445_030_520_datasheet.pdf.pdf")
newPart.addTag("kicadTags", "Fuseholder clips")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Littelfuse_445_030_series_5x30mm.wrl")

OOMP.parts.append(newPart)