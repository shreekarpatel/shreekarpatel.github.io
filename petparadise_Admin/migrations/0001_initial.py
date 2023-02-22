# Generated by Django 3.2.10 on 2022-02-12 08:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('area_id', models.AutoField(primary_key=True, serialize=False)),
                ('area_name', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'area',
            },
        ),
        migrations.CreateModel(
            name='category',
            fields=[
                ('category_id', models.AutoField(primary_key=True, serialize=False)),
                ('category_name', models.CharField(max_length=20)),
                ('category_descripation', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'category',
            },
        ),
        migrations.CreateModel(
            name='customer',
            fields=[
                ('c_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_name', models.CharField(max_length=20)),
                ('c_email', models.EmailField(max_length=254, unique=True)),
                ('c_contact', models.CharField(max_length=20)),
                ('c_address', models.CharField(max_length=200)),
                ('c_password', models.CharField(max_length=20)),
                ('is_admin', models.IntegerField()),
                ('c_otp', models.CharField(max_length=10, null=True)),
                ('c_otp_used', models.IntegerField(null=True)),
                ('area_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.area')),
            ],
            options={
                'db_table': 'customer',
            },
        ),
        migrations.CreateModel(
            name='doctor',
            fields=[
                ('doctor_id', models.AutoField(primary_key=True, serialize=False)),
                ('doctor_name', models.CharField(max_length=20)),
                ('doctor_email', models.EmailField(max_length=254, unique=True)),
                ('doctor_password', models.CharField(max_length=20)),
                ('doctor_contact', models.CharField(max_length=20)),
                ('doctor_address', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_date', models.DateField()),
                ('total_amount', models.FloatField()),
                ('order_status', models.CharField(max_length=50)),
                ('payment_status', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.customer')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='shelter_home',
            fields=[
                ('shelter_id', models.AutoField(primary_key=True, serialize=False)),
                ('shelter_name', models.CharField(max_length=20)),
                ('owner_name', models.CharField(max_length=20)),
                ('shelter_email', models.EmailField(max_length=254, unique=True)),
                ('shelter_contact', models.CharField(max_length=20)),
                ('shelter_address', models.CharField(max_length=200)),
                ('shelter_password', models.CharField(max_length=20)),
                ('shelter_image', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'shelter_home',
            },
        ),
        migrations.CreateModel(
            name='sub_category',
            fields=[
                ('sub_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('sub_category_name', models.CharField(max_length=20)),
                ('sub_category_descripation', models.CharField(max_length=200)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.category')),
            ],
            options={
                'db_table': 'sub_category',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=50)),
                ('product_description', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('product_quantity', models.IntegerField()),
                ('product_image', models.CharField(max_length=200)),
                ('sub_category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.sub_category')),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='order_item',
            fields=[
                ('order_item_id', models.AutoField(primary_key=True, serialize=False)),
                ('qty_id', models.CharField(max_length=100)),
                ('product_price', models.FloatField()),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.order')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.product')),
            ],
            options={
                'db_table': 'order_item',
            },
        ),
        migrations.CreateModel(
            name='gallery',
            fields=[
                ('gallery_id', models.AutoField(primary_key=True, serialize=False)),
                ('image_path', models.CharField(max_length=200)),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.product')),
            ],
            options={
                'db_table': 'gallery',
            },
        ),
        migrations.CreateModel(
            name='feedback',
            fields=[
                ('feedback_id', models.AutoField(primary_key=True, serialize=False)),
                ('feedback_message', models.CharField(max_length=100)),
                ('feedback_date', models.DateField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.product')),
            ],
            options={
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='cart',
            fields=[
                ('cart_id', models.AutoField(primary_key=True, serialize=False)),
                ('c_date', models.DateField()),
                ('c_qty', models.IntegerField()),
                ('total_amt', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.customer')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.product')),
            ],
            options={
                'db_table': 'cart',
            },
        ),
        migrations.CreateModel(
            name='appointment',
            fields=[
                ('appointment', models.AutoField(primary_key=True, serialize=False)),
                ('appointment_time', models.CharField(max_length=100)),
                ('appointment_date', models.DateField()),
                ('appointment_status', models.IntegerField()),
                ('c_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.customer')),
                ('doctor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='petparadise_Admin.doctor')),
            ],
            options={
                'db_table': 'appointment',
            },
        ),
    ]
