###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_CSP")
newPart.addTag("oompIndex", "WLCSP-56_3.170x3.444mm_Layout7x8_P0.4mm")

newPart.addTag("kicadDesc", "WLCSP-56, 7x8 raster, 3.170x3.444mm package, pitch 0.4mm; see section 48.2.4 of http://ww1.microchip.com/downloads/en/DeviceDoc/DS60001479B.pdf")
newPart.addTag("kicadTags", "BGA 56 0.4")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_CSP.3dshapes/WLCSP-56_3.170x3.444mm_Layout7x8_P0.4mm.wrl")

OOMP.parts.append(newPart)