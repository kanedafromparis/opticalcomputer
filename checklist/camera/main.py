from picamzero import Camera
import datetime

if __name__ == '__main__':
    x = datetime.datetime.now()
    print(x.strftime("%Y-%m-%d-%H-%M-%S-%f"))
    cam = Camera()
    cam.capture_sequence("sequence-"+x.strftime("%Y-%m-%d-%H-%M-%S")+".jpg", num_images=5, interval=0.5)
    x = datetime.datetime.now()
    cam.take_photo(x.strftime("%Y-%m-%d-%H-%M-%S-%f"))