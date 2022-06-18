###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "UDFN-10_1.35x2.6mm_P0.5mm")

newPart.addTag("kicadDesc", "http://www.st.com/content/ccc/resource/technical/document/datasheet/f2/11/8a/ed/40/31/40/56/DM00088292.pdf/files/DM00088292.pdf/jcr:content/translations/en.DM00088292.pdf")
newPart.addTag("kicadTags", "UDFN 0.5 uQFN")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/UDFN-10_1.35x2.6mm_P0.5mm.wrl")

OOMP.parts.append(newPart)