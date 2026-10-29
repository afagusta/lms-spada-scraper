!pip install beautifulsoup4 requests pandas

from bs4 import BeautifulSoup
import pandas as pd
import requests
import time
from google.colab import files

data = []

# Header agar request tidak dianggap sebagai bot
headers = {
    'User-Agent': (
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML,'
        ' like Gecko) Chrome/120.0.0.0 Safari/537.36'
    )
}

print('Memulai proses scraping ID 4435 sampai 4455...\n')

# Looping dari ID 4435 sampai 4455
# max id 4468
for course_id in range(4435, 4456):
  url = (
      f'https://lmsspada.kemdiktisaintek.go.id/course/view.php?id={course_id}'
  )

  try:
    response = requests.get(url, headers=headers, timeout=10)

    if response.status_code == 200:
      soup = BeautifulSoup(response.text, 'html.parser')

      title_elem = soup.find('h1', {'class': 'h2'}) or soup.find('title')
      title = title_elem.text.strip() if title_elem else 'Tidak Diketahui'

      if 'Log in' in title or 'Masuk' in title:
        course_title = 'Butuh Login / Private Course'
      else:
        course_title = title

      sections = soup.find_all('li', {'class': 'section'})
      topic_list = []
      for sec in sections:
        sec_title = sec.find('h3') or sec.find('span', {'class': 'sectionname'})
        if sec_title:
          topic_list.append(sec_title.text.strip())

      data.append({
          'ID': course_id,
          'URL': url,
          'Judul Course': course_title,
          'Jumlah Topik': len(sections),
          'Topik Pertama': topic_list[0] if topic_list else '-',
      })
      print(f'[SUKSES] ID {course_id} berhasil diproses.')
    else:
      print(f'[GAGAL] ID {course_id} - Status Code: {response.status_code}')

  except Exception as e:
    print(f'[ERROR] ID {course_id}: {e}')

  time.sleep(1)

# Buat DataFrame Pandas
df = pd.DataFrame(data)

# Tampilkan tabel langsung di Colab
display(df)

# Simpan dan otomatis download file CSV-nya
filename = 'lms_spada_courses_4435_4455.csv'
df.to_csv(filename, index=False)
print(f'\nSelesai! File "{filename}" berhasil di-download otomatis.')
files.download(filename)
