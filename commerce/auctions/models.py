from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Category(models.Model):
    category_name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
class Bid(models.Model):
    bid = models.IntegerField
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_bid")
    
    

class Listings(models.Model):
    title = models.CharField(max_length = 30)
    description = models.CharField(max_length = 300)
    image_url = models.CharField(max_length = 1000)
    price = models.ForeignKey(Bid, on_delete=models.CASCADE, blank=True, null=True, related_name="bid_price")
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, related_name="category")
    watch_list = models.ManyToManyField(User, blank=True, null=True, related_name="listing_watch_list")
    
    def __str__(self):
        return self.title
    
class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True, related_name="user_comment")
    listing = models.ForeignKey(Listings, on_delete=models.CASCADE, blank=True, null=True, related_name="listing_comment")
    message = models.CharField(max_length=200)
    
    def __str__(self):
        return f"{self.author} comment on {self.listing}"
    

