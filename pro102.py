from statistics import mode
import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret, frame = videoCaptureObject.read()
        image_name = "img" + str(number) + ".png"
        cv2.imwrite(image_name, frame)
        start_time = time.timeresult = False
    return image_name
    print("Snapshot Taken")
    
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
take_snapshot()

def upload_file(image_name):
    access_token = 'sl.BF9ZKcIiHfV9_PrndikWemPO0uv4UmRHgbc8MAuGl-6ZpqNFpfF9BLOZwgdzZXKTI7JyDG6NQywLIs0ZpVBW25Ihwv6Th8RlcNS4cY2eChqRAAYnq3xFd0HwolNoH05Dyzb0MB8'    
    file = image_name
    src = file
    dest = '/newfolder24' + (image_name)
    dbx = dropbox.Dropbox(access_token)
    
    with open(src, 'rb') as f:
        dbx.files_upload(f.read(), dest, mode = dropbox.files.WriteMode.overwrite)
        print('File uploaded')
        
def main():
    while(True):
        if ((time.time() - start_time) >= 3):
            name = take_snapshot()
            upload_file(name)
            
main()                    