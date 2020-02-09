from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView
from myapp.serializers import QuestionSerializer, ChoiceSerializer
from myapp.models import Question, Choice


class QuestionAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Question.objects.get(pk=id)
            serializer = QuestionSerializer(item)
            return Response(serializer.data)
        except Question.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Question.objects.get(pk=id)
        except Question.DoesNotExist:
            return Response(status=404)
        serializer = QuestionSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Question.objects.get(pk=id)
        except Question.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class QuestionAPIListView(APIView):

    def get(self, request, format=None):
        items = Question.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = QuestionSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class ChoiceAPIView(APIView):

    def get(self, request, id, format=None):
        try:
            item = Choice.objects.get(pk=id)
            serializer = ChoiceSerializer(item)
            return Response(serializer.data)
        except Choice.DoesNotExist:
            return Response(status=404)

    def put(self, request, id, format=None):
        try:
            item = Choice.objects.get(pk=id)
        except Choice.DoesNotExist:
            return Response(status=404)
        serializer = ChoiceSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, id, format=None):
        try:
            item = Choice.objects.get(pk=id)
        except Choice.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ChoiceAPIListView(APIView):

    def get(self, request, format=None):
        items = Choice.objects.order_by('pk')
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(items, request)
        serializer = ChoiceSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    def post(self, request, format=None):
        serializer = ChoiceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
