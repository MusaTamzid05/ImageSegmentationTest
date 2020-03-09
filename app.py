import cv2
from processor import Processor

lower_hue = 10
higher_hue = 100

lower_segmentation = 10
higher_segmentation = 100


lower_value = 10
higher_value = 100

def show_values():

    print("Lower Hue : {}".format(lower_hue))
    print("Higher Hue : {}".format(higher_hue))
    print("Lower Segmentation : {}".format(lower_segmentation))
    print("Higher Segmentation : {}".format(higher_segmentation))
    print("Lower Value : {}".format(lower_value))
    print("Higher AValue : {}".format(higher_value))

def update_lower_hue(value):

    global lower_hue

    if value > higher_hue:
        print("cannot update => lower_h > higher_h")
        return

    lower_hue = value
    show_values()


def update_higher_hue(value):

    global higher_hue

    if value < lower_hue:
        print("Cannot update => lower_hue > higher_hue")
        return

    higher_hue = value
    show_values()


def update_lower_segmentation(value):

    global lower_segmentation

    if value >  higher_segmentation:
        print("cannot update => lower_segmentation > higher_segmentation")
        return

    lower_segmentation = value
    show_values()

def update_higher_segmentation(value):

    global higher_segmentation

    if value < lower_segmentation:
        print("cannot update => lower_segmentation > higher_segmentation")
        return

    higher_segmentation = value
    show_values()


def update_lower_value(value):

    global lower_value

    if value > higher_value:
        print("cannot update => lower_value > higher_value")
        return

    lower_value = value
    show_values()


def update_higher_value(value):

    global higher_value

    if value < lower_value:
        print("cannot update => lower_value > higher_segmentation")
        return

    higher_value = value
    show_values()



class App:

    def __init__(self , src):
        self.src = src
        self._init_window()
        self.processor = Processor()

    def _init_window(self):
        self.window_name =  "Window"
        cv2.namedWindow(self.window_name , cv2.WINDOW_NORMAL)
        cv2.createTrackbar("lower_h" , self.window_name , lower_hue , 180 ,  update_lower_hue)
        cv2.createTrackbar("higher_h" , self.window_name , higher_hue , 180 ,  update_higher_hue)
        cv2.createTrackbar("lower_s" , self.window_name , lower_segmentation , 180 ,  update_lower_segmentation)
        cv2.createTrackbar("higher_s" , self.window_name , higher_segmentation , 180 ,  update_higher_segmentation)
        cv2.createTrackbar("lower_v" , self.window_name , lower_value, 180 ,  update_lower_value)
        cv2.createTrackbar("higher_v" , self.window_name , higher_value , 180 ,  update_higher_value)

    def run(self):

        if self.src.endswith("mp4") or type(self.src) == int:
            self._run_camera()
            return

        self._display_image()


    def _run_camera(self):

        cap = cv2.VideoCapture(self.src)

        while True:
            _ , frame = cap.read()

            self._show(frame)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        cap.release()
        cv2.destroyAllWindows()

    def _display_image(self):

        image = cv2.imread(self.src)

        if image is None:
            print("No a valid image => {}".format(self.src))
            return

        image = self.processor.process(image)
        self._show(image)
        cv2.waitKey()

    def _show(self , image):

        cv2.imshow(self.window_name , image)




