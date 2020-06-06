import requests
import json

def template(data):
  return f"""
    <html>
      <p>{data.get('title')}</p>
    <html>
  """

def data():
  res = requests.request('GET', 'https://jsonplaceholder.typicode.com/todos/1')

  data = json.loads(res.content)

  return data

