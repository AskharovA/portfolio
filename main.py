import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Резюме')

st.subheader("Добро пожаловать :wave:")
st.title("Резюме Асхаров А.")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['О себе', 'Проекты'],
        icons=['person', 'code-slash'],
        orientation='horizontal',
    )

if selected == 'О себе':
    st.header("О себе")
    st.write("""
    Асхаров Акылбек Ануарович\n
    :date: 1993 года рождения\n
    :email: a.askharov@gmail.com\n
    :phone: +7 (771) 869-63-93
    """)

    st.markdown(
        "<style>.text-justify { text-align: justify;}</style>"
        "<div class='text-justify'>"
        "Начинающий специалист в области backend-разработки с пониманием программирования на Python "
        "и создания веб-приложений с использованием Django. Имею опыт реализации RESTful API и работы с реляционными "
        "базами данных."
        "</div>", unsafe_allow_html=True)
    st.write('---')
    st.header("Технические навыки")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        - Языки программирования:
            - Python
            - JavaScript\n

        - Фреймворки:
            - Django
            - DjangoRestFramework
            - FastAPI\n

        - Веб технологии:
            - HTML5
            - CSS3
            - AJAX
            - WebSockets
            - REST API
            - Docker
            - Git\n
        """)
    with col2:
        st.write("""
        - Базы данных:
            - PostgreSQL
            - MySQL
            - SQLite3
            - MongoDB\n

        - Библиотеки:
            - StreamLit
            - Flet
            - PyWebIo
            - eel
            - SQL Alchemy
            - Bootstrap
            - HTMX
            - CustomTkinter\n
        """)
    st.write('---')
    st.header('Дополнительное знание программ')
    col3, col4 = st.columns(2)
    with col3:
        st.write("""
        - Adobe Photoshop
        - Adobe Illustrator
        - Adobe After Effects
        - Adobe Premier Pro
        - MAGIX Vegas Pro
        - Cubase Elements
        """)
    with col4:
        st.image('coding.gif', use_column_width=True)
    st.write('---')
    st.header("Образование")
    st.write("""
    - 2011 - 2015 г. Атырауский Институт Нефти и Газа\n
        Специальность: Автоматизация технологических процессов (бакалавриат)
    - 2022 - 2023 г. Step IT Academy Atyrau\n
        Специальность: Backend разработка на Python | Django
    """)
    st.write('---')
    st.header("Сертификаты")
    st.write('Нажмите, чтобы посмотреть сертификат об окончаний курса.')
    with st.expander('"Python Generation: курс для начинающих", Stepik, 2022г.'):
        st.image('cert/1.jpg', use_column_width=True)

    with st.expander('"Python Generation: курс для продвинутых", Stepik, 2023г.'):
        st.image('cert/2.jpg', use_column_width=True)

    with st.expander('"Python Generation: курс для профессионалов", Stepik, 2023г.'):
        st.image('cert/3.jpg', use_column_width=True)

    with st.expander('"Python-разработчик", Stepik, 2023г.'):
        st.image('cert/4.jpg', use_column_width=True)

    with st.expander('"Объектно-ориентированное программирование на Python", Stepik, 2023г.'):
        st.image('cert/5.jpg', use_column_width=True)

    with st.expander('"Django 4 для начинающих", Stepik, 2023г.'):
        st.image('cert/6.jpg', use_column_width=True)

    with st.expander('"Продвинутый Django 4 для продолжающих", Stepik, 2023г.'):
        st.image('cert/7.jpg', use_column_width=True)

    st.write('---')
    st.header("Профессиональный опыт")
    st.write("""
    - 2017 - 2023 г. Республиканский Центр Электронного Здравоохранения\n
        - Специалист сектора информатизаций здравоохранения
        - Системный администратор
    """)

    st.write('---')
    st.header("Дополнительная информация")
    st.write('- Английский язык: B1 (Intermediate)')
    st.write("""
    - Хобби
        - Игра на гитаре
        - Кодинг
        - Компьютерные игры
        - Сборка компьютеров
    """)

    st.markdown("""
    <style>
        img {
            border-radius: 10px;
        }
    </style>
    """, unsafe_allow_html=True)