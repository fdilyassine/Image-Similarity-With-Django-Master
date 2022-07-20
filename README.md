# Image-Similarity-With-Django-Master
### Welcome To My Django Rest API Project

HOW TO INSTALL AND USE THIS PROJECT :


- INSTALLATION :


1- INSTALL PYTHON 3.10.1  (https://www.python.org/downloads/)

2- INSTALL PIP (https://pip.pypa.io/en/stable/installing/)

3- cd INSIDE THE PROJECT AND USE THE PIP COMMAND TO INSTALL THE REQUIREMENTS VIA THE FOLLOWING COMMAND (pip install -r requirements.txt)
   note : for the annoy library you will need to install "visual c ++ build tools" first


- USAGE : 


1- cd INSIDE THE APP FOLDER (/app), AND VECTORIZE THE DATABASE OF IMAGES VIA THE COMMAND  
(python vectorize_database.py "/path/to/the/database/of/images")

2- RENAME THE VECTORS BY PUTTING THE FULL PATH TO THE /image_vectors FOLDER IN THE rename.py FILE AND USE THE FOLLOWING COMMAND 
(python rename.py) 
note : only rename the files that contain three "." in the name, example : "2018.3100.002383_xx_xx_jKynk.jpg.npz --> 2018-3100-002383_xx_xx_jKynk-jpg.npz" 

3- CREATE THE MODEL BY USING THE COMMAND (python database_model.py)

4- cd .. BACK INTO THE MAIN DIRECTORY

5- RUN THE LOCAL SERVER VIA THE COMMAND (python manage.py runserver)

