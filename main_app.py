# マルチ画面
# このメイン画面と同じフォルダにpagesフォルダを作成し、そこにサブ画面のスクリプトを配置する
import streamlit as st
from PIL import Image

st.title('サプーアプリ')
st.caption('これはさぷーの動画用テストアプリです')

image = Image.open('./data/flower_ume_kaika.png')
st.image(image, width=200)