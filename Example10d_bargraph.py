import matplotlib.pyplot as plt
import numpy as np
label = ['Adventure', 'Action', 'Drama', 'Comedy', 'Thriller/Suspense', 'Horror', 'Romantic Comedy', 'Musical',
         'Documentary', 'Black Comedy', 'Western', 'Concert/Performance', 'Multiple Genres', 'Reality']
no_movies = [941,854,4595,2125,942,509,548,149,1952,161,64,61,35,5]
index = np.arange(len(label))

plt.bar(index, no_movies)
plt.xlabel('Movietype', fontsize=8)
plt.ylabel('No of Movies', fontsize=8)
plt.xticks(index, label, fontsize=8, rotation=90)
plt.title('Movie type released during 2017-2019')
plt.show() 
