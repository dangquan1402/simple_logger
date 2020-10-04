import logging


LOGGING_CONFIG = { 
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': { 
        'standard': { 
            'format': '%(asctime)s: %(name)s: [%(levelname)s]: %(message)s'
        },
    },
    'handlers': { 
        'default': { 
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.StreamHandler',
        },
        'sample':{
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.FileHandler',
            'filename': 'sample1.log'
        },
        'rotate_time':{
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'when': 's',
            'interval': 1,
            'backupCount': 5,
            'filename': 'rotate.log'
        },
        'rotate_storage': {
            'level': 'INFO',
            'formatter': 'standard',
            'class': 'logging.handlers.RotatingFileHandler',
            'maxBytes': 100,
            'backupCount': 5,
            'filename': 'rotate_storage.log'
        }
    },
    'loggers': { 
        '__main__': {  # root logger
            'handlers': ['default', 'rotate_time', 'rotate_storage'],
            'level': 'DEBUG',
            
            
        },
        'employee_dict': { 
            'handlers': ['default', 'sample'],
            'level': 'INFO',
        }
    } 
}