from django.db import models
import uuid

# Create your models here.

class BookingUser(models.Model):
    # id = models.UUIDField(primarykey = True, editable = False, default = uuid.uuid4)
    name = models.CharField(max_length = 100, blank = False, default = "")
    date = models.CharField(max_length = 40, blank = False, default = "")
    gender = models.CharField(max_length = 10, blank = False, default = "")
    email = models.EmailField(blank = False)
    # peoples = models.TextField(blank = False)
    whats_app_num = models.CharField(max_length = 12)
    pick_up_point = models.TextField(blank = False)
    time_stamp = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.email
    

class Feedback(models.Model):
    # id = models.UUIDField(primarykey = True, editable = False, default = uuid.uuid4)
    name = models.CharField(max_length = 100, blank = False)
    phone = models.CharField(max_length = 10, blank = False)
    message = models.CharField(max_length = 300, blank = False)



# # A model for Creating Destination
    
# class Destinations(models.Model):
#     id = models.UUIDField(primarykey = True, editable = False, default = uuid.uuid4)
#     name = models.CharField(max_length = 100, blank = False)
#     date = models.DateField(blank = False)
    

#     def __str__(self):
#         return self.name
    

# # A Model for Creating Customised Tourist Place
    
# class Customised(models.Model):
#     id = models.UUIDField(primarykey = True, editable = False, default = uuid.uuid4)
#     name = models.CharField(max_length = 100, blank = False)
#     date = models.DateField(blank = False)
#     number_people = models.TextField(blank = False)
#     peoples = models.TextField(blank = False)
#     phone_number = models.CharField(blank = False)


#     def __str__(self):
#         return self.name
    
