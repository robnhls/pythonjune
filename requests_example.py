import requests


path = 'https://www.nasa.gov/pdf/739318main_ISS%20Utilization%20Brochure%202012%20Screenres%203-8-13.pdf'
local_name = 'nasa.pdf'

with requests.get(path, stream=True) as r:
    r.raise_for_status()  # 200 OK, 404 Not found
    with open(local_name, "wb") as output_file:
        for chunk in r.iter_content(chunk_size=512):
            if chunk:
                output_file.write(chunk)

print("all done")
