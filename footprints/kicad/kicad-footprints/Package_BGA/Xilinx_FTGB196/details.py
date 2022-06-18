###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_FTGB196")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_FTGB196")

newPart.addTag("kicadDesc", "Spartan-7 BGA, 14x14 grid, 15x15mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=261, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 196 1 FTGB196")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_FTGB196.wrl")

OOMP.parts.append(newPart)