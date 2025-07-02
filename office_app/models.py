from django.db import models

# Optional: Top-level company model
class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# class Department(models.Model):
#     name = models.CharField(max_length=100)

# class ChickenBatch(models.Model):
#     department = models.ForeignKey(Department, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField()
#     added_on = models.DateTimeField(auto_now_add=True)


class Department(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


# Agriculture Section
class ChickenBatch(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    number = models.PositiveIntegerField()
    age_in_weeks = models.PositiveIntegerField()
    purpose = models.CharField(max_length=50, choices=[('meat', 'Meat'), ('eggs', 'Eggs')])

    def __str__(self):
        return f"{self.number} chickens for {self.purpose}"


class FishPond(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    pond_name = models.CharField(max_length=100)
    fish_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.pond_name


class PigPen(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    number_of_pigs = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.number_of_pigs} pigs"


# Construction Projects
class ConstructionProject(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    budget = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# Transportation Section
class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = [
        ('taxi', 'Taxi'),
        ('lorry', 'Lorry')
    ]
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    vehicle_type = models.CharField(max_length=10, choices=VEHICLE_TYPE_CHOICES)
    plate_number = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.vehicle_type.upper()} - {self.plate_number}"


class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    purpose = models.TextField()
    trip_date = models.DateField()

    def __str__(self):
        return f"{self.vehicle} to {self.destination}"
