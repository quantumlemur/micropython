import gc
import uos
from flashbdev import bdev

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
