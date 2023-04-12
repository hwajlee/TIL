from django.db import models

# Create your models here.
class ImageUploadModel(models.Model):

    # blank=True : Form에서 빈 채로 저장되는 것을 허용 (views.py에서 활용한 .is_valid() 함수가 검증 진행 시)
    description = models.CharField(max_length=255, blank=True)

    # upload_to : 저장될 파일의 경로를 지정 (ex. ‘images/2020/02/21/test_image.jpg’)
    document = models.ImageField(upload_to='images/%Y/%m/%d')

    # auto_now_add : 자동으로 저장되는 시점을 기준으로 현재 시간을 세팅
    uploaded_at = models.DateTimeField(auto_now_add=True)

<<<<<<< Updated upstream
=======
# Model form을 쓰지 않고 한땀한땀 꺼내쓸 경우
# ------------------------------------------------
# @ ~~~.html
# ------------------------------------------------
# <input type='text' name='input_description' placeholder='이미지의 설명을 입력해주세요' required>
# <input type='file' name='input_image' required>
# ------------------------------------------------
# ------------------------------------------------
# @ views.py
# ------------------------------------------------
# from .models import ImageUploadModel
# def user_upload(request):
#     new_record = ImageUploadModel()
#     new_record.description = request.POST['input_description']
#     new_record.document = request.FILES['input_image']
#     new_record.save()
# ------------------------------------------------


>>>>>>> Stashed changes
# row_sample = ImageUploadModel()
# print(row_sample.uploaded_at) # 해당 데이터 건의 업로드 날짜 문자열
# row_sample.description = "설명 덮어쓰기 입니다."
# print(row_sample.description) # "설명 덮어쓰기 입니다."
