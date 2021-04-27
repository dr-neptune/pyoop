from filestack import Client

client = Client("AViVqp7suSQWWEdrl6hf9z")

new_filelink = client.upload(filepath = "files/scratch.txt")
print(new_filelink.url)
