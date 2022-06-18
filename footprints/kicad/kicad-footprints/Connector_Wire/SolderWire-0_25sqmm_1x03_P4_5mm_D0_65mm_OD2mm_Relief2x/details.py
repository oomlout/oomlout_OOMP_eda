###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Wire")
newPart.addTag("oompIndex", "SolderWire-0.25sqmm_1x03_P4.5mm_D0.65mm_OD2mm_Relief2x")

newPart.addTag("kicadDesc", "Soldered wire connection with double feed through strain relief, for 3 times 0.25 mm² wires, reinforced insulation, conductor diameter 0.65mm, outer diameter 2mm, size source Multi-Contact FLEXI-2V 0.25 (https://ec.staubli.com/AcroFiles/Catalogues/TM_Cab-Main-11014119_(en)_hi.pdf), bend radius 3 times outer diameter, generated with kicad-footprint-generator")
newPart.addTag("kicadTags", "connector wire 0.25sqmm double-strain-relief")
newPart.addTag("kicadAttr", "exclude_from_pos_files exclude_from_bom")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Wire.3dshapes/SolderWire-0.25sqmm_1x03_P4.5mm_D0.65mm_OD2mm_Relief2x.wrl")

OOMP.parts.append(newPart)