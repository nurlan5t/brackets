from rest_framework.decorators import api_view
from rest_framework.response import Response
from bracketsapp.models import Journal
from bracketsapp.serializers import JournalsListSerializer
from datetime import datetime


def check_brackets(string_received):
    open_brackets = '([{'
    close_brackets = ')]}'
    string_shorted = [i for i in string_received if i in (open_brackets + close_brackets)]
    sequence = []
    for i in string_shorted:
        if i in open_brackets:
            sequence.append(i)
        elif i in close_brackets:
            pos = close_brackets.index(i)
            if sequence and (open_brackets[pos] == sequence[-1]):
                sequence.pop()
            else:
                return False
    return True if len(sequence) == 0 else False


def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


# Create your views here.
@api_view(['GET', 'POST'])
def check(request):
    if request.method == 'GET':
        all_posts = Journal.objects.all()
        serializer = JournalsListSerializer(all_posts, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        data = dict(
            input_data=tuple(request.data.keys())[0],
            source_ip=get_ip_address(request),
            posted_at=datetime.now()
        )
        data['checking_results'] = check_brackets(data['input_data'])
        serializer = JournalsListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
