from random import randrange
from mcpi.minecraft import Minecraft
mc = Minecraft.create()


for j in range(100):
    x,y,z = mc.player.getTilePos()
    x = x+j
    for i in range(100):
        color = randrange(0,16)
        z = z+1
        mc.setBlock(x,y,z,35,color)
ans = randrange(0,16)
while True:
    hits = mc.events.pollBlockHits()
    if len(hits) > 0:
        h = hits[0]
        block = mc.getBlockWithData(h.pos)
        data = block.data
        if data == ans:
            mc.postToChat("恭喜你找到我啦")
            mc.setBlock(h.pos,46)
            break
        elif data < ans:
            mc.postToChat("錯!!! 再找大一點的")
        elif data > ans:
            mc.postToChat("錯!!! 再找一點的")    


