###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SOIC-14-16_3.9x9.9mm_P1.27mm")
newPart.addTag("oompName", "kicad-footprints/Package_SO/SOIC-14-16_3.9x9.9mm_P1.27mm")

newPart.addTag("kicadDesc", "SOIC, 16 Pin package with pin 2 and 13 removed for voltage clearance  (UCC256301, https://www.ti.com/lit/ds/symlink/ucc256301.pdf)")
newPart.addTag("kicadTags", "SOIC SO")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SOIC-16_3.9x9.9mm_P1.27mm.wrl")

OOMP.parts.append(newPart)