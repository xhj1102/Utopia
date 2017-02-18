# Utopia - A government simulator that works
# Aurura 2017. Published under the MITv3 License.
# https://github.com/xhj1102/Utopia
#
# Template class for Game Servers.

import time
import ticking

#################################################################################
# TO DEVELOPERS: Content must INCLUDE an implementation of this template class! #
#################################################################################

TIMING_VERY_SLOW = 1000    # A tick per 0.27 hours
TIMING_SLOW = 5            # A tick per 5 secs
TIMING_NORMAL = 2          # A tick per 2 secs
TIMING_FAST = 1            # A tick per 1 sec

debugging = True

class GameServer:

    runningRate = TIMING_NORMAL;

    def __init__(self, queue):
        self.timeUpdater()
        pass

    def timeUpdater(self):
        for frame, t in ticking.Clock(self.runningRate):
            self.onTimeUpdate()
            #if(debugging):
            print(frame, t)

    def onTimeUpdate(self):
        # Developers: Implement this in the corresponding content class.
        pass
