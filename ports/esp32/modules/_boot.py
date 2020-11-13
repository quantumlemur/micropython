import gc
import uos
from flashbdev import bdev
from machine import WDT

WDT(timeout=10*60*1000) # Global watchdog timer @ 10 minutes

try:
    if bdev:
        uos.mount(bdev, "/")
        if "lfs2File" not in uos.listdir():
            uos.umount("/")
            uos.VfsLfs2.mkfs(bdev)
            uos.mount(bdev, "/")

            with open("lfs2File", 'w') as f:
                f.write('asdasdasd')
except OSError:
    import inisetup

    vfs = inisetup.setup()
    

   # os.VfsLfs2.mkfs(bdev)
   # uos.mount(bdev, "/")
   # with open("testfile", 'w') as f:
   #     f.write("asdasd")
   # uos.umount("/")



gc.collect()
