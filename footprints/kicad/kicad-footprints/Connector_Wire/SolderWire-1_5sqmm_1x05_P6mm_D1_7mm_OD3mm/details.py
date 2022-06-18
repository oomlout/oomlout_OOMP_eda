###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-1.5sqmm_1x05_P6mm_D1.7mm_OD3mm")

newPart.addTag("kicadDesc", "Soldered wire connection, for 5 times 1.5 mm² wires, basic insulation, conductor diameter 1.7mm, outer diameter 3mm, size source Multi-Contact FLEXI-E 1.5 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 1.5sqmm")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-1.5sqmm_1x05_P6mm_D1.7mm_OD3mm.wrl")

OOMP.parts.append(newPart)