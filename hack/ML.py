#the machine learning stuff here
from models import *
import numpy as np
import numpy.linalg as linalg
# **something else needed??**

def updateRecommendations():
	all_entries = Survey.objects.all()
	count = Survey.objects.all().count()
	resources_used = Survey.objects.resources_used ## **check??**
	resource_count = Resource.objects.distinct().count()
	ratings = all_entries.rating ## **check??**

	#matrices needed for linear algebra
	matrix_ratings = np.zeros((count,1))   #column vector
	matrix_coefficients = np.zeros(resource_count,1)   #column vector
	matrix_binaryFeatures = np.zeros(count,resource_count)	#matrix
	list_ratings = [];
	#filling up known matrices
	for i in range(1,count):
		matrix_ratings[i,1]=ratings[i]
		list_ratings.append(rating[i])
		for j in range(1,resource_count):
			if j in resources_used:
				matrix_binaryFeatures[i,j] = 1 


	#computing unknown matrix through linear algebra
	matrix_coefficients = linalg.solve(matrix_binaryFeatures,matrix_ratings)



	new_ratings = np.zeros((count,1))
	#using coefficients to compute new scores and select top 3
	for i in range(1,count):
		for j in range(1,resource_count):
			new_ratings[i,1] = new_ratings[i,1] + (matrix_coefficients[j,1] * matrix_binaryFeatures[i,j]) 
	

#use all combination of subsets and display the most powerful



##backup heuristic approach
#max1 = np.amax(ratings);

