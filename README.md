# mobileapp

1. CREATED FOLDER "MobAppDev_Assignment1" for proj name and env folder.
2. python -m venv venv2                         creates folder with python package inside the MobAppDev_Assignment1 folder.
3. venv2\Scripts\activate                       activates and u'll see (venv2) C: blabla
4. pip install Django                           when (venv2) visible. to install django
   python -m django --version                   version check
5. django-admin startproject core .             create Django project folder inside MobAppDev_Assignment1 folder
6. python manage.py startapp reservation_app    create DJANGO app folder inside DJANGO contains models,admin.py and migrations
7. models.py > create customer/table/tablecategory/reservationstatus/reservation/payment/auditlog model
8. settings.py > installed_apps > insert reservation_app    record reservation_app
9. python manage.py makemigrations              to record migration or partial migration
10. python manage.py migrate                    to migrate it
11. create forms.py inside reservation_app
12. create views.py inside reservation_app
13. create urls.py inside reservation_app
14. python manage.py runserver                  Starting development server at http://127.0.0.1:8000/
                                                                               http://127.0.0.1:8000/admin/
