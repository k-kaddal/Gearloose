import cv2
import logging 
import os
import random
import argparse
import string

def rand_string(length):
    rand_string=''.join(random.choice(
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.digits)
        for i in range(length))
    return rand_string

def length_video(video_path):
    cap=cv2.VideoCapture(video_path)
    length=int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    return length

def extracting_frame(video_path, save_path, skip_frames=30):
    
    _,file_name=os.path.split(video_path)
    file_name_without_extention=os.path.splitext(file_name)[0]

    length = length_video(video_path)
    if length==0:
        print('Length is 0, exiting extracting frames!')
        return 0
    
    cap = cv2.VideoCapture(video_path)
    count=0
    random_string = rand_string(5)

    ret,frame=cap.read()
    test_file_path=os.path.join(
        save_path,
        file_name_without_extention[:6]+\
        '{}_{}.jpeg'.format(random_string,count))

    cv2.imwrite(test_file_path,frame)
    if os.path.isfile(test_file_path):
        print('Saving Test Frame was successful,' + ' Continuing Extraction')

        count=1
        while ret:
            ret,frame=cap.read()
            if ret and count % skip_frames==0:
                cv2.imwrite(os.path.join(
                    save_path,
                    file_name_without_extention[:6]+\
                    '{}_{}.jpeg'.format(random_string,count)), frame)
                count+=1
                print(count)
            else:
                count+=1
    
    else:
        print('Problem with Saving Test Frame cv2 encoding, cannot save file')
        return 0
    
    cap.release()
    print('Extraction Finished')


def parse_args():
    desc = "Tools to extract frames from video" 
    parser = argparse.ArgumentParser(description="Tools to extract frames from video")

    parser.add_argument('-v','--video_path', type=str,
        help='Path of the video file to be extracted.')

    parser.add_argument('-o','--output_folder', type=str,
        default='./output/',
        help='Directory path to the outputs folder. (default: %(default)s)')

    parser.add_argument('-f','--frames', type=int,
        default=30,
        help='Numbers of frames to be skiped. (default: %(default)s)')


    args = parser.parse_args()
    return args

if __name__ == "__main__":

    global args
    args = parse_args()

    movie=args.video_path    
    save_path = args.output_folder
    skip_frames=args.frames

    extracting_frame(movie, save_path,skip_frames)