#the machine learning stuff here
import numpy as np
import numpy.linalg as linalg
# **something else needed??**

def updateRecommendations():
	all_entries = Survey.objects.all()
	count = Survey.objects.all().count()
	resources_used = all_entries.resources_used ## **check??**
	resource_count = Resource.objects.distinct().count()
	ratings = all_entries.rating ## **check??**

	#matrices needed for linear algebra
	matrix_ratings = np.zeros((count,1))   #column vector
	matrix_coefficients = np.zeros(resource_count,1)   #column vector
	matrix_binaryFeatures = np.zeros(count,resource_count)	#matrix

	#filling up known matrices
	for i in range(1,count):
		matrix_ratings[i,1]=ratings[i]
		for j in range(1,resource_count):
			if j in resources_used:
				matrix_binaryFeatures[i,j] = 1 


	#computing unknown matrix through linear algebra
	matrix_coefficients = linalg.solve(matrix_binaryFeatures,matrix_ratings)
