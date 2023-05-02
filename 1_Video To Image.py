import cv2
import os
from glob import glob

from diffusers import StableDiffusionControlNetPipeline
from diffusers.utils import load_image

from PIL import Image
import numpy as np

from diffusers import ControlNetModel
from diffusers import UniPCMultistepScheduler
import torch, gc

from diffusers import StableDiffusionPipeline

gc.collect()
torch.cuda.empty_cache()

print(cv2.__version__)

os.getcwd()
print(os.getcwd())
os.chdir('D:\Work\Python\Video') # 현재 작업 디렉토리 변경
print(os.getcwd())


start_time =7                  # 시작 시간 (초)
end_time =start_time+10         # 종료 시간 (초)

cap = cv2.VideoCapture('video.mp4')         # 동영상 파일 열기
frame_rate = cap.get(cv2.CAP_PROP_FPS)
frame_num = 0                                 # 이미지로 저장할 프레임 번호 초기화
fps = 5

## 시작 초 ~ 끝 초 프레임 -> 이미지로 저장
while True:   
    for i in range(fps):
        ret, frame = cap.read()
     
        if not ret:                         # 읽은 프레임이 없으면 종료
            break
        
    current_time = cap.get(cv2.CAP_PROP_POS_MSEC) / 1000.0

    if current_time < start_time:           # 시작 시간 이전이면 건너뛰기
        continue
    if current_time > end_time:             # 종료 시간 이후이면 종료
        break
    
    filename = f'frame_{frame_num:05d}.png' # 이미지로 저장할 파일 이름 설정
    cv2.imwrite(filename, frame)            # 프레임을 이미지로 저장
    frame_num += 1                          # 다음 프레임 번호 증가
    # cv2.waitKey(int(frame_rate * 0.2))
cap.release()                               # 동영상 파일 닫기

