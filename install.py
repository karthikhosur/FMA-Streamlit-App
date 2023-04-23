import gdown

url = 'https://drive.google.com/uc?id=1b2xSsUtaD-oD3cygmpvZPY1gUi9oQoJK'
output = 'data/merged_file.csv'
gdown.download(url, output, quiet=False)