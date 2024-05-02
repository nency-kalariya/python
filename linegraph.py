import matplotlib.pyplot as plt

years=['2001','2002','2003','2004','2005']
moviesrelease=[12,65,44,35,71]

plt.plot(years,moviesrelease,color='green')

plt.xlabel('Number of movies')
plt.ylabel('years')



plt.title('Movie releases')
plt.legend()
plt.show()
