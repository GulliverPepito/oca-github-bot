# Copyright (c) ACSONE SA/NV 2018
# Distributed under the MIT License (http://opensource.org/licenses/MIT).

from celery.schedules import crontab

from .queue import app

app.conf.beat_schedule = {
    "heartbeat": {
        "task": "oca_github_bot.tasks.heartbeat.heartbeat",
        "schedule": crontab(minute="*/15"),
    },
    "main_branch_bot_all_repos": {
        "task": "oca_github_bot.tasks.main_branch_bot.main_branch_bot_all_repos",
        "args": ("OCA",),
        "schedule": crontab(hour="2", minute="30"),
    },
    "tag_ready_to_merge": {
        "task": "oca_github_bot.tasks.tag_ready_to_merge.tag_ready_to_merge",
        "args": ("OCA",),
        "schedule": crontab(minute="0"),
    },
}
