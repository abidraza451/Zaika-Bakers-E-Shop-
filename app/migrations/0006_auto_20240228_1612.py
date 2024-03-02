# Generated by Django 3.2.12 on 2024-02-28 10:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0005_alter_customer_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='state',
            field=models.CharField(choices=[('Puducherry', 'Puducherry'), ('Kerala', 'Kerala'), ('Lakshadweep', 'Lakshadweep'), ('Chhattisgarh', 'Chhattisgarh'), ('Telangana', 'Telangana'), ('Gujarat', 'Gujarat'), ('Maharashtra', 'Maharashtra'), ('Delhi', 'Delhi'), ('Jharkhand', 'Jharkhand'), ('Tripura', 'Tripura'), ('Karnataka', 'Karnataka'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Meghalaya', 'Meghalaya'), ('West Bengal', 'West Bengal'), ('Bihar', 'Bihar'), ('Rajasthan', 'Rajasthan'), ('Goa', 'Goa'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Andhra Pradesh', 'Andhra Pradesh'), ('Manipur', 'Manipur'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Haryana', 'Haryana'), ('Nagaland', 'Nagaland'), ('Assam', 'Assam'), ('Odisha', 'Odisha'), ('Mizoram', 'Mizoram'), ('Uttarakhand', 'Uttarakhand'), ('Chandigarh', 'Chandigarh'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Punjab', 'Punjab'), ('Sikkim', 'Sikkim'), ('Daman and Diu', 'Daman and Diu'), ('Tamil Nadu', 'Tamil Nadu'), ('Madhya Pradesh', 'Madhya Pradesh')], max_length=100),
        ),
        migrations.CreateModel(
            name='Wishlist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]