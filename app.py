import cv2

class App:

    def __init__(self , src):
        self.src = src
        self.window_name =  "Press q to quit"

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

        self._show(image)
        cv2.waitKey()

    def _show(self , image):

        cv2.namedWindow(self.window_name , cv2.WINDOW_NORMAL)
        cv2.imshow(self.window_name , image)




def main():

    app = App(src = "./test.mp4")
    app.run()

if __name__ == "__main__":
    main()
