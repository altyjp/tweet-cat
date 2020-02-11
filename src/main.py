import json
import param
import twitter
import urllib.request

# giphyからネコ画像を検索する
cat_gif_url = None
url = 'https://api.giphy.com/v1/gifs/random?api_key=' + param.ParamGiphy().API_KEY + '&tag=cat&rating=G'
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as res:
    resJSON = json.loads(res.read())
    cat_gif_url = resJSON["data"]["images"]["fixed_height"]["url"]

print("cat_gif_url = " + cat_gif_url)

# ダウンロードを実行
cat_file_name = "./download/cat.gif" # ネコ画像の位置
urllib.request.urlretrieve(cat_gif_url, cat_file_name)


# ツイッターへ認証を行う
auth = twitter.OAuth(
    consumer_key=param.ParamOAuth().consumer_key,
    consumer_secret=param.ParamOAuth().consumer_secret,
    token=param.ParamOAuth().token,
    token_secret=param.ParamOAuth().token_secret
)

t = twitter.Twitter(auth=auth)

# ネコ画像をツイートする
# ダウンロードした画像ファイルを読み込む
with open(cat_file_name,"rb") as image_file:
 image_data=image_file.read()
# 呟く文字列
tweet_str = "[Bot]Cat here!"
# 画像のアップロード
pic_upload = twitter.Twitter(domain='upload.twitter.com',auth=auth)
id_img = pic_upload.media.upload(media=image_data)["media_id_string"]

t.statuses.update(status=tweet_str,media_ids=id_img)
