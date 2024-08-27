from django.db import models

class TagLine(models.Model):
    caption = models.CharField(max_length=255)

    def __str__(self):
        return self.caption


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# still not migrte
# should i do now mam
# already done 
# but made some error in the models
# for that i create new db mam


class Post(models.Model):
    title = models.CharField(max_length=200)
    image_name = models.FileField( upload_to='images/', max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(TagLine)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=100)
    user_email = models.EmailField()
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"Comment by {self.user_name} on {self.post}"
