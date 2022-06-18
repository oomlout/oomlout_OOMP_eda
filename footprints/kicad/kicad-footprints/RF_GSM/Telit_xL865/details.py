###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "RF_GSM")
newPart.addTag("oompIndex", "Telit_xL865")

newPart.addTag("kicadDesc", "Telit xL865 familly footprint, http://www.telit.com/fileadmin/user_upload/products/Downloads/3G/Telit_UL865_Hardware_User_Guide_r8.pdf")
newPart.addTag("kicadTags", "xL865 gsm umts")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/RF_GSM.3dshapes/Telit_xL865.wrl")

OOMP.parts.append(newPart)