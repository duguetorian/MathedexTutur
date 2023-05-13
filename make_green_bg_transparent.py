import cv2
import imageio
import numpy as np
import sys

if __name__ == "__main__":
    if "--help" in sys.argv:
        print(
            "Options:\n --video <video_path> : the video to convert\n --o <output_path> : the path of the output file"
        )
        sys.exit()

    if "--video" in sys.argv:
        vidx = sys.argv.index("--video")
        try:
            video = sys.argv[vidx + 1]
        except IndexError:
            print("You must enter the video path after video")
            sys.exit()
    else:
        print("You need to put a video file after --video argument")

    if "--o" in sys.argv:
        oidx = sys.argv.index("--o")
        try:
            output = sys.argv[oidx + 1]
        except IndexError:
            print("You must put a valid path for the outpu after --o")

    else:
        output = f'{video.split(".")[0]}.gif'

    cap = cv2.VideoCapture(video)

    img_lst = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame2 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        indices = np.where((frame2[..., 1] - frame2[..., 0] - frame2[..., 2] > 10) & (frame2[..., 1] > 50))
        frame2[indices[0], indices[1], -1] = 0
        img_lst.append(frame2)



    # print(img_lst)
    # Convert to webp using the imageio.mimsave method
    imageio.mimsave(output, img_lst)
    # imageio.show_formats()
