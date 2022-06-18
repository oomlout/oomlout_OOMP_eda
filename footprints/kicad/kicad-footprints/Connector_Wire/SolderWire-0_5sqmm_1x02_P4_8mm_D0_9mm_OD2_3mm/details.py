###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-0.5sqmm_1x02_P4.8mm_D0.9mm_OD2.3mm")
newPart.addTag("oompName", "kicad-footprints/Connector_Wire/SolderWire-0.5sqmm_1x02_P4.8mm_D0.9mm_OD2.3mm")

newPart.addTag("kicadDesc", "Soldered wire connection, for 2 times 0.5 mm² wires, reinforced insulation, conductor diameter 0.9mm, outer diameter 2.3mm, size source Multi-Contact FLEXI-xV 0.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 0.5sqmm")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.5sqmm_1x02_P4.8mm_D0.9mm_OD2.3mm.wrl")

OOMP.parts.append(newPart)