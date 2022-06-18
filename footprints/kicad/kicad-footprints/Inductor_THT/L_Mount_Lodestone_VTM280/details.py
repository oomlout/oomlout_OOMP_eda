###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Inductor_THT")
newPart.addTag("oompIndex", "L_Mount_Lodestone_VTM280")

newPart.addTag("kicadDesc", "Lodestone Pacific, 71.12mm diameter vertical toroid mount, 16AWG/1.27mm holes, http://www.lodestonepacific.com/CatKpdf/VTM_Series.pdf")
newPart.addTag("kicadTags", "vertical inductor toroid mount")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/L_Mount_Lodestone_VTM280.wrl")

OOMP.parts.append(newPart)