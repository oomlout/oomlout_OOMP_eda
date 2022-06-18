###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "PQFP-112_20x20mm_P0.65mm")

newPart.addTag("kicadDesc", "PQFP, 112 pins, 20mm sq body, 0.65mm pitch (http://cache.freescale.com/files/shared/doc/package_info/98ASS23330W.pdf, http://www.nxp.com/docs/en/application-note/AN4388.pdf)")
newPart.addTag("kicadTags", "PQFP 112")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/PQFP-112_20x20mm_P0.65mm.wrl")

OOMP.parts.append(newPart)