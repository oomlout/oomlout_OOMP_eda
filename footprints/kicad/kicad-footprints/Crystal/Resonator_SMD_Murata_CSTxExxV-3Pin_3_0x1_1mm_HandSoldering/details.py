###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Crystal")
newPart.addTag("oompIndex", "Resonator_SMD_Murata_CSTxExxV-3Pin_3.0x1.1mm_HandSoldering")

newPart.addTag("kicadDesc", "SMD Resomator/Filter Murata CSTCE, https://www.murata.com/en-eu/products/productdata/8801162264606/SPEC-CSTNE16M0VH3C000R0.pdf")
newPart.addTag("kicadTags", "SMD SMT ceramic resonator filter")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Resonator_SMD_Murata_CSTxExxV-3Pin_3.0x1.1mm.wrl")

OOMP.parts.append(newPart)