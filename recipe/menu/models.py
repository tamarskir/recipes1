from django.urls import reverse
from django.db import models



    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_ur1(self):
        return reverse('category', args = [str(self.id)])

     
    def get_recipes(self):
        return self.recipe.all()
  

class Recipe(models.Model):
    category = models.ForeignKey(Category,  on_delete=models.CASCADE, null = True)
    name = models.CharField(max_length=100)
    ingridient1 = models.CharField(max_length=100,null = True)
    col1 = models.CharField(max_length=100,  null=True)
    ingridient2 = models.CharField(max_length=100, null = True)
    col2 = models.CharField(max_length=100, null = True)
    ingridient3 = models.CharField(max_length=100, null = True, blank=True)
    col3 = models.CharField(max_length=100, null = True,  blank=True)
    ingridient4 = models.CharField(max_length=100, null = True, blank=True)
    col4 = models.CharField(max_length=100, null = True, blank=True)
    ingridient5 = models.CharField(max_length=100,null = True,blank=True)
    col5 = models.CharField(max_length=100, null = True, blank=True)    
    description = models.TextField(help_text="Enter short description")  
    picture = models.ImageField(blank=True, upload_to='picture/%y/%m/%d/')

    class Meta:
        ordering = ('category',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('recipe', args = [str(self.id)])

    
    

    

    def picture_url(self):
        if self.picture:
            return self.picture.url
        else:
            self.picture_url="https://bipbap.ru/wp-content/uploads/2020/11/46780003-watercolor-cosmetics-and-perfumes-collection-vector-illustration.jpg"
            return self.picture_url


class Messages(models.Model):
    recipe = models.ForeignKey(Recipe,  on_delete=models.CASCADE, null = True)
    date = models.DateField(auto_now_add=True)
    name = models.CharField(max_length=100, null = True, blank=True)
    messages = models.TextField()
 
