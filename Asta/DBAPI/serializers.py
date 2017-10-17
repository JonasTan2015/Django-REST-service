from rest_framework import serializers
from .models import CreditCard, AlchemyCreditCard
from .crud import AlchemyCRUDMixin


class CreditCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreditCard
        fields = ('ID', 'name', 'deposit', 'date')
        read_only_fields = ('date',)


from DBAPI import Session


class AlchemyCreditCardSerializer(serializers.Serializer, AlchemyCRUDMixin):
    ID = serializers.CharField(max_length=80, allow_null=False)
    name = serializers.CharField(max_length=50)
    deposit = serializers.IntegerField(default=0)
    date = serializers.ReadOnlyField()


    def save(self):
        alchemyCreditCard = AlchemyCreditCard(
            ID = self.validated_data['ID'],
            name=self.validated_data['name'],
            deposit=self.validated_data['deposit']
        )
        self.__create__(alchemyCreditCard)
