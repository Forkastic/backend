# encoding: utf8
from django.db import models, migrations
import model_utils.fields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(editable=False, verbose_name='created', default=django.utils.timezone.now)),
                ('modified', model_utils.fields.AutoLastModifiedField(editable=False, verbose_name='modified', default=django.utils.timezone.now)),
                ('name', models.CharField(max_length=255)),
                ('proteins', models.FloatField()),
                ('carbs', models.FloatField()),
                ('fat', models.FloatField()),
            ],
            options={
                'abstract': False,
            },
            bases=(models.Model,),
        ),
    ]
