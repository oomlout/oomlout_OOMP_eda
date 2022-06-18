###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DirectFET")
newPart.addTag("oompIndex", "DirectFET_MD")

newPart.addTag("kicadDesc", "DirectFET MD https://www.infineon.com/dgdl/Infineon-AN-1035-ApplicationNotes-v29_01-EN.pdf?fileId=5546d462533600a40153559159020f76#page=38")
newPart.addTag("kicadTags", "DirectFET MD MOSFET Infineon")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DirectFET.3dshapes/DirectFET_MD.wrl")

OOMP.parts.append(newPart)