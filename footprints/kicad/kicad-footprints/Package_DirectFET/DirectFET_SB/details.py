###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DirectFET")
newPart.addTag("oompIndex", "DirectFET_SB")
newPart.addTag("oompName", "kicad-footprints/Package_DirectFET/DirectFET_SB")

newPart.addTag("kicadDesc", "DirectFET SB https://www.infineon.com/dgdl/Infineon-AN-1035-ApplicationNotes-v29_01-EN.pdf?fileId=5546d462533600a40153559159020f76#page=23")
newPart.addTag("kicadTags", "DirectFET SB MOSFET Infineon")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DirectFET.3dshapes/DirectFET_SB.wrl")

OOMP.parts.append(newPart)