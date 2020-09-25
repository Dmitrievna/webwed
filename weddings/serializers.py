from django.contrib.auth.models import User, Group
from rest_framework import serializers
from weddings.models import Occupation, Guest, Task, Wedding, Supplier, Table

class OccupationSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    short_title = serializers.CharField(max_length=3)

    def create(self, validated_data):
        """
        Create and return a new Occupation instance, given the validated data.
        """
        return Occupation.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Occupation instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.short_title = validated_data.get('short_title', instance.short_title)
        instance.save()
        return instance


class SupplierSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=200)
    last_name = serializers.CharField(max_length=200)
    contact_email = serializers.EmailField(max_length=200)
    phone_number = serializers.CharField(max_length=200)
    web_site = serializers.CharField(max_length=200)
    description = serializers.TextField()
    occupation = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def create(self, validated_data):
        """
        Create and return a new Supplier instance, given the validated data.
        """
        return Supplier.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing Supplier instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.contact_email = validated_data.get('contact_email', instance.contact_email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.web_site = validated_data.get('web_site', instance.web_site)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        return instance


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=200)
    type = serializers.CharField(max_length=1, choices=['I','U','R'], default='R' )
    status = serializers.CharField(max_length=1, choices=['D','I','N'], default ='N')
    due_to = serializers.DateField()

    def create(self, validated_data):
        """
        Create and return a new Task instance, given the validated data.
        """
        return Task.objects.create(**validated_data)

    def update(self,instance, validated_data):
        """
        Update and return an existent task instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.name)
        instance.type = validated_data.get('type', instance.type)
        instance.status = 


class TableSerializer(models.Model):
    id = serializers.IntegerField(read_only=True)
    title =  models.CharField(max_length=200)
    number = models.IntegerField()
    special_note = models.TextField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class GuestSerializer(models.Model):
    """Model for representing an instance of a guest"""

    BELONGS_TO = (
    ('H','Husband'),
    ('W','Wife'),
    )

    STATUSES = (
    ('Y','Yes'),
    ('N','No'),
    ('M','Maybe'),
    )

    id = serializers.IntegerField(read_only=True)
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    table = models.ForeignKey(Table,on_delete=models.SET_NULL, null=True)
    whose = models.CharField(max_length=1, choices=BELONGS_TO)
    status = models.CharField(max_length=1, choices=STATUSES)

    def __str__(self):
            """String for representing the Model object."""
            return f'{self.last_name}, {self.name}'




class WeddingSerializer(models.Model):
    """Model representing an instance of the wedding"""

    husband = models.CharField(max_length=200)
    wife = models.CharField(max_length=200)
    tasks = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    special_date = models.DateField(null=True, blank=True)
    guests = models.ForeignKey(Guest, on_delete=models.SET_NULL, null=True)
    suppliers = models.ManyToManyField(Supplier)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.wife}, {self.husband}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this wedding."""
        return reverse('wedding-detail', args=[str(self.id)])
