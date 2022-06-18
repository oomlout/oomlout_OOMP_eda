###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DIP")
newPart.addTag("oompIndex", "Fairchild_LSOP-8")

newPart.addTag("kicadDesc", "8-Lead, 300\\\" Wide, Surface Mount Package (https://www.fairchildsemi.com/package-drawings/ML/MLSOP08A.pdf)")
newPart.addTag("kicadTags", "LSOP 2.54mm 300mil")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DIP.3dshapes/Fairchild_LSOP-8.wrl")

OOMP.parts.append(newPart)