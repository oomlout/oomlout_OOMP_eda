###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_TO_SOT_THT")
newPart.addTag("oompIndex", "TO-92L_HandSolder")

newPart.addTag("kicadDesc", "TO-92L leads in-line (large body variant of TO-92), also known as TO-226, wide, drill 0.75mm, hand-soldering variant with enlarged pads (see https://www.diodes.com/assets/Package-Files/TO92L.pdf and http://www.ti.com/lit/an/snoa059/snoa059.pdf)")
newPart.addTag("kicadTags", "to-92 sc-43 sc-43a sot54 PA33 transistor")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_TO_SOT_THT.3dshapes/TO-92L.wrl")

OOMP.parts.append(newPart)