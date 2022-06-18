###### OOMP FILE  ######

import OOMP

newPart = OOMP.oompItem()

newPart.addTag("hexID", "")
newPart.addTag("oompType", "FOOTPRINT")
newPart.addTag("oompSize", "kicad")
newPart.addTag("oompColor", "kicad-footprints")
newPart.addTag("oompDesc", "Package_BGA")
newPart.addTag("oompIndex", "Xilinx_CLG484_CLG485")
newPart.addTag("oompName", "kicad-footprints/Package_BGA/Xilinx_CLG484_CLG485")

newPart.addTag("kicadDesc", "Zynq-7000 BGA, 22x22 grid, 19x19mm package, 0.8mm pitch; https://www.xilinx.com/support/documentation/user_guides/ug865-Zynq-7000-Pkg-Pinout.pdf#page=79, NSMD pad definition Appendix A")
newPart.addTag("kicadTags", "BGA 484 0.8 CLG484 CL484 CLG485 CL485")
newPart.addTag("kicadAttr", "smd")
newPart.addTag("kicad3DModel", "${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Xilinx_CLG484_CLG485.wrl")

OOMP.parts.append(newPart)