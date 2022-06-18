###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_QFP")
newPart.addTag("oompIndex", "EQFP-144-1EP_20x20mm_P0.5mm_EP7.2x6.35mm_ThermalVias")

newPart.addTag("kicadDesc", "EQFP, 144 Pin (https://www.intel.com/content/dam/www/programmable/us/en/pdfs/literature/packaging/04r00487-01.pdf), generated with kicad-footprint-generator ipc_gullwing_generator.py")
newPart.addTag("kicadTags", "EQFP QFP")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/EQFP-144-1EP_20x20mm_P0.5mm_EP7.2x6.35mm.wrl")

OOMP.parts.append(newPart)