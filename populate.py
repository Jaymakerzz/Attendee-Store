import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendeestore.settings.dev')
django.setup()

from attendee.models import Attendee, Attendee_photo
from faker import Faker
import random 

fakegen = Faker()

ROLES = ['Speaker', 'Attendee', 'Organizer', 'Volunteer', 'Sponsor',
         'Exhibitor', 'Media', 'VIP', 'Partner', 'Guest', 'Other']
WEIGHTS = [0.8, 0.1, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05, 0.05]


def populate_list(n=10):
    for _ in range(n):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        attendee = Attendee.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=fakegen.unique.email(),
            phone_number=f"+255{random.choice('67')}{fakegen.numerify('########')}",
            organization=fakegen.company(),
            role=random.choices(ROLES, weights=WEIGHTS, k=1)[0],
        )
        Attendee_photo.objects.create(
            attendee=attendee,
            photo=f'photos/{first_name}_{last_name}.jpg',
        )


if __name__ == '__main__':
    if Attendee.objects.exists():
        print("Attendees already exist, skipping population.")
    else:
        print("Populating the database with fake attendees...")
        populate_list(100)
        print("Database population complete.")
