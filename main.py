import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Резюме')

font_awesome_css = st.write(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    """, unsafe_allow_html=True
)

st.title("Асхаров А.")
st.subheader("Python Backend разработчик")

with st.container():
    selected = option_menu(
        menu_title=None,
        options=['О себе', 'Проекты'],
        icons=['person', 'code-slash'],
        orientation='horizontal',
    )

if selected == 'О себе':
    st.header("О себе")
    col1, col2 = st.columns(2)
    with col1:
        st.write("""
        ФИО: Асхаров Акылбек Ануарович\n
        :taurus: Год рождения: 1993 г.\n
        :e-mail: email: a.askharov@gmail.com\n
        :iphone: phone: +7 (771) 869-63-93\n
        :link: GitHub page: [AskharovA](https://github.com/AskharovA)
        """, unsafe_allow_html=True)
    with col2:
        st.image('coding.gif', use_column_width=True)
    st.markdown(
        "<style>.text-justify { text-align: justify; text-indent: 1rem;}</style>"
        "<div class='text-justify'>"
        "Начинающий специалист в области backend-разработки с пониманием программирования на Python "
        "и создания веб-приложений с использованием Django. Имею опыт реализации RESTful API и работы с реляционной "
        "базой данных PostgreSQL."
        "</div><br>", unsafe_allow_html=True)
    st.write(
        """
        - 7 лет опыт работы в сфере IT
        - 1 год опыт программирования
        """
    )
    st.write('---')
    st.header("Технические навыки")
    st.write(
        """
        - Программирование на языке :orange[**Python**]
        - Асинхронное программирование
        - Модульное и интеграционное тестирование
        - Создание пользовательских графических интерфейсов (GUI)
        - Создание Backend веб-приложений с помощью :orange[**Django**]
        - Создание REST API с помощью :orange[**Django REST Framework**]
        - Работа с реляционной базой данных :orange[**PostgreSQL**]
        - Создание асинхронных задач :orange[**Celery**]
        - Работа с Вебсокетами
        - Знание Frontend веб-технологии:
            - Работа с :orange[**DOM**]
            - Гипертекстовая разметка веб-страниц :orange[**HTML5**]
            - Работа со стилями :orange[**CSS3**] и фреймворком :orange[**Bootstrap5**]
            - Создание одностраничных и интерактивных приложений (SPA) с использованием :orange[**HTMX**]
        - Работа с кодом и системой управления версии :orange[**Git**], :orange[**GitHub**], :orange[**GitFlow**]
        - Контейнеризация и оркестрация с помощью :orange[**Docker**] и :orange[**Docker-Compose**]
        - Развертывание (:orange[**Deploy**]) веб-приложений на виртуальных серверах (:orange[**VPS**])
        """
    )
    st.write('---')
    st.header("Образование")
    st.write("""
    - 2011 - 2015 г. Атырауский Институт Нефти и Газа\n
        Специальность: Автоматизация технологических процессов (бакалавриат)
    - 2022 - 2023 г. Step IT Academy Atyrau\n
        Специальность: Backend разработка на Python
    """)
    with st.expander('Посмотреть Диплом'):
        st.image('diploma/1.jpg', use_column_width=True)
        st.image('diploma/2.jpg', use_column_width=True)
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

    with st.expander('"Django, shall we dance?", Stepik, 2023г.'):
        st.image('cert/8.jpg', use_column_width=True)

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
    st.write("""
    - Английский язык: A2 (Pre-Intermediate)
    - Личные качества:
        - Способность быстро обучаться
        - Адаптивность
        - Ориентация на качество кода
        - Терпение и настойчивость
    """)
    st.write("""
    - Хобби:
        - Игра на гитаре :orange[<i class="fa-solid fa-guitar"></i>]
        - Кодинг :orange[<i class="fa-solid fa-laptop-code"></i>]
        - Сборка компьютеров :orange[<i class="fa-solid fa-desktop"></i>]
        - Изучение новых технологий :orange[<i class="fa-solid fa-microchip"></i>]
    """, unsafe_allow_html=True)

    st.markdown("""
    <style>
        img {
            border-radius: 10px;
        }
        a {
            text-decoration: none;
        }
    </style>
    """, unsafe_allow_html=True)
if selected == 'Проекты':
    st.header('PlayQuiz - платформа для создания и проведения онлайн викторин в реальном времени')
    st.image('media/PlayQuiz.jpg', use_column_width=True)
    st.write("""
    :link: GitHub репозиторий: [AskharovA/django_online_quiz](https://github.com/AskharovA/django_online_quiz)\n
    :link: Страница веб-приложения: [playquiz.kz](https://playquiz.kz/)\n
    Платформа PlayQuiz - это FullStack веб-приложение созданный на основе фреймворка Django. Основной задачей является 
    предоставить пользователям инструмент для создания индивидуальных квизов и возможность участвовать в онлайн играх 
    с другими пользователями в реальном времени.\n
    Стек технологии:
    - Django: Основа веб-приложения, обеспечивающий backend и frontend.
    - HTML & CSS & Bootstrap: Структура и стиль интерфейса пользователя.
    - JavaScript & HTMX: Динамическое взаимодействие на стороне клиента. Отправка AJAX запросов.
    - PostgreSQL: База данных.
    - Celery: Организация асинхронных задач.
    - Eventlet Запуск асинхронных задач Celery.
    - Redis: Брокер сообщений, создание очереди задач.
    - Django Channels: Расширение веб-протокола Django, обработка WebSockets. Обработка данных в асинхронном режиме.
    - Channels-Redis: Основной канальный слой Channels.
    - Daphne: ASGI-сервер. Обработка входящих соединений WebSockets.
    - uWSGI: Веб сервер. Обеспечение эффективной загрузки.
    - NGINX: HTTP-сервер. Перенаправление запросов к uWSGI и Daphne.
    - Docker и Docker-compose: Контейнеризация и определение запуска веб-приложения.
    - Certbot: Получение и обновление SSL сертификатов от Let's Encrypt.
    """)
    st.write('---')

    st.header('API для Блога на Django Rest Framework')
    st.write("""
    :link: GitHub репозиторий: [AskharovA/DRF_blog](https://github.com/AskharovA/DRF_blog)\n
    RESTful API, разработанное с использованием Django Rest Framework, предназначено для управления блогом.\n
    Реализованный функционал:
    - Набор функций для создания, чтения, обновления и удаления (CRUD) постов блога
    - Безопасная система аутентификации с использованием JSON Web Tokens (JWT)
    - Модульные и интеграционные тесты
    - Кэширование ответов
    - Документация с помощью Swagger
    - Пагинация для управления большим объемом постов
    - Комментарии к постам
    - Добавление тегов к постам\n
    """)
    st.write('---')

    st.header('DarkPlayer - MP3 плеер на Python')
    st.image('media/DarkPlayer.jpg', use_column_width=True)
    st.write("""
    :link: GitHub репозиторий: [AskharovA/MP3Player-Python](https://github.com/AskharovA/MP3Player-Python)\n
    Приложение написано по принципам ООП. Создана для удобного создания плейлистов из локальных .mp3 файлов.\n
    Стек технологии:
    - Язык программирования: Python
    - GUI интерфейс приложения: CustomTkinter
    - Работа с аудио: PyGame\n
    Возможности:
    - Воспроизведение .mp3 файлов
    - Создание, сохранение и загрузка плейлистов
    - Удобное управление и контроллеры
    - Добавление из YouTube роликов без авторских прав\n
    """)

    st.markdown("""
    <style>
        * {
            text-align: justify;
        }
        img {
            border-radius: 15px;
        }
    </style>
    """, unsafe_allow_html=True)