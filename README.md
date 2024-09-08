# Accuknox-Django-Trainee-Assignment  
This repository contains solutions for demonstrating the behavior of Django signals in response to three questions.  
Each question is implemented in a separate Django app: `myapp1`, `myapp2`, and `myapp3`.   

myapp1->Question 1 solution  
myapp2->Question 2 solution  
myapp3->Question 3 solution  
 
# Create a Virtual Environment:  
python -m venv venv  
source venv/bin/activate  # On Windows: venv\Scripts\activate  

# then install django using   
->pip install django  

# then run the below cmd   
py manage.py runserver  

# Viewing Outputs for Each Question  
# Question 1  
Answer: By default, Django signals are executed synchronously. This means when a signal is sent, the connected receiver functions are executed one by one in the order they are connected,   
and the sender waits for all receivers to complete before continuing execution.    

# click this url after running the cmd   
py manage.py runserver  
URL to Test: http://127.0.0.1:8000/myapp1/create/  

# console will display for question 1 as  
Signal received for: Test  
Signal handler execution completed.  
Object created.  

# Browser will display  
Object created and signal handled.  


# Question 2  
Answer: By default, Django signals run synchronously in the same thread as the caller. This means that when a signal is triggered, it is executed in the same thread as the operation that initiated the signal, blocking the caller until the signal handler finishes.  

# click this url after running the cmd   
py manage.py runserver  
URL to Test: http://127.0.0.1:8000/myapp2/create/  

# console will display for question 2 as  
View running in thread: <Thread-ID>  
Signal received for: Test  
Signal handler running in thread: <Same Thread-ID>  
Signal handler execution completed.  
Object created.  

# browser will display  
Object created and signal handled.  


# Question 3  
Answer: Yes, Django signals run in the same database transaction as the caller by default.  

# click this url after running the cmd   
py manage.py runserver  
URL to Test: http://127.0.0.1:8000/myapp3/create/  

# console will display for question 3 as  
Name before save: Original  
Signal received for: Original  
Name after save: Updated  


# browser will display  
Object created and modified.  


