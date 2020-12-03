from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='likes',
            field=models.ManyToManyField(related_name='review_likes', through='book.Like', to='user.User'),
        ),
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='like',
            name='review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='book.review'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.category'),
        ),
        migrations.AddField(
            model_name='book',
            name='keyword',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='book.keyword'),
        ),
        migrations.AddField(
            model_name='book',
            name='reviews',
            field=models.ManyToManyField(through='book.Review', to='user.User'),
        ),
    ]