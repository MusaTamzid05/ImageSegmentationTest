import cv2
from processor import Processor

lower_hue1 = 10
higher_hue1 = 100

lower_segmentation1 = 10
higher_segmention1 = 100


lower_value1 = 10
higher_value1 = 100


lower_hue2 = 10
higher_hue2 = 100

lower_segmentation2 = 10
higher_segmention2 = 100


lower_value2 = 10
higher_value2 = 100

def show_values():

    print("Lower Hue 1: {}".format(lower_hue1))
    print("Higher Hue 1 : {}".format(higher_hue1))
    print("Lower Segmentation 1: {}".format(lower_segmentation1))
    print("Higher Segmentation 1: {}".format(higher_segmention1))
    print("Lower Value 1: {}".format(lower_value1))
    print("Higher Value 1: {}".format(higher_value1))


    print("Lower Hue 2: {}".format(lower_hue2))
    print("Higher Hue 2: {}".format(higher_hue2))
    print("Lower Segmentation 2 : {}".format(lower_segmentation2))
    print("Higher Segmentation 2 : {}".format(higher_segmention2))
    print("Lower Value 2 : {}".format(lower_value2))
    print("Higher Value 2 : {}".format(higher_value2))

def update_lower_hue1(value):

    global lower_hue1

    if value > higher_hue1:
        print("cannot update => lower_h > higher_h")
        return

    lower_hue1 = value
    show_values()


def update_higher_hue1(value):

    global higher_hue1

    if value < lower_hue1:
        print("Cannot update => lower_hue1 > higher_hue1")
        return

    higher_hue1 = value
    show_values()


def update_lower_segmentation1(value):

    global lower_segmentation1

    if value >  higher_segmention1:
        print("cannot update => lower_segmentation1 > higher_segmention1")
        return

    lower_segmentation1 = value
    show_values()

def update_higher_segmention1(value):

    global higher_segmention1

    if value < lower_segmentation1:
        print("cannot update => lower_segmentation1 > higher_segmention1")
        return

    higher_segmention1 = value
    show_values()


def update_lower_value1(value):

    global lower_value1

    if value > higher_value1:
        print("cannot update => lower_value1 > higher_value1")
        return

    lower_value1 = value
    show_values()


def update_higher_value1(value):

    global higher_value1

    if value < lower_value1:
        print("cannot update => lower_value1 > higher_segmention1")
        return

    higher_value1 = value
    show_values()


def update_lower_hue2(value):

    global lower_hue2

    if value > higher_hue2:
        print("cannot update => lower_h > higher_h")
        return

    lower_hue2 = value
    show_values()


def update_higher_hue2(value):

    global higher_hue2

    if value < lower_hue2:
        print("Cannot update => lower_hue2 > higher_hue2")
        return

    higher_hue2 = value
    show_values()


def update_lower_segmentation2(value):

    global lower_segmentation2

    if value >  higher_segmention2:
        print("cannot update => lower_segmentation2 > higher_segmention2")
        return

    lower_segmentation2 = value
    show_values()

def update_higher_segmention2(value):

    global higher_segmention2

    if value < lower_segmentation2:
        print("cannot update => lower_segmentation2 > higher_segmention2")
        return

    higher_segmention2 = value
    show_values()


def update_lower_value2(value):

    global lower_value2

    if value > higher_value2:
        print("cannot update => lower_value2 > higher_value2")
        return

    lower_value2 = value
    show_values()

def update_higher_value2(value):

    global higher_value2

    if value < lower_value2:
        print("cannot update => lower_value2 > higher_segmention2")
        return

    higher_value2 = value
    show_values()


class App:

    def __init__(self , src):
        self.src = src
        self._init_window()
        self.processor = Processor()

    def _init_window(self):
        self.window_name =  "Window"
        cv2.namedWindow(self.window_name , cv2.WINDOW_NORMAL)
        cv2.createTrackbar("lower_h1" , self.window_name , lower_hue1 , 180 ,  update_lower_hue1)
        cv2.createTrackbar("higher_h1" , self.window_name , higher_hue1 , 180 ,  update_higher_hue1)
        cv2.createTrackbar("lower_s1" , self.window_name , lower_segmentation1 , 255,  update_lower_segmentation1)
        cv2.createTrackbar("higher_s1" , self.window_name , higher_segmention1 , 255 ,  update_higher_segmention1)
        cv2.createTrackbar("lower_v1" , self.window_name , lower_value1, 255 ,  update_lower_value1)
        cv2.createTrackbar("higher_v1" , self.window_name , higher_value1 , 255,  update_higher_value1)


        cv2.createTrackbar("lower_h2" , self.window_name , lower_hue2 , 180 ,  update_lower_hue2)
        cv2.createTrackbar("higher_h2" , self.window_name , higher_hue2 , 180 ,  update_higher_hue2)
        cv2.createTrackbar("lower_s2" , self.window_name , lower_segmentation2 , 255,  update_lower_segmentation2)
        cv2.createTrackbar("higher_s2" , self.window_name , higher_segmention2 , 255 ,  update_higher_segmention2)
        cv2.createTrackbar("lower_v2" , self.window_name , lower_value2, 255 ,  update_lower_value2)
        cv2.createTrackbar("higher_v2" , self.window_name , higher_value2 , 255,  update_higher_value2)

        self.result_window = "Result"
        cv2.namedWindow(self.result_window , cv2.WINDOW_NORMAL)



    def _display_result(self , image):
        result = self.processor.process(image = image ,
                    min_range = [lower_hue1 , lower_segmentation1 , lower_value1],
                    max_range = [higher_hue1 , higher_segmention1 , higher_value1])
        cv2.imshow(self.result_window , result)


    def run(self):

        video_src = False

        if self.src.endswith("mp4") or type(self.src) == int:
            video_src = True
            cap = cv2.VideoCapture(self.src)

        if video_src == False:
            image = cv2.imread(self.src)

            if image is None:
                print("No a valid image => {}".format(self.src))
                return

        while True:

            if video_src:
                _ , image = cap.read()


            self._display_result(image)
            cv2.imshow(self.window_name , image)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break





