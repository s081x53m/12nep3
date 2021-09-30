import base64
import json

# नमस्ते

# message = "नमस्ते"
# message_bytes = message.encode()
# base64_bytes = base64.b64encode(message_bytes)
# base64_message = base64_bytes.decode('ascii')

# print(base64_message)

data = {}

# Notes
for i in range(1, 13):
    fread = open(f'notes/{i}', "r", encoding="utf8")
    content = fread.read()
    fread.close()

    data[i] = base64.b64encode(content.encode()).decode('ascii')



json_data = json.dumps(data)

fwrite = open('data.json', "w")
fwrite.write(json_data)
fwrite.close()