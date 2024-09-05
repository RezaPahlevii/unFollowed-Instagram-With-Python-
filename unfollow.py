from bs4 import BeautifulSoup

# Baca file followers.html dan following.html
with open('followers.html', 'r', encoding='utf-8') as followers_file:
    followers_soup = BeautifulSoup(followers_file, 'html.parser')

with open('following.html', 'r', encoding='utf-8') as following_file:
    following_soup = BeautifulSoup(following_file, 'html.parser')

# Ekstrak username dari followers dan following
followers = {elem.text.strip() for elem in followers_soup.find_all('a')}
following = {elem.text.strip() for elem in following_soup.find_all('a')}

# Dapatkan akun yang tidak mengikuti balik
not_following_back = following - followers

# Cetak hasil
print("Akun yang tidak mengikuti Anda kembali:")
for user in not_following_back:
    print(user)
