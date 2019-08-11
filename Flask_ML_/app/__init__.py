from flask import Flask

app = Flask(__name__)

def create_app():
    
    # 组件注册
    from .api import api as api_blueprint
    app.register_blueprint(api_blueprint)

    app.config['REDIS_HOST'] = '127.0.0.1'
    app.config['REDIS_PORT'] = '6379'
    app.config['REDIS_DB'] = '0'
    app.config['REDIS_EXPIRE'] = '600'

    app.debug = True

    return app
