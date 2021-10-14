from rest_framework import serializers
from .models import Principal,Dependants


class PrincipalSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Principal
        fields= ('first_name', 'last_name', 'member_type','member_number')

class DependantsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model= Dependants
        fields= ('first_name', 'last_name', 'member_type','principal_no')