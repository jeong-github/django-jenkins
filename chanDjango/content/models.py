from django.db import models

class Post(models.Model):
    content = models.TextField()  # The content of the post
    created_at = models.DateTimeField(auto_now_add=True)  # The timestamp for when the post is created

    def __str__(self):
        return self.content[:50]  # Display the first 50 characters of the content

    class Meta:
        db_table = 'post'  # Specify the exact name of the table in PostgreSQL
        app_label = 'content'

class Feed(models.Model):
    content       = models.TextField()        # 글 내용
    image         = models.TextField()        # 이미지 URL 또는 경로
    profile_image = models.TextField()        # 작성자 프로필 이미지 URL
    user_id       = models.TextField()        # 작성자 ID
    like_count    = models.IntegerField()     # 좋아요 수

    def __str__(self):
        return f"{self.user_id}: {self.content[:30]}"

    class Meta:
        db_table = 'feed'  # PostgreSQL에서 사용할 테이블 이름






#from django.db import models
#class Post(models.Model):
#    content = models.TextField()  # The content of the post
#    created_at = models.DateTimeField(auto_now_add=True)  # The timestamp for when the post is created
#
#    def __str__(self):
#        return self.content[:50]  # Display the first 50 characters of the content
#
#    class Meta:
#        db_table = 'post'  # Specify the exact name of the table in PostgreSQL
#        app_label = 'content'
