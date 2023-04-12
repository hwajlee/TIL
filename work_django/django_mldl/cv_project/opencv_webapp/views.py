from django.shortcuts import render, redirect
<<<<<<< Updated upstream
from .forms import SimpleUploadForm # from opencv_webapp.forms import SimpleUploadForm -> SimpleUploadForm라는 class를 import해라
from django.core.files.storage import FileSystemStorage
=======
from .forms import SimpleUploadForm, ImageUploadForm # from opencv_webapp.forms import SimpleUploadForm -> SimpleUploadForm라는 class를 import해라
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from .cv_functions import cv_detect_face
>>>>>>> Stashed changes

# Create your views here.
def first_view(request):
    # <input type='text' name='passenger_id' class='~~' id='~~'>
    # -> request.POST['passenger_id'] => 위의 input tag에 유저가 입력한 값 꺼낼 수 있음
<<<<<<< Updated upstream
    return render(render, 'opencv_webapp/first_view.html', {})
=======
    return render(request, 'opencv_webapp/first_view.html', {})
>>>>>>> Stashed changes


def simple_upload(request):

    if request.method == 'POST':
        # print(request.POST) : <QueryDict: {'csrfmiddlewaretoken': [‘~~~’], 'title': ['upload_1']}>
        # print(request.FILES) : <MultiValueDict: {'image': [<InMemoryUploadedFile: ses.jpg (image/jpeg)>]}>
        # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.
        form = SimpleUploadForm(request.POST, request.FILES)

        if form.is_valid():
            myfile = request.FILES['image'] # 메모리에 한시적으로 저장되어있는 파일 객체
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            # myfile.name : 'ses.jpg' (사용자가 업로드한 파일 원본의 이름)
            # filename : 'ses_UPArih4.jpg' (서버에 업로드가 끝난 파일의 이름, 중복될 시 자동으로 변경됨)
            # 서버에 업로드가 끝난 이미지 파일의 URL을 얻어내 Template에게 전달

            uploaded_file_url = fs.url(filename) # '/media/ses.jpg'

            print('\n\n\n')
            print("myfile.name :", myfile.name)
            print("filename :", filename)
            print("uploaded_file_url :", uploaded_file_url)
            print('\n\n\n')

            context = {'form': form, 'uploaded_file_url': uploaded_file_url} # filled form
            return render(request, 'opencv_webapp/simple_upload.html', context)

    else: # request.method == 'GET' (DjangoBasic 실습과 유사한 방식입니다.)

        print('\n\n\n')
        print(request.method) # -> 요청이 들어왔을 때 cmd창에 post인지 get인지 보여줌
        print('\n\n\n')

        form = SimpleUploadForm()
        context = {'form': form} # empty form
        return render(request, 'opencv_webapp/simple_upload.html', context)
<<<<<<< Updated upstream
=======


def detect_face(request):

    # request.method == 'GET' 일 경우
    # 빈 양식 만들기
    form = ImageUploadForm()
    # 내보내기(detect_face.html file)
    return render(request, 'opencv_webapp/detect_face.html', {'form' : form})


def detect_face(request):

    if request.method == 'POST' :

        # 비어있는 Form에 사용자가 업로드한 데이터를 넣고 검증합니다.
        form = ImageUploadForm(request.POST, request.FILES) # filled form

        if form.is_valid():

            post = form.save(commit=False)
            # save() 함수는 DB에 저장될 ImageUploadModel 클래스 객체 자체를 리턴함 (== record 1건)
            # Form에 채워진 데이터를 DB에 실제로 저장하기 전에 변경/추가할 수 있음 (commit=False)
            # ex) post.description = papago.translate(post.description)
            post.save() # Form 객체('form')에 채워져 있는 데이터를 DB에 실제로 저장

            # settings.MEDIA_URL == '/media/'
	        # document : ImageUploadModel Class에 선언되어 있는 “document”에 해당
            imageURL = settings.MEDIA_URL + form.instance.document.name
            # == form.instance.document.url
            # == post.document.url
            # == '/media/images/2021/10/29/ses_XQAftn4.jpg'
            # print(form.instance, form.instance.document.name, form.instance.document.url)
            # cv_detect_face(settings.MEDIA_ROOT_URL + imageURL) # 추후 구현 예정
            print('\n\n\n')
            print('form.instance :',                form.instance)
            print('form.instance.document :',       form.instance.document)
            print('form.instance.document.name :',  form.instance.document.name)
            print('form.instance.document.url :',   form.instance.document.url)
            print('post.document.url :',            post.document.url)
            print('\n\n\n')

            # cv_detect_face('./media/images/2023/04/11/ses_98L2d66.jpg')
            cv_detect_face(settings.MEDIA_ROOT_URL + imageURL)

            return render(request, 'opencv_webapp/detect_face.html', {'form':form, 'post':post})

    else: # request.method == 'GET'
         form = ImageUploadForm() # empty form
         return render(request, 'opencv_webapp/detect_face.html', {'form':form})
>>>>>>> Stashed changes
