###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_RB484")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_RB484")

newPart.addTag("kicadDesc", "Artix-7 and Zynq-7000 BGA, 22x22 grid, 23x23mm package, 1mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug475_7Series_Pkg_Pinout.pdf#page=278, https://www.xilinx.com/support/documentation/user_guides/ug865-Zynq-7000-Pkg-Pinout.pdf#page=92, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 484 1 RB484")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_RB484.wrl")

OOMP.parts.append(newPart)