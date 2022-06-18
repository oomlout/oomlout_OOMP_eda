###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_Coaxial")
newPart.addTag("oompIndex", "SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount")

newPart.addTag("kicadDesc", "Connector SMA, 0Hz to 20GHz, 50Ohm, Edge Mount (http://suddendocs.samtec.com/prints/sma-j-p-x-st-em1-mkt.pdf)")
newPart.addTag("kicadTags", "SMA Straight Samtec Edge Mount")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_Coaxial.3dshapes/SMA_Samtec_SMA-J-P-X-ST-EM1_EdgeMount.wrl")

OOMP.parts.append(newPart)