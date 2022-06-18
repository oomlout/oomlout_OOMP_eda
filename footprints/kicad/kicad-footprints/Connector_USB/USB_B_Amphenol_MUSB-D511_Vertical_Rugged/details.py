###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Connector_USB")
newPart.addTag("oompIndex", "USB_B_Amphenol_MUSB-D511_Vertical_Rugged")

newPart.addTag("kicadDesc", "A,phenol MUSB_D511, USB B female connector, straight, rugged, https://www.amphenolcanada.com/ProductSearch/drawings/AC/MUSBD511XX.pdf")
newPart.addTag("kicadTags", "USB_B_MUSB_Straight female connector straight rugged MUSB D511")
newPart.addTag("kicadAttr", "through_hole")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Connector_USB.3dshapes/USB_B_Amphenol_MUSB-D511_Vertical_Rugged.wrl")

OOMP.parts.append(newPart)