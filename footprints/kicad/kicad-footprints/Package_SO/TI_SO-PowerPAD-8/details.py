###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "TI_SO-PowerPAD-8")

newPart.addTag("kicadDesc", "8-Lead Plastic PSOP, Exposed Die Pad (TI DDA0008B, see http://www.ti.com/lit/ds/symlink/lm3404.pdf)")
newPart.addTag("kicadTags", "SSOP 0.50 exposed pad")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/TI_SO-PowerPAD-8.wrl")

OOMP.parts.append(newPart)