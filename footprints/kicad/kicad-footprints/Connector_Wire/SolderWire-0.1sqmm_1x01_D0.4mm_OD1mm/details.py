###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-0.1sqmm_1x01_D0.4mm_OD1mm")
newPart.addTag("oompName", "kicad-footprints/Connector_Wire/SolderWire-0.1sqmm_1x01_D0.4mm_OD1mm")

newPart.addTag("kicadDesc", "Soldered wire connection, for a single 0.1 mm² wire, basic insulation, conductor diameter 0.4mm, outer diameter 1mm, size source Multi-Contact FLEXI-E 0.1 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 0.1sqmm")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.1sqmm_1x01_D0.4mm_OD1mm.wrl")

OOMP.parts.append(newPart)