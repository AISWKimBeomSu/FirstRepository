"""
!pip install -r requirements.txt
"""

import pytesseract
import cv2
import os
from PIL import Image

# Image
image = cv2.imread('img1.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Read file in os
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# lang : Language to use
text = pytesseract.image_to_string(Image.open(filename), lang=None)
os.remove(filename)

# Show result
print(text)


# cv2.imshow('image', image)

# 함수
# 1. 숫자, 기호 판별 ? .. 그냥 수식 이미지만 넣을 것인가
# 2. 계산
# 3. 결과

def split_calculation(result):
    """
    :param result: OCR의 결과
    :return: [list] OCR의 결과 식들을 리스트로 반환
    """
    calculations = result.split('\n')

    # 마지막 값이 null 이면 drop
    if calculations[-1] == '':
        calculations.pop()

    return calculations

# 숫자 분리, 계산 출력
a = split_calculation(text)

print('결과')

x = a[0].split('+')
y = a[1].split('+')
z = a[2].split('+')
sum = 0
for i in x:
    sum += int(i)
print(sum)
sum = 0
for i in y:
    sum += int(i)
print(sum)
sum = 0
for i in z:
    sum += int(i)
print(sum)