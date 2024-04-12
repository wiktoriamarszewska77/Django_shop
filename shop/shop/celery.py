import os
from celery import Celery, signals
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from dotenv import load_dotenv

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "shop.settings")

app = Celery("shop")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


@signals.celeryd_init.connect
def init_sentry(**_kwargs):
    sentry_sdk.init(
        dsn=os.getenv("dsn"),
        enable_tracing=True,
        integrations=[
            CeleryIntegration(
                monitor_beat_tasks=True,
                exclude_beat_tasks=["unimportant-task", "payment-check-.*"],
            ),
        ],
    )
