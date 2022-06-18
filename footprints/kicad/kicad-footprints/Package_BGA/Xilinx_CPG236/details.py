###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_CPG236")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_CPG236")

newPart.addTag("kicadDesc", "Artix-7 BGA, 19x19 grid, 10x10mm package, 0.5mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=266, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 238 0.5 CP236 CPG236")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_CPG236.wrl")

OOMP.parts.append(newPart)