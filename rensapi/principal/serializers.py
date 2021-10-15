from rest_framework import serializers
from .models import Principal,Dependants

class DependantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Dependants
        fields= ('first_name', 'last_name', 'member_type','principal_no')
class PrincipalSerializer(serializers.HyperlinkedModelSerializer):
    
    dependants=serializers.StringRelatedField(many=True)
    class Meta:
        model= Principal
        fields= ('first_name', 'last_name', 'member_type','member_number','dependants')

