FINE_FACEBOOK = 150
FINE_INSTAGRAM = 100
FINE_REDDIT = 50
open_tabs = int(input())
salary = int(input())
web_facebook = "Facebook"
web_instagram = "Instagram"
web_reddit = "Reddit"
total_fine = 0

for page in range(open_tabs):
    opened_webs = input()
    if opened_webs == web_facebook:
        total_fine += FINE_FACEBOOK
    elif opened_webs == web_instagram:
        total_fine += FINE_INSTAGRAM
    elif opened_webs == web_reddit:
        total_fine += FINE_REDDIT
    if total_fine >= salary:
        break

if total_fine >= salary:
    print("You have lost your salary.")
else:
    print(salary - total_fine)
