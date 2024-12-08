facebook = False
twitter = True
instagram = True


if (facebook and twitter) or (twitter and instagram) or (facebook and instagram):
    print(f"You are a good influencer!")