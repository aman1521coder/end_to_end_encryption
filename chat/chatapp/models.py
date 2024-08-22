from django.db import models

class Users(models.Model):
	userId=pass
	Name=pass
	password=pass
	Gmail=pass
	follower_ID
	following_ID
	public_key
	last_online
	joined_data
	Update_at
    Avatar_url
class Chat:
	chat_Id
	chat_content
	chat_Time_stamp
	chat_Pic_Url
	Chat_Recive_ID
	chat_Send_id
	chat_status
class Random_chat:
	Random_chat_ID
	User_ID
	Chat_User_ID
	Start_Time
	End_Time
class Freinds:
	user_Id
	frends_ID
	friend_Status
	friend_user_ID

