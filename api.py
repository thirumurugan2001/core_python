from sanic import sanic
from sanic.response import json
app=sanic()
@app.route("/")
async def hello (request):
    return json("Hello thiru")

if __name__== "__main__":
    app. run(host="0.0.0.0",port=8000)
