###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Toroid_Vertical_L25.4mm_W14.7mm_P12.20mm_Vishay_TJ5")

newPart.addTag("kicadDesc", "L_Toroid, Vertical series, Radial, pin pitch=12.20mm, , length*width=25.4*14.7mm^2, Vishay, TJ5, http://www.vishay.com/docs/34079/tj.pdf")
newPart.addTag("kicadTags", "L_Toroid Vertical series Radial pin pitch 12.20mm  length 25.4mm width 14.7mm Vishay TJ5")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Toroid_Vertical_L25.4mm_W14.7mm_P12.20mm_Vishay_TJ5.wrl")

OOMP.parts.append(newPart)