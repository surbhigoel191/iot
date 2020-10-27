# -*- encoding: utf-8 -*-
"""
License: MIT
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Drone(models.Model):
	lat = models.DecimalField(max_digits=9, decimal_places=7)
	lon = models.DecimalField(max_digits=10, decimal_places=7)
	vel = models.DecimalField(max_digits=5, decimal_places=2)
	acc = models.DecimalField(max_digits=5, decimal_places=2)
	# bitsid = models.CharField(max_length = 20, unique = True)
	# contact = models.IntegerField(default = 0,validators = [MinValueValidator(100000000),MaxValueValidator(9999999999)])
	# use_required_attribute = True

	# def update_user_profile(sender, instance, created, **kwargs):
	# 	if created:
	# 		Candidate.objects.create(user=instance)
	# 		instance.Candidate.save()
	# def __str__(self):
	# 	return self.bitsid
