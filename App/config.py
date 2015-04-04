import os

config = {
    'PORT': os.getenv('OPENSHIFT_NODEJS_PORT', '8000'),
    'HOST': os.getenv('OPENSHIFT_NODEJS_IP', '0.0.0.0'),
    'MONGODB_URL':  os.getenv('OPENSHIFT_MONGODB_DB_URL', 'mongodb://localhost:27017/'),
    'Database': "dusty"
}