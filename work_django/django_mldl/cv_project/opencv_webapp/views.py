from django.shortcuts import render, redirect
from .forms import SimpleUploadForm # from opencv_webapp.forms import SimpleUploadForm -> SimpleUploadForm라는 class를 import해라
from django.core.files.storage import FileSystemStorage

# Create your views here.
def first_view(request):
    # <input type='text' name='passenger_id' class='~~' id='~~'>
    # -> request.POST['passenger_id'] => 위의 input tag에 유저가 입력한 값 꺼낼 수 있음
    return render(render, 'opencv_webapp/first_view.html', {})


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
