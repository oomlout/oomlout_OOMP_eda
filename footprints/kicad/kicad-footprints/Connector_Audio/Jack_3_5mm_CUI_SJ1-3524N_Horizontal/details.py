###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Audio")
newPart.addTag("oompIndex", "Jack_3.5mm_CUI_SJ1-3524N_Horizontal")

newPart.addTag("kicadDesc", "TRS 3.5mm, horizontal, through-hole, https://www.cuidevices.com/product/resource/pdf/sj1-352xn.pdf")
newPart.addTag("kicadTags", "TRS audio jack stereo horizontal")
newPart.addTag("kicadAttr", "through_hole exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Audio.3dshapes/Jack_3.5mm_CUI_SJ1-3524N_Horizontal.wrl")

OOMP.parts.append(newPart)