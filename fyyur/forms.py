from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, SelectMultipleField, DateTimeField, BooleanField
from wtforms.validators import DataRequired, AnyOf, URL, InputRequired, Email, Regexp, Optional


state_choices = [
            ('AL', 'AL'),
            ('AK', 'AK'),
            ('AZ', 'AZ'),
            ('AR', 'AR'),
            ('CA', 'CA'),
            ('CO', 'CO'),
            ('CT', 'CT'),
            ('DE', 'DE'),
            ('DC', 'DC'),
            ('FL', 'FL'),
            ('GA', 'GA'),
            ('HI', 'HI'),
            ('ID', 'ID'),
            ('IL', 'IL'),
            ('IN', 'IN'),
            ('IA', 'IA'),
            ('KS', 'KS'),
            ('KY', 'KY'),
            ('LA', 'LA'),
            ('ME', 'ME'),
            ('MT', 'MT'),
            ('NE', 'NE'),
            ('NV', 'NV'),
            ('NH', 'NH'),
            ('NJ', 'NJ'),
            ('NM', 'NM'),
            ('NY', 'NY'),
            ('NC', 'NC'),
            ('ND', 'ND'),
            ('OH', 'OH'),
            ('OK', 'OK'),
            ('OR', 'OR'),
            ('MD', 'MD'),
            ('MA', 'MA'),
            ('MI', 'MI'),
            ('MN', 'MN'),
            ('MS', 'MS'),
            ('MO', 'MO'),
            ('PA', 'PA'),
            ('RI', 'RI'),
            ('SC', 'SC'),
            ('SD', 'SD'),
            ('TN', 'TN'),
            ('TX', 'TX'),
            ('UT', 'UT'),
            ('VT', 'VT'),
            ('VA', 'VA'),
            ('WA', 'WA'),
            ('WV', 'WV'),
            ('WI', 'WI'),
            ('WY', 'WY')]

genres_choices = [
            ('Alternative', 'Alternative'),
            ('Blues', 'Blues'),
            ('Classical', 'Classical'),
            ('Country', 'Country'),
            ('Electronic', 'Electronic'),
            ('Folk', 'Folk'),
            ('Funk', 'Funk'),
            ('Hip-Hop', 'Hip-Hop'),
            ('Heavy Metal', 'Heavy Metal'),
            ('Instrumental', 'Instrumental'),
            ('Jazz', 'Jazz'),
            ('Musical Theatre', 'Musical Theatre'),
            ('Pop', 'Pop'),
            ('Punk', 'Punk'),
            ('R&B', 'R&B'),
            ('Reggae', 'Reggae'),
            ('Rock n Roll', 'Rock n Roll'),
            ('Soul', 'Soul'),
            ('Other', 'Other')]


class ShowForm(FlaskForm):
    artist_id = StringField(
        'artist_id',
        validators=[InputRequired("Artist ID is required")]
    )
    venue_id = StringField(
        'venue_id',
        validators=[InputRequired("Venue ID is required")]
    )
    start_time = DateTimeField(
        'start_time',
        validators=[DataRequired("Need a show date & time")],
        default= datetime.today()
    )


class VenueForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired("Venue name is required")]
    )
    city = StringField(
        'city', validators=[DataRequired("City is required")]
    )
    state = SelectField(
        'state', validators=[DataRequired("Need to select a state")],
        choices=state_choices
    )
    address = StringField(
        'address', validators=[DataRequired("Need an address")]
    )
    phone = StringField(
        'phone', validators=[Regexp(r'^\d{3}-\d{3}-\d{4}$',
                                    message="Please provide a valid phone number (format xxx-xxx-xxxx)")]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        # TODO implement enum restriction
        'genres', validators=[DataRequired("Need to select at least a genre")],
        choices=genres_choices
    )
    facebook_link = StringField(
        'facebook_link', validators=[URL(), Optional()]
    )
    website_link = StringField(
        'website_link'
    )

    seeking_talent = BooleanField( 'seeking_talent' )

    seeking_description = StringField(
        'seeking_description'
    )


class ArtistForm(FlaskForm):
    name = StringField(
        'name', validators=[DataRequired("Artist name is required")]
    )
    city = StringField(
        'city', validators=[DataRequired("City is required")]
    )
    state = SelectField(
        'state', validators=[DataRequired("Need to select a state")],
        choices=state_choices
    )
    phone = StringField(
        # TODO implement validation logic for state
        'phone', validators=[Regexp(r'^\d{3}-\d{3}-\d{4}$',
                                    message="Please provide a valid phone number (format xxx-xxx-xxxx)")]
    )
    image_link = StringField(
        'image_link'
    )
    genres = SelectMultipleField(
        'genres', validators=[DataRequired("Need to select at least a genre")],
        choices=genres_choices
     )
    facebook_link = StringField(
        # TODO implement enum restriction
        'facebook_link', validators=[Optional(), URL()]
     )

    website_link = StringField(
        'website_link'
     )

    seeking_venue = BooleanField( 'seeking_venue' )

    seeking_description = StringField(
            'seeking_description'
     )

