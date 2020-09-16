from django.db import models

# Create your models here.
class Occupation(models.Model):
    """Model for representing an instance of occupation for the suppliers"""

    title = models.CharField(max_length=200)
    short_title = models.CharField(max_length=3)

    def __str__(self):
        """String for representing the Model object."""
        return self.title

class Supplier(models.Model):
    """Model representing an instance of a supplier"""

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    phone_number = models.CharField(max_length=200)
    web_site = models.CharField(max_length=200)
    description = models.TextField()
    occupation = models.ForeignKey(Occupation, on_delete=models.SET_NULL, null=True)

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
    ('H','Husband'),
    ('W','Wife'),
    )

    STATUSES = (
    ('Y','Yes'),
    ('N','No'),
    ('M','Maybe'),
    )

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    contact_email = models.EmailField(max_length=200)
    table = models.ForeignKey(Table,on_delete=models.SET_NULL, null=True)
    whose = models.CharField(max_length=1, choices=BELONGS_TO)
    status = models.CharField(max_length=1, choices=STATUSES)

    def __str__(self):
            """String for representing the Model object."""
            return f'{self.last_name}, {self.name}'




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
