###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_CSGA324")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_CSGA324")

newPart.addTag("kicadDesc", "Spartan-7 BGA, 18x18 grid, 15x15mm package, 0.8mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=263, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 324 0.8 CSGA324")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_CSGA324.wrl")

OOMP.parts.append(newPart)