###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_SO")
newPart.addTag("oompIndex", "SSOP-18_4.4x6.5mm_P0.65mm")

newPart.addTag("kicadDesc", "SSOP18: plastic shrink small outline package; 18 leads; body width 4.4 mm (http://toshiba.semicon-storage.com/info/docget.jsp?did=30523&prodName=TBD62783APG)")
newPart.addTag("kicadTags", "SSOP 0.65")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/SSOP-18_4.4x6.5mm_P0.65mm.wrl")

OOMP.parts.append(newPart)