
# Low-Level Cache API in Django

Using the [low-level cache API](https://docs.djangoproject.com/en/5.1/topics/cache/#the-low-level-cache-api), you can selectively cache specific data rather than the entire view, ensuring that you cache only the information that rarely changes. This allows you to optimize performance while still providing up-to-date data for frequently changing elements.

You can cache various Python objects—such as strings, dictionaries, and lists of model instances—that can be safely pickled. This flexibility enables you to create tailored caching strategies that meet your application's specific needs. By leveraging this API, you can significantly enhance your application's efficiency without compromising on the freshness of dynamic data.


# Caching Python Objects

In the Athlete Management System, caching Python objects plays a crucial role in optimizing performance and resource management. By leveraging Django's caching framework, the system stores athlete data in memory for a specified duration. This allows frequently accessed athlete records to be retrieved quickly, significantly reducing the need for repetitive database queries. When users request athlete lists or perform country-specific searches, the application first checks the cache. If the requested data is available, it serves it instantly, ensuring minimal delay. If not, the application fetches the data from the database, populates the cache, and serves the response. This strategy not only speeds up user interactions but also alleviates database load, leading to a more efficient and responsive application overall.


## Features
- View a list of athletes.
- Filter athletes by country.
- Pagination (10 athletes per page).
- Caching of athlete data for performance optimization.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sohail342/LowLevel-CacheAPI-Django.git
   ```

2. **Create a virtual environment and activate it:**
    ```bash
    python -m venv venv
    Source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4. **Apply the migrations:**
    ```bash
    python manage.py migrate
    ```
5. **Run the development server:**
    ```bash
    python manage.py runserver

    ```
6. **Access the website:**
    Open http://127.0.0.1:8000/ in your web browser.


## Contact

If you have any questions or feedback, feel free to reach out:

<p align="left">
<a href="https://wa.me/+923428041928" target="blank"><img align="center" src="https://img.icons8.com/color/48/000000/whatsapp.png" alt="WhatsApp" height="30" width="40" /></a>
<a href="https://www.hackerrank.com/sohail_ahmad342" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/hackerrank.svg" alt="sohail_ahmad342" height="30" width="40" /></a>
<a href="https://www.linkedin.com/in/sohailahmad3428041928/" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="sohail-ahmad342" height="30" width="40" /></a>
<a href="https://instagram.com/sohail_ahmed113" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="sohail_ahmed113" height="30" width="40" /></a>
<a href="mailto:sohailahmed34280@gmail.com" target="blank"><img align="center" src="https://img.icons8.com/ios-filled/50/000000/email-open.png" alt="Email" height="30" width="40" /></a>
</p>
