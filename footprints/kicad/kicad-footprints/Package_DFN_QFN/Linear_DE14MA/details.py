###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_DFN_QFN")
newPart.addTag("oompIndex", "Linear_DE14MA")

newPart.addTag("kicadDesc", "14-Lead Plastic DFN, 4mm x 3mm (http://www.analog.com/media/en/package-pcb-resources/package/pkg_pdf/ltc-legacy-dfn/05081731_C_DE14MA.pdf)")
newPart.addTag("kicadTags", "DFN 0.5")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_DFN_QFN.3dshapes/Linear_DE14MA.wrl")

OOMP.parts.append(newPart)