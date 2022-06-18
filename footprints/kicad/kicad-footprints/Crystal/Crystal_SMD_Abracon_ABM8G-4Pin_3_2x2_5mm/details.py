###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Crystal_SMD_Abracon_ABM8G-4Pin_3.2x2.5mm")

newPart.addTag("kicadDesc", "Abracon Miniature Ceramic Smd Crystal ABM8G http://www.abracon.com/Resonators/ABM8G.pdf, 3.2x2.5mm^2 package")
newPart.addTag("kicadTags", "SMD SMT crystal")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_SMD_Abracon_ABM8G-4Pin_3.2x2.5mm.wrl")

OOMP.parts.append(newPart)