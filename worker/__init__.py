import os
from celery import Celery

# 设置环境变量，加载Django的settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'swiper.settings')

# 创建Celery Application
celery_app = Celery('swiper')
celery_app.config_from_object('worker.config')
celery_app.autodiscover_tasks()


def call_by_worker(func):
    """将任务在celery中异步执行"""
    task = celery_app.task(func)
    return task.delay
