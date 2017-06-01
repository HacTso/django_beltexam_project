from __future__ import unicode_literals
from django.db import models
import datetime
import bcrypt
import re
NAME_REGEX =re.compile('^[A-z]+$')
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def register(self, postData):
    	errors = []
    	#check if email exists
    	if User.objects.filter(email=postData['email']):
    		errors.append('*Email is already registered')
    	# validate username
    	if len(postData['username']) < 2:
    		errors.append('*Username must be at least 2 characters')
    	elif not NAME_REGEX.match(postData['username']):
    		errors.append('*Username must only contain alphabet')
    	# validate email
    	if len(postData['email']) < 1:
    		errors.append('*Email cannot be blank')
    	elif not EMAIL_REGEX.match(postData['email']):
    		errros.append('*Invaild email format')
    	# validate password
    	if len(postData['password']) < 8:
    		errors.append('*Password should be at least 8 characters')
    	# validate confirm passowrd
    	elif postData['password'] != postData['confirm']:
    		errors.append('*Password do not match')
    	return(False, errors)
    	
    	# if no errors
    	# if len(errors) == 0:
    	# 	# hash pw with password(encode) and (gen)salt
    	# 	reg_pw = bcrypt.hashpw(postData['password'].encode('utf-8'), bcrypt.gensalt())
    	# 	# add to database
    	# 	userinfo = User.objects.create(email=postData['email'], password=reg_pw)
    	# 	return(True, userinfo)
     #    #if not valid return false and an array of the errors
     #    else:

    def login(self, postData):
    	errors = []
    	# if email is found in db
    	if User.objects.filter(email=postData['email']):
            db_pw = User.objects.get(email=postData['email']).password
            # print db_pw
            login_pw = bcrypt.hashpw(postData['password'].encode(), db_pw.encode())
            # print login_pw
    		# check if passwords not match, then flash messages
            if login_pw != db_pw:
    			errors.append('Incorrect password')
    			return(False, errors)
    	#else if email is not found in db
    	else:
    		errors.append('Email has not been registered')
    		return(False, errors)


class User(models.Model):
    username = models.CharField(max_length=45)
    alias = models.CharField(max_length=45)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()

    def __str__(self):
        return "id: " + str(self.id) + ", username: " + self.username + ", alias: " + self. alias + ", email: " + self.email + ", password: " + self.password + ", dob: " + self.dob

class Poke(models.Model):
	poker = models.ForeignKey(User, related_name="pokingpoker")
	poked = models.ForeignKey(User, related_name="beingpoked")
	num_poker = models.IntegerField(default=200)
	count_poked = models.IntegerField(default=1000)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return "user_id: " + str(self.user.id) + ", user_alias: " + self.user.alias + ", "















