import re

r = re.compile(r"m[a-z][a-z]\W")
content = "test map zoom cat mat may my fly match"

m_words = r.findall(content)

for match in m_words:

    print(match)


email = re.compile(r"^\w+@[a-zA-Z_]+?\.[a-zA-Z]{2,3}$")
address = "Is this example@example.com an email addres or no?"

is_email = email.search(address)
if is_email:
    print("yup")
    print(is_email)
else:
    print("nope")
