import cv2
import os
def changeImg(videoPath):
  # 비디오 파일 경로
  video_path = videoPath
  # 프레임이 저장될 폴더 경로
  output_folder = 'frames'

  # 저장 폴더가 없으면 생성
  os.makedirs(output_folder, exist_ok=True)

  # 비디오 캡처 객체 생성
  cap = cv2.VideoCapture(video_path)

  frame_count = 0
  while True:
    # 프레임 읽기
    ret, frame = cap.read()

    # 더 이상 프레임이 없으면 종료
    if not ret:
        break

    # 프레임 저장 (예: frame_00001.png)
    frame_filename = os.path.join(output_folder, f'frame_{frame_count:05d}.png')
    cv2.imwrite(frame_filename, frame)
    
    frame_count += 1

  # 비디오 캡처 객체 해제
  cap.release()
  print(f'{frame_count} 프레임이 {output_folder} 폴더에 저장되었습니다.')
