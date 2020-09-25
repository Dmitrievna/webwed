from django.db import models

# Create your models here.
class Occupation(models.Model):
    """Model for representing an instance of occupation for the suppliers"""

    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=3)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Location(models.Model):
    """Model for representing an instance of location for suppliers and a wedding"""

    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Category(models.Model):
    """Model for representing an instance of location for suppliers and a wedding"""

    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=3)

    def __str__(self):
        """String for representing the Model object."""
        return self.short_title


class Supplier(models.Model):
    """Model representing an instance of a supplier"""

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200)
    web_site = models.CharField(max_length=200)
    description = models.TextField()
    occupation = models.ForeignKey(Occupation, on_delete=models.SET_NULL, null=True)
    location = models.ForeignKey(Location, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.last_name}, {self.name}'

    def get_absolute_url(self):
        """Returns the url to access a detail record for this wedding."""
        return reverse('supplier-detail', args=[str(self.id)])

class Task(models.Model):
    """Model representing an instance of the task"""

    TYPES = (
    ('I', 'Important'),
    ('U', 'Urgent'),
    ('R', 'Rest'),
    )

    STATUSES = (
    ('D', 'Done'),
    ('I', 'In Progress'),
    ('N', 'Not Started'),
    )

    title = models.CharField(max_length=200)
    type = models.CharField(max_length=1, choices=TYPES, default='R' )
    status = models.CharField(max_length=1, choices=STATUSES, default ='N')
    due_to = models.DateField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Table(models.Model):
    """Model for the table representation"""

    title =  models.CharField(max_length=200)
    number = models.IntegerField()
    special_note = models.TextField()

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Guest(models.Model):
    """Model for representing an instance of a guest"""

    BELONGS_TO = (
    ('G','Groom'),
    ('B','Bride'),
    )

    STATUSES = (
    ('Y','Yes'),
    ('N','No'),
    ('M','Maybe'),
    ('U','Unknown')
    )

    ALLERGIES = (
    ('Lac', 'Lactose'),
    ('Egg', 'Eggs'),
    ('Soy', 'Soya'),
    ('Nut', 'Nuts and Seeds'),
    ('Glu', 'Gluten'),
    ('Fis', 'Fish'),
    ('Veg', 'Vegetables'),
    ('Fru', 'Fruits'),
    ('Mea', 'Meat'),
    ('Non', 'None'),
    )

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    table = models.ForeignKey(Table,on_delete=models.SET_NULL, null=True)
    whose = models.CharField(max_length=1, choices=BELONGS_TO, default = 'B')
    status = models.CharField(max_length=1, choices=STATUSES, default = 'U')
    hotel_date = models.DateField(null=True)
    children = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)
    age = models.IntegerField(null=True)
    allergy = models.CharField(max_length=3, choices=ALLERGIES, default='Non')
    comment = models.TextField(default='No comments')

    def __str__(self):
            """String for representing the Model object."""
            return f'{self.last_name}, {self.name}'

class Budget(models.Model):
    """Model represeting an instance of the budget entity"""

    item_title = models.CharField(max_length=200)
    expected_payment = models.IntegerField()
    resulted_payment = models.IntegerField()
    amount_paid = models.IntegerField()
    amount_to_go = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    supplier_in_connect = models.ForeignKey(Supplier, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.item_title}, {self.category}'



class Wedding(models.Model):
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
