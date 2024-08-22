from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    public_key = models.TextField()
    last_online = models.DateTimeField(null=True, blank=True)
    joined_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    avatar_url = models.URLField(null=True, blank=True)

    def __str__(self):
        return self.name

class Friend(models.Model):
    user = models.ForeignKey(User, related_name='friends', on_delete=models.CASCADE)
    friend_user = models.ForeignKey(User, related_name='friend_of', on_delete=models.CASCADE)
    friend_status = models.CharField(max_length=50, default="pending")

    class Meta:
        unique_together = ('user', 'friend_user')  # Ensures that the same pair cannot be friends twice

    def __str__(self):
        return f"{self.user} is friends with {self.friend_user}"

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    sender = models.ForeignKey(User, related_name='chats_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='chats_received', on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    pic_url = models.URLField(null=True, blank=True)
    status = models.CharField(max_length=50, default="sent")

    def __str__(self):
        return f"Chat from {self.sender} to {self.receiver} at {self.timestamp}"

class RandomChat(models.Model):
    random_chat_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, related_name='random_chats_started', on_delete=models.CASCADE)
    chat_user = models.ForeignKey(User, related_name='random_chats_received', on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Random chat between {self.user} and {self.chat_user}"
