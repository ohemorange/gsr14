#the machine learning stuff herei
import numpy as np


all_entries = Survey.objects.all()
count = Survey.objects.all().count()
resources_used = all_entries.resources_used
resource_count = Resource.objects.distinct().count()

#matrices needed for linear algebra
matrix_ratings = np.zeros((count,1))   #column vector
matrix_coefficients = np.zeros(resource_count,1)   #column vector
matrix_binaryFeatures = np.zeros(count,resource_count)	#matrix
for i in range(1,count)
	resources_used[i]
