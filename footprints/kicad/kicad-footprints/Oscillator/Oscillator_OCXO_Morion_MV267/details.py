###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Oscillator")
newPart.addTag("oompIndex", "Oscillator_OCXO_Morion_MV267")

newPart.addTag("kicadDesc", "http://www.morion.com.ru/catalog_pdf/MV267.pdf")
newPart.addTag("kicadTags", "OCXO")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Oscillator.3dshapes/Oscillator_OCXO_Morion_MV267.wrl")

OOMP.parts.append(newPart)