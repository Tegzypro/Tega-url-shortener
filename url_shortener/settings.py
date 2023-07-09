import os

SQLALCHEMY_DATABASE_URI=os.environ.get('DATBASE_URL')
SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite3'
SQLALCHEMY_TRACK_NOTIFICATIONS = False
ADMIN_USERNAME=os.environ.get('ADMIN-USERNAME')
ADMIN_PASSWORD=os.environ.get('ADMIN_PASSWORD')
# postgres://scissors_shortener_user:U3emawxW6tPTUEXwtPGxl0qbiJCFSSq7@dpg-cihm3ulgkuvojja275e0-a.oregon-postgres.render.com/scissors_shortener