from django_filters import rest_framework as filters
from rest_framework import response, status
from rest_framework.views import APIView

from .models import DialyModel
from .serializers import DialySerializer


class DialyListFilter(filters.FilterSet):
    title = filters.filters.CharFilter(lookup_expr='icontains')
    content = filters.filters.CharFilter(lookup_expr='icontains')
    isDeleted = filters.filters.BooleanFilter(lookup_expr=False)

    class Meta:
        model = DialyModel
        fields = '__all__'


class DialyViewSet(APIView):
    queryset = DialyModel.objects.all()
    serializer_class = DialySerializer
    filter_class = DialyListFilter

    def get(self, request):
        requestParams = request.query_params
        # params = {
        #     'isDeleted': requestParams.get('isDeleted')
        # }
        # TODO: 検索機能
        qs = DialyModel.objects.filter(isDeleted=False)
        # filterset = DialyListFilter(
        #     params, queryset=qs)
        serializer = DialySerializer(instance=qs, many=True)
        data = {
            "status": status.HTTP_200_OK,
            "message": "",
            "result": serializer.data,
        }
        return response.Response(data, status=status.HTTP_200_OK)

    def put(self, request):
        # idの有無によって新規・更新を分ける
        param = request.data
        if param['id'] == '' or param['id'] == None:
            # if True:
            # 新規作成
            serializer = DialySerializer(data=param)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Exception as e:
                print(e)
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            data = {
                "status": status.HTTP_200_OK,
                "message": "",
                "result": serializer.data,
            }
            return response.Response(data, status=status.HTTP_200_OK)
        else:
            # 更新
            try:
                todo = DialyModel.objects.get(pk=param.get('id'))
            except Exception as e:
                print(e)
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                # partial = true?
            serializer = DialySerializer(instance=todo, data=param)
            try:
                serializer.is_valid(raise_exception=True)
                serializer.save()
            except Exception as e:
                print(e)
                return response.Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            data = {
                "status": status.HTTP_200_OK,
                "message": "",
                "result": serializer.data,
            }
        return response.Response(data, status=status.HTTP_200_OK)
