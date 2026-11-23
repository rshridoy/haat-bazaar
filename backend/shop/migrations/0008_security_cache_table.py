from django.core.management import call_command
from django.db import migrations


def create_cache_table(apps, schema_editor):
    # The table behind settings.CACHES['security'] (login lockouts, auth/signup/guest-order limits).
    # Here so every `migrate`, Heroku's release phase included, makes it; skips a table that exists.
    call_command('createcachetable', database=schema_editor.connection.alias, verbosity=0)


class Migration(migrations.Migration):
    dependencies = [('shop', '0007_price_min_order_user_set_null')]

    operations = [migrations.RunPython(create_cache_table, migrations.RunPython.noop)]
