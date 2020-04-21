# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Actors(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'actors'


class Albums(models.Model):
    title = models.CharField(max_length=160)
    artist = models.ForeignKey('Artists', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'albums'


class Artists(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'artists'


class Categories(models.Model):
    name = models.CharField(max_length=25)
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'categories'


class Customers(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=20)
    company = models.CharField(max_length=80, blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    email = models.CharField(max_length=60)
    support_rep = models.ForeignKey('Employees', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customers'


class Employees(models.Model):
    last_name = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    title = models.CharField(max_length=30, blank=True, null=True)
    reports_to = models.ForeignKey('self', models.DO_NOTHING, db_column='reports_to', blank=True, null=True)
    birth_date = models.DateTimeField(blank=True, null=True)
    hire_date = models.DateTimeField(blank=True, null=True)
    address = models.CharField(max_length=70, blank=True, null=True)
    city = models.CharField(max_length=40, blank=True, null=True)
    state = models.CharField(max_length=40, blank=True, null=True)
    country = models.CharField(max_length=40, blank=True, null=True)
    postal_code = models.CharField(max_length=10, blank=True, null=True)
    phone = models.CharField(max_length=24, blank=True, null=True)
    fax = models.CharField(max_length=24, blank=True, null=True)
    email = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'employees'


class FilmActor(models.Model):
    actor_id = models.SmallIntegerField(primary_key=True)
    film_id = models.SmallIntegerField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_actor'
        unique_together = (('actor_id', 'film_id'),)


class FilmCategory(models.Model):
    film_id = models.SmallIntegerField()
    category_id = models.SmallIntegerField()
    last_update = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'film_category'


class Films(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    release_year = models.IntegerField(blank=True, null=True)
    language_id = models.SmallIntegerField()
    rental_duration = models.SmallIntegerField()
    rental_rate = models.DecimalField(max_digits=4, decimal_places=2)
    length = models.SmallIntegerField(blank=True, null=True)
    replacement_cost = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.TextField(blank=True, null=True)
    last_update = models.DateTimeField()
    special_features = models.TextField(blank=True, null=True)  # This field type is a guess.
    fulltext = models.TextField()  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'films'


class Genres(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'genres'


class InvoiceLines(models.Model):
    invoice = models.ForeignKey('Invoices', models.DO_NOTHING)
    track = models.ForeignKey('Tracks', models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'invoice_lines'


class Invoices(models.Model):
    customer = models.ForeignKey(Customers, models.DO_NOTHING)
    invoice_date = models.DateTimeField()
    billing_address = models.CharField(max_length=70, blank=True, null=True)
    billing_city = models.CharField(max_length=40, blank=True, null=True)
    billing_state = models.CharField(max_length=40, blank=True, null=True)
    billing_country = models.CharField(max_length=40, blank=True, null=True)
    billing_postal_code = models.CharField(max_length=10, blank=True, null=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'invoices'


class MediaTypes(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'media_types'


class PlaylistTrack(models.Model):
    playlist = models.OneToOneField('Playlists', models.DO_NOTHING, primary_key=True)
    track = models.ForeignKey('Tracks', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'playlist_track'
        unique_together = (('playlist', 'track'),)


class Playlists(models.Model):
    name = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playlists'


class Tracks(models.Model):
    name = models.CharField(max_length=200)
    album = models.ForeignKey(Albums, models.DO_NOTHING, blank=True, null=True)
    media_type = models.ForeignKey(MediaTypes, models.DO_NOTHING)
    genre = models.ForeignKey(Genres, models.DO_NOTHING, blank=True, null=True)
    composer = models.CharField(max_length=220, blank=True, null=True)
    milliseconds = models.IntegerField()
    bytes = models.IntegerField(blank=True, null=True)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        managed = False
        db_table = 'tracks'