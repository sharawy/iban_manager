# iban_manager
Simple user iban management 
### How to run
- Edit configuration in common.env
   - SECRET_KEY
   - GOOGLE_KEY
   - GOOGLE_SECRET
- Add admin info in settings.py to be used by the custom command `python manage.py initadmin`
<br/>example: `ADMINS = (
   'name', 'example@example.com'
)` 
- Run command `docker-compose up`
##### or
- `pip install -r requirements.txt`
- Edit settings.py
  - Add admin info in settings.py to be used by the custom command `python manage.py initadmin`
<br/>example: `ADMINS = (
   'name', 'example@example.com'
)` 
  - SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET to enable google authentication 
  - DATABASES
- `python manage.py runserver`

   
 ### Models
 - BaseUser: shared base class with common fields for all users
 - Admin: The authentication model for the project 
 - User: Normal user created by admins
 - BankAccount: contain user iban info
 
 ### Permissions
 `Only superusers and staff can acces the admin panel`
 - ExtraObjectLevelPermission: Base class provide generic way to apply custom object level perimission to the ModelAdmin
 - AllowOnlyCreatorToChangeDeleteUser: Restrict change or delete to user model
 - AllowOnlyCreatorIBAN: Restircit change or delete user model
 
 ### Scripts
 - entrypoint.sh: used by docker-compose to run the following commands:

    - Apply database migrations
      `python manage.py migrate`

    - Create default admin
        `python manage.py initadmin`

    - Start server
        `uwsgi --ini /app/iban_manager/wsgi/uwsgi.ini`
