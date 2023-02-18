# Dashboard_project_BG

![imagen](images/Portada.jpeg) 

## OBJECTIVE
---

I have decided to carry out this visualization project following my [previous hotel data analysis project](https://github.com/Belengasset/Project_Jan22_Hotels). 
The former project consisted in evaluating if the ranking proposed by Travel+ Leisure magazine was in line with what Tripadvisor and Google Reviews users thought.

This time the project goes further, from the databases of the hotels of the previous project together with a database of restaurants of the Michelin Guide, I propose you three possibilities in which you can travel according to your preferences. First you can choose where you want to travel and I will propose you the best hotel, in the same way the best restaurant of the michelin guide. Finally I will propose you a complete experience, combining the best hotel and restaurant of the country of your choice.

In this [link](https://public.tableau.com/app/profile/bel.n.gasset.cortejarena7615/viz/Dashboard_project_BGC/DashboardRest?publish=yes) you can find the visualization project realized in **Tableau Public**. 


## Folders
----

[Data](https://github.com/Belengasset/Dashboard_project_BG/tree/main/Data): *Contains the csv's that I have been generating throughout the work.*

[Images](https://github.com/Belengasset/Dashboard_project_BG/tree/main/Images): *Contains the files (images) to insert in the jupyters*

[Notebook](https://github.com/Belengasset/Dashboard_project_BG/tree/main/Notebook): *Contains the files (Jupyter notebooks) where the code is*

src

## Project development
---
### **I. Data set**

#### **Data extraction**

As I have already mentioned, the databases related to the hotels I have extracted them from my previous project, where you will find more detail of each of the csv.

What's new about the data concerning the hotels is the data set containing the website of each hotel. everything is done in the file [1- Scrapping_hotels](https://github.com/Belengasset/Dashboard_project_BG/tree/main/Notebook#:~:text=1%2D%20Scrapping_hotels.ipynb). To perform a data extraction by Web Scraping, using *Selenium* to interact with web browsers and perform actions such as clicking buttons, filling out forms, and navigating between pages. In this phase of web escraping I thought it appropriate to do it by extracting information through Google as I already had the code to do the scrapping. I've created a dataframe which contains the hotels (uniques), eliminating the repeated ones, as some of them were in both rankings), so that the extraction would be faster.

Then, to obtain perform the gastronomic experience I've decided to get the file from [Kaggle](https://www.kaggle.com/datasets/ngshiheng/michelin-guide-restaurants-2021). This file contains a dataset of the **Michelin Guide Restaurants** from all around the world curated from https://guide.michelin.com/en/restaurants. The culinary distinctions included are 3 Stars,2 Stars,1 Star,Bib Gourmand.

![imagen](images/michelin.jpeg)

### **II. Cleaning**

In the notebook [2 - Clean_Notebook](https://github.com/Belengasset/Dashboard_project_BG/tree/main/Notebook#:~:text=2%20%2D%20Clean_Notebook.ipynb)is where all the cleaning and adjustments are done.

No cleaning was needed for the hotels link file as the scrapping worked well, only I had to include with `.loc` the few missing websites that the scrapping wasn't abble to get.

Regarding the restaurants files, some updated where done. First, I've creates with `lambda` a new column called **country** with the data from the Address column, which is primordial to make the link between datasets. Moreover, I've created a function with the type of cuisine and group the restaurants, as there are many different types. I though, also, it might be usefull to  seprate the caracterics which are more relevant, creating several columns to see if they have the facilitiy or service with a fuction which you can find in the *scr folder*.

Finally, I've decided to create a dataframe with the rates to be able to convert after, the average price of the restaurant into euros, as it's given in local currency.

Once everything is clean, the next step is to create the visualisation through Tableau Public.

### **III. Tableau**

#### **1- Dashboard Index**
![imagen](images/index.png)

The first dashboard, called **Dashboard Index**, contains the index of the different experience dashboards. in it you will find a brief description of each one and its direct link.

#### **2- Dashboard Hotel**

![imagen](images/best_hotel.png)
In this second dashboard, I propose the hotel experience. You can choose the *country* and depending on your choice you will get the **best hotel** according to the reviews of users of Google and Tripadvisor within the list of those proposed by Travel + Leisure.
On the dashboard map, if you position yourself in a certain country, you will see the types of hotels in that country thanks to the use of the pop-up description.
![imagen](images/Hotel_map_descemerg.png)

Once you have selected the country, the graph below will show you the **best hotel** and the results of user reviews from Google Reviews and Tripadvisor websites. Also if you click on any bar you will see more details of the proposed hotel. 
![imagen](images/Hotel_barrras_descemerg.png)

Finally, if you click on the name of the hotel in the graph on the right side of the dashboard, it will give you access to the **hotel web page** and you will be able to browse or make your reservation directly!

#### **3- Dashboard Restaurant**

![imagen](images/best_restaurant.png)

The third dashboard presents the gastronomic experience. First, on the **map** you can select the *country* in which you want to enjoy the experience. If you position yourself in a specific country you will be able to see thanks to the pop-up description the type of gastronomy of the restaurants in that country. Then you can select a country and the dashboard will adjust to your choice. 
![imagen](images/Rest_map_descemergente.png)

On the right side, you wil find the two best restaurant of the country with it's price and michelin award. 
As there are many restaurants in several countries, I've decided to present all the restaurants of the country and more detail about them in case you may not want the best restaurante but choose several caracteristics.
Finally, you can click on the hotel name so the web page of the restaurant will appear on the bottom right side and make you reservation directly.
![imagen](images/1best.png)


#### **4- Dashboard Union**
![imagen](images/Full_experience.png)
In this dashboard you will be able to combine both experiences, the hotel and the gastronomic. To do so, you only need to choose a country (it will allow to select only the countries in which you have hotels AND restaurants). Once you select the desired country, in the right side you will find the two best restaurants and below th map the chart with the reviwes of the best hotel of the country. 
As on the other dashboards, if you click on the name of the hotel and restaurant you will be able to do all your reservations!


#### **5- History**

The history, called in **Tavel experience** ,  is composed of the four previous dashboards and where you can save the results of the selection made.

![imagen](images/History.png)

## Libraries
----

- [Pandas](https://pandas.pydata.org/): library is used for data analysis and manipulation
- [Numpy](https://numpy.org/): library is used for numerical operations
- [Selenium](https://www.selenium.dev/): popular open-source tool for automating web browsers. It provides a way to programmatically interact with web pages, allowing you to simulate actions such as clicking buttons, filling out forms, and navigating between pages.
- [Requests](https://requests.readthedocs.io/en/master/): Python library for making HTTP requests
- [Warnings](https://docs.python.org/3/library/warnings.html): warnings are messages that are generated to indicate that something unexpected has occurred, but the program can continue running.

## Contact
----

This work has allowed me to improve my programming skills, to put into practice what has been learned in visualization and more importantly learn to discern and filter what is relevant.

Do no hesitate to contact me belen.gassetc@gmail.com