from mcpi.minecraft import Minecraft
mc = Minecraft.create()  
import time
myid = mc.getPlayerEntityId("YT_nugget")
mc.postToTitle(myid,"fuck")
time.sleep(10)