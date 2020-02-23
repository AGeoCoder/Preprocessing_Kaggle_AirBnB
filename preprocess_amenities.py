#############################################
# 2/23/2020
# preprocess_amenities.py
# Written By: @AGeoCoder
#############################################

import csv

with open('amenities.csv', mode='w', newline='') as test_file:
    csv_writer = csv.writer(test_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    with open('SF_AirBnB_3.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')

        csv_writer.writerow(["id", "parking", "hvac", "hot_water", "breakfast", "kitchen", "laundry", "internet",
                            "laptop_friendly", "television", "family_friendly", "pets_allowed", "renters_pets",
                            "private_entrance", "private_bathroom", "essentials", "twenty_four_hour_check_in"])

        line_count = 0
        amenitiesText = "Amenities Text Variable Error"
        internet_count_error = 0 # Out of curiosity, how many times was "Wifi" listed without "Internet"?

        for row in csv_reader:
            line_count += 1

            # Reset Flags and Variables
            parking = "Parking Variable Error"
            ac_flag = False
            heat_flag = False
            hvac = "HVAC Variable Error"
            hot_water = "No Hot Water"
            breakfast = "No Breakfast"
            kitchen = "No Kitchen"
            washer_flag = False
            dryer_flag = False
            laundry = "Laundry Variable Error"
            internet = "Internet Variable Error"
            internet_flag = False
            wifi_flag = False
            laptop_friendly = "No Desk with Chair"
            television = "TV Variable Error"
            family_friendly = "Not Family Friendly"
            pets_allowed = "No Pets Allowed"
            dog_flag = False
            cat_flag = False
            renters_pets = "No pets already live on this property"
            other_pet_flag = False
            private_entrance = "No Private Entrance"
            private_bathroom = "No Private Bathroom"
            essentials = "No Essentials"
            twenty_four_hour_check_in = "No 24-Hour Check-In"

            id_variable = row[18]
            amenitiesText = row[19]

            #What parking is available?
            if amenitiesText.find("parking") != -1:
                if amenitiesText.find("Free parking on premises") != -1:
                    parking = "Free parking on premises"
                if amenitiesText.find("Free street parking") != -1:
                    parking = "Free street parking"
                elif amenitiesText.find("Paid parking off premises"):
                    parking = "Paid parking"
                else:
                    parking = "Unknown Parking Option Error"
            else:
                parking = "No parking"

            # What Air Conditioning and/or Heating is available?
            if amenitiesText.find("Air conditioning") != -1:
                ac_flag = True
            if amenitiesText.find("Heating") != -1:
                heat_flag = True
            if ac_flag and heat_flag is True:
                hvac = "Both"
            elif ac_flag is True:
                hvac = "Only AC"
            elif heat_flag is True:
                hvac = "Only Heating"
            else:
                hvac = "Neither"

            # Is hot water available?
            if amenitiesText.find('Hot water') != -1:
                hot_water = "Hot Water"

            # Is Breakfast Included?
            if amenitiesText.find('Breakfast') != -1:
                breakfast = "Breakfast"

            # Is a Kitchen Included?
            if amenitiesText.find('Kitchen') != -1:
                kitchen = "Kitchen"

            # Is a Washer and/or Dryer Included?
            if amenitiesText.find('Washer') != -1:
                washer_flag = True
            if amenitiesText.find('Dryer') != -1:
                dryer_flag = True
            if washer_flag and dryer_flag is True:
                laundry = "Washer and Dryer"
            elif washer_flag is True:
                laundry = "Only Washer"
            elif dryer_flag is True:
                laundry = "Only Dryer"
            else:
                laundry = "No Washer Or Dryer"

            # Is Internet Included?
            if amenitiesText.find('Internet') != -1:
                internet_flag = True
            if amenitiesText.find('Wifi') != -1:
                wifi_flag = True
            if internet_flag and wifi_flag is True:
                internet = "Wifi"
            elif internet_flag is True:
                internet = "No Wifi"
            elif wifi_flag is True:
                internet_count_error += 1
                internet = "Wifi"
            else:
                internet = "No Internet"

            # Is there a desk and chair?
            if amenitiesText.find('Laptop friendly workspace') != -1:
                laptop_friendly = "Desk with Chair"

            # Is there TV available?
            if amenitiesText.find('TV') != -1:
                if amenitiesText.find('Cable TV') != -1:
                    television = "Cable TV"
                else:
                    television = "Non-Cable TV"
            else:
                television = "No TV"

            # Is it Family/Kid Friendly?
            if amenitiesText.find('Family/kid friendly') != -1:
                family_friendly = "Family Friendly"

            # Are pets allowed?
            if amenitiesText.find('Pets allowed') != -1:
                pets_allowed = "Pets Allowed"
            if amenitiesText.find('Dog') != -1:
                dog_flag = True
            if amenitiesText.find('Cat') != -1:
                cat_flag = True
            if amenitiesText.find('Other pet') != -1:
                other_pet_flag = True
            if dog_flag and cat_flag and other_pet_flag is True:
                pets_allowed = "All Pets Allowed"
            elif dog_flag and cat_flag is True:
                pets_allowed = "Dogs and Cats"
            elif dog_flag and other_pet_flag is True:
                pets_allowed = "Dogs and Other"
            elif cat_flag and other_pet_flag is True:
                pets_allowed = "Cats and Other"
            elif dog_flag is True:
                pets_allowed = "Dogs Only"
            elif cat_flag is True:
                pets_allowed = "Cats Only"
            elif other_pet_flag is True:
                pets_allowed = "Other Pets Only"

            # Does the Renter Already Have Pets On the Property?
            if amenitiesText.find('Pets live on this property') != -1:
                renters_pets = "Pets already live on this property"

            # Is there a private entrance?
            if amenitiesText.find('Private entrance') != -1:
                private_entrance = "Private Entrance"

            # Is there a private bathroom?
            if amenitiesText.find('Private bathroom') != -1:
                private_bathroom = "Private Bathroom"

            # Are the essentials provided? (Essentials are defined to be Toilet paper, Soap (for hands and body),
            # One towel per guest, One pillow per guest, and Linens for each guest bed)
            if amenitiesText.find('Essentials') != -1:
                essentials = "Essentials Included"

            # Is 24-Hour Check In Available?
            if amenitiesText.find('24-hour check-in') != -1:
                twenty_four_hour_check_in = "24-Hour Check-In Available"

            # skip the first row of titles
            if line_count > 1:
                csv_writer.writerow([id_variable, parking, hvac, hot_water, breakfast, kitchen, laundry, internet, laptop_friendly,
                                     television, family_friendly, pets_allowed, renters_pets, private_entrance,
                                     private_bathroom, essentials, twenty_four_hour_check_in])
