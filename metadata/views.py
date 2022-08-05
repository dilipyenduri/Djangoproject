from xml.etree.ElementPath import xpath_tokenizer
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_200_OK
from .serializers import LocationSerializer, LocationUpdateSerializer
from datetime import datetime

# Create your views here.


class LocationData(APIView):
    """
    Get all location data
    """
    def get(self,request):
        try:
            location_list = []
            location_obj = Location.objects.all()
            for each in location_obj:
                location_dict = {}
                location_dict['name'] = each.name
                location_dict['created_on'] = each.created_on
                location_dict['updated_on'] = each.updated_on
                location_list.append(location_dict)
            output = "Successfully Fetched"
            return Response({'status_code': HTTP_200_OK,
                                'status': 'success', "data": location_list, "message": output})
        except Exception as e:
            print(e)
            output = "Bad Request"
            return Response({'status_code': HTTP_400_BAD_REQUEST,
                                'status': 'failure', "message": output})
    
    def post(self,request):
        try:
            serializer = LocationSerializer(data=request.data)
            if serializer.is_valid():
                date_value = datetime.now()
                Location.objects.create(name = request.data['name'],created_on = date_value, updated_on = date_value )
                result = "succesfully created"
                context_data = {"success" : True, "data" :{"result" : result}}
            else:
                context_data = {"success" : False, "errors" : {"message": "Validation Error" ,  "errors_list" : serializer.errors}}

            output = "Successfully Fetched"
            return Response({'status_code': HTTP_200_OK,
                                'status': 'success', "data": context_data, "message": output})
        except Exception as e:
            print(e)
            output = "Bad Request"
            return Response({'status_code': HTTP_400_BAD_REQUEST,
                                'status': 'failure', "message": output})
    
    def put(self,request):
        try:
            serializer = LocationUpdateSerializer(data=request.data)
            if serializer.is_valid():
                date_value = datetime.now()
                try:
                    loc_obj = Location.objects.get(name = request.data['old_name'])
                    loc_obj.name = request.data['new_name']
                    loc_obj.save()
                except Location.DoesNotExist as e:
                    print(e)
                    return {"success" : False,"errors":"Location doesn't exist"}

                result = "succesfully updated"
                context_data = {"success" : True, "data" :{"result" : result}}
            else:
                context_data = {"success" : False, "errors" : {"message": "Validation Error" ,  "errors_list" : serializer.errors}}

            output = "Successfully Fetched"
            return Response({'status_code': HTTP_200_OK,
                                'status': 'success', "data": context_data, "message": output})
        except Exception as e:
            print(e)
            output = "Bad Request"
            return Response({'status_code': HTTP_400_BAD_REQUEST,
                                'status': 'failure', "message": output})
                                

    def delete(self,request,location_delete_id=None):
        try:
            try:
                location_obj = Location.objects.get(id = location_delete_id)
            except Location.DoesNotExist as e:
                print(e)
                return Response({"success" : False,"errors":"Location doesn't exist"} )
            Department.objects.filter(location=location_obj).delete()
            Category.objects.filter(location=location_obj).delete()
            SubCategory.objects.filter(location=location_obj).delete()
            location_obj.delete()  
            output = "Deleted Succesfully"
            return Response({'status_code': HTTP_200_OK,
                                'status': 'success', "message": output})
        except Exception as e:
            print(e)
            output = "Bad Request"
            return Response({'status_code': HTTP_400_BAD_REQUEST,
                                'status': 'failure', "message": output})


class DepartmentData(APIView):
    """
    Get department data based on location id
    """

    def get(self,request,location_id=None):
        try:
            department_list=[]
            location_obj = Location.objects.get(id=location_id)
            department_obj = Department.objects.filter(location = location_obj)
            for each_dept in department_obj:
                department_dict = {}
                department_dict['name'] = each_dept.name
                department_dict['created_on'] = each_dept.created_on
                department_dict['updated_on'] = each_dept.updated_on
                department_list.append(department_dict)
            output = "Successfully Fetched"
            return Response({'status_code': HTTP_200_OK,
                                'status': 'success', "data": department_list, "message": output})
        except Exception as e:
            print(e)
            output = "Bad Request"
            return Response({'status_code': HTTP_400_BAD_REQUEST,
                                'status': 'failure', "message": output})


class CategoryData(APIView):
    """
    Get category data based on location id and department id
    """

    def get(self,request,location_id=None,department_id=None):
        try:
            category_list=[]
            location_obj = Location.objects.get(id=location_id)
            department_obj = Department.objects.get(id=department_id)
            catergory_obj = Category.objects.filter(location=location_obj,department=department_obj)
            for each_cat in catergory_obj:
                cat_dict = {}
                cat_dict['name'] = each_cat.name
                cat_dict['created_on'] = each_cat.created_on
                cat_dict['updated_on'] = each_cat.updated_on
                category_list.append(cat_dict)
            output = "Successfully Fetched"
            return Response({'status_code': HTTP_200_OK,
                                'status': 'success', "data": category_list, "message": output})
        except Exception as e:
            print(e)
            output = "Bad Request"
            return Response({'status_code': HTTP_400_BAD_REQUEST,
                                'status': 'failure', "message": output})


class SubCategoryData(APIView):
    """
    Get subcategory data based on location id and department id and category id
    """

    def get(self,request,location_id=None,department_id=None,category_id=None):
        try:
            subcategory_list=[]
            location_obj = Location.objects.get(id=location_id)
            department_obj = Department.objects.get(id=department_id)
            catergory_obj = Category.objects.get(id=category_id)
            subcatergory_obj = SubCategory.objects.filter(location=location_obj,department=department_obj,category=catergory_obj)
            for each_subcat in subcatergory_obj:
                subcat_dict = {}
                subcat_dict['name'] = each_subcat.name
                subcat_dict['created_on'] = each_subcat.created_on
                subcat_dict['updated_on'] = each_subcat.updated_on
                subcategory_list.append(subcat_dict)
            output = "Successfully Fetched"
            return Response({'status_code': HTTP_200_OK,
                                'status': 'success', "data": subcategory_list, "message": output})
        except Exception as e:
            print(e)
            output = "Bad Request"
            return Response({'status_code': HTTP_400_BAD_REQUEST,
                                'status': 'failure', "message": output})

