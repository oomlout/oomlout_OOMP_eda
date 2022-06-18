###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DirectFET")
newPart.addTag("oompIndex", "DirectFET_MZ")
newPart.addTag("oompName", "kicad-footprints/Package_DirectFET/DirectFET_MZ")

newPart.addTag("kicadDesc", "DirectFET MZ https://www.infineon.com/dgdl/Infineon-AN-1035-ApplicationNotes-v29_01-EN.pdf?fileId=5546d462533600a40153559159020f76#page=31")
newPart.addTag("kicadTags", "DirectFET MZ MOSFET Infineon")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DirectFET.3dshapes/DirectFET_MZ.wrl")

OOMP.parts.append(newPart)