###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_RJ")
newPart.addTag("oompIndex", "RJ45_Amphenol_54602-x08_Horizontal")

newPart.addTag("kicadDesc", "8 Pol Shallow Latch Connector, Modjack, RJ45 (https://cdn.amphenol-icc.com/media/wysiwyg/files/drawing/c-bmj-0102.pdf)")
newPart.addTag("kicadTags", "RJ45")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_RJ.3dshapes/RJ45_Amphenol_54602-x08_Horizontal.wrl")

OOMP.parts.append(newPart)