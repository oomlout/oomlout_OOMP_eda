###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-0.127sqmm_1x04_P3.7mm_D0.48mm_OD1mm_Relief2x")
newPart.addTag("oompName", "kicad-footprints/Connector_Wire/SolderWire-0.127sqmm_1x04_P3.7mm_D0.48mm_OD1mm_Relief2x")

newPart.addTag("kicadDesc", "Soldered wire connection with double feed through strain relief, for 4 times 0.127 mm² wires, basic insulation, conductor diameter 0.48mm, outer diameter 1mm, size source Multi-Contact FLEXI-E/HK 0.127 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 0.127sqmm double-strain-relief")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.127sqmm_1x04_P3.7mm_D0.48mm_OD1mm_Relief2x.wrl")

OOMP.parts.append(newPart)