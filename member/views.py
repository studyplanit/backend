from random import randint
import requests
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .serializers import MemberSerializer
from .models import Member
from rest_framework.parsers import JSONParser


@csrf_exempt
def members(request):
    data = JSONParser().parse(request)

    # 신규 회원 등록
    if request.method == 'POST':
        serializer = MemberSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

    # 사용자 전체 정보 조회
    elif request.method == 'GET':
        members = Member.objects.all()
        serializer = MemberSerializer(members, many=True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def member(request, phone):
    data = Member.objects.get(pk=phone)  # 폰번호가 같은 데이터 하나만 찾기

    # 사용자 정보 조회
    if request.method == 'GET':
        serializer = MemberSerializer(data)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def checkNick(request, nick):

    # 사용자 정보 조회
    if request.method == 'GET':
        data = Member.objects.filter(nick=nick)
        if len(data) != 0:
            is_member = 1
        else:
            is_member = 0

        return JsonResponse({'isMember': is_member})


@csrf_exempt
def smsAuth(request,phone):
    auth_number=randint(1000, 10000)

    #사용자의 폰으로 인증번호 전송
    if request.method == 'GET':
        def send_sms(auth_number):
            url = 'https://api-sens.ncloud.com/v1/sms/services/ncp:sms:kr:260831440301:split/messages/'
            data = {
                "type": "SMS",
                "from": "01046262087",
                "to": [phone],
                "content": "[스플릿] 인증 번호 [{}]를 입력해주세요.".format(auth_number)
            }
            headers = {
                "Content-Type": "application/json",
                "x-ncp-auth-key": "ofkcwdhgnIxoyxBDT1Km",
                "x-ncp-service-secret": "926151691d4e4d209810ce27edacfef0",
            }
            requests.post(url, json=data, headers=headers)

        send_sms(auth_number)

        #사용자의 폰번호가 회원으로 등록이 되어있는지 확인
        data = Member.objects.filter(phone=phone)
        if len(data)!=0:
            is_member=1
        else:
            is_member=0

        return JsonResponse({'authNumber': auth_number,'isMember': is_member})


















