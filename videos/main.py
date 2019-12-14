import cv2
def main():
    """ main function """
    cap = cv2.VideoCapture(0) # get camera

    fourcc = cv2.VideoWriter_fourcc(*'XVID') # video codec

    # output video as .mp4 with fourcc codec 20 FPS with 1280 * 720
    out = cv2.VideoWriter("output.mp4", fourcc, 20, (1280, 720))

    while (cap.isOpened()): # while camera is open
        rdy, frame = cap.read() # read camera current frame

        if (rdy): # if this camera frame ready
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # convert camera frame color to gray

            cv2.imshow("Camera", frame) # display camera frame
            cv2.imshow("Camera gray", gray) # display gray frame

            out.write(frame) # write frame to output.mp4

            print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # show camera width
            print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # show camera height

            if (cv2.waitKey(1) & 0xFF == ord("q")): # if press 'q' key break the loop
                break
        else:
            break

    cap.release() # release camera
    out.release() # release out
    cv2.destroyAllWindows() # close all windows
main()
