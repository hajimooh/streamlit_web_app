import streamlit as st
import datetime

with st.form(key='profile_form'):
    #テキストボックス
    name = st.text_input('名前')
    address = st.text_input('住所')

    #セレクトボックス
    age_category = st.selectbox(
        '年齢層',
        ('子ども(18歳未満)',  '大人(18歳以上)')
    )
    #ラジオボタン
    sex = st.radio(
        '性別',
        ('女',  '男', '答えたくない')
    )

    #複数選択
    hobby = st.multiselect(
        '趣味',
        ('スポーツ', '読書', 'プログラミング', '登山', '料理', '釣り', '映画')
    )

    #チェックボックス
    mail_subscribe = st.checkbox('メールマガジンを購読する')

    #スライダー
    height = st.slider('身長', min_value=110, max_value=210)

    #日付
    start_data = st.date_input(
        '開始日',
        datetime.date(2202, 7, 1)
    )

    #カラーピッカー
    color = st.color_picker('テーマカラー', '#00f900')
    
    #ボタン
    # submit_btn = st.button('送信')
    # cancel_btn = st.button('キャンセル')
    submit_btn = st.form_submit_button('送信')             #formの内容を一括で渡すsubmitボタン
    cancel_btn = st.form_submit_button('キャンセル')

    if submit_btn:
        st.text(f'ようこそ！ {name}さん！{address}に書籍を送りました！')
        st.text(f'年齢層： {age_category}')
        st.text(f'性別： {sex}')
        st.text(f'趣味： {", ".join(hobby)}')