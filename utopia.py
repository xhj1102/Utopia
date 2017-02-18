# Note: Use reflection to initialize custom GameServer.py
#from person import Person
#theObj = globals()["Person"]()
#print theObj.getName()


# Utopia - A government simulator that works
# Aurura 2017. Published under the MITv3 License.
# https://github.com/xhj1102/Utopia
#
# Entry for command-line interaction.
# utopia.py - Main Program
#

import time
from multiprocessing import Process, Queue
import lib.GameServer as GameServer

#         .fjttii;iijfjtiitjft
#       :ffjttttitjjfjttjjjjjttt.
#      :ffjLffjjjjffftjjjjfffttit
#     :GLGGLLLLLffffjjttjjfLfLLft,
#     GLGGGGLGLLLLffLjtjitjLjjjtjt
#    GLGGDGLGGLGGfLLLjjftttfjjjjtt
#    LGGDDDGDGGGGGGDGfjitjjjGLGDfj,
#   ,EGDDDDDGGGLGLGLGGfjfjjjfLGfjfL
#    #EDDDGEEDDGGGGLGDEfLffjGGfjtjf
#    WDDDDDDEDDDGGfLLGDEDfjf#fDtttf
#    WDEDDDGDGGDEDfLLGDDKKKG   Lijj:
#    KEKEDDGGGEDKLjLGGG#KKEK    ..fi:
#    .GKKEDGLGEKELLGLLtKEGGD     LLi
#   : GGKKDGGG;i.GfLfG  DGGD     jfG
#   W DGEWEDDD   tLfLD  GLLL     .fG
#   W DDKt LDD    LfL:  ffLL      fL
#   # EK:.  GD    LLL    DGG      fL
#    .EK    GG    LLL    DGG      ,f,
#    EEK    GG:   LfG    ,Lf       Kf
#    DDW    GGG ffLGE     LL        fL
#   :DDL    EGLffGDK      GD         G
#   :DGD     GLGLE        Gf,         L
#   EEDD,    GD ,        .fLL.        .L


def createTimeServer(queue):
    server = GameServer.GameServer(queue)
    pass

q = Queue()
p = Process(target=createTimeServer, args=(q,))
p.start()
