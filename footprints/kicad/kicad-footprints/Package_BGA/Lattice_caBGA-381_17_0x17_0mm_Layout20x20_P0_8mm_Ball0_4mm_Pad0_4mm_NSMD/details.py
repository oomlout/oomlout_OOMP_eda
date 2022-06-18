###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Lattice_caBGA-381_17.0x17.0mm_Layout20x20_P0.8mm_Ball0.4mm_Pad0.4mm_NSMD")

newPart.addTag("kicadDesc", "Lattice caBGA-381 footprint for ECP5 FPGAs, based on http://www.latticesemi.com/view_document?document_id=213")
newPart.addTag("kicadTags", "BGA 381 0.8")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Lattice_caBGA-381_17.0x17.0mm_Layout20x20_P0.8mm_Ball0.4mm_Pad0.4mm_NSMD.wrl")

OOMP.parts.append(newPart)