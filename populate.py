import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'attendeestore.settings.dev')
django.setup()
import random
from faker import Faker
from attendee.models import Attendee, Attendee_photo

fakegen = Faker()
def PopulateList(N=10):
    for att in range(N):
        first_name = fakegen.first_name()
        last_name = fakegen.last_name()
        email = fakegen.email()
        noprefix = random.choice(['6', '7'])
        phone_number = f"+255{fakegen.numerify(noprefix + '########')}"
        organization = fakegen.company()
        role = random.choice([('Speaker', 0.8), ('Attendee', 0.1),
                              ('Organizer', 0.05), ('Volunteer', 0.05), ('Sponsor',
                                                                         0.05), ('Exhibitor', 0.05), ('Media', 0.05),
                              ('VIP', 0.05), ('Partner', 0.05), ('Guest', 0.05), ('Other', 0.05)])

        attendee = Attendee.objects.get_or_create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            organization=organization,
            role=role[0]  # Extract the role name from the tuple
        )[0]

        # Create a corresponding Attendee_photo instance
        # Example photo path
        photo_path = f'photos/{first_name}_{last_name}.jpg'
        photo = Attendee_photo.objects.get_or_create(
            attendee=attendee, photo=photo_path)[0]


if __name__ == '__main__':
    print("Populating the database with fake attendees...")
    PopulateList(100)
    print("Database population complete.")
