# Django

---
Django is a web framework written using [Python](/wiki/Python) that allows for the design of web applications that generate [HTML](/wiki/HTML) dynamically.

Django (/ˈdʒæŋɡoʊ/ JANG-goh; sometimes stylized as django) is a free and open-source, Python-based web framework that runs on a web server. It follows the model–template–views (MTV) architectural pattern. It is maintained by the Django Software Foundation (DSF), an independent organization established in the US as a 501(c)(3) non-profit.

Django's primary goal is to ease the creation of complex, database-driven websites. The framework emphasizes reusability and "pluggability" of components, less code, low coupling, rapid development, and the principle of don't repeat yourself. Python is used throughout, even for settings, files, and data models. Django also provides an optional administrative create, read, update and delete interface that is generated dynamically through introspection and configured via admin models.

Some well-known sites that use Django include Instagram, Mozilla, Disqus, Bitbucket, Nextdoor, and Clubhouse.

History
Django was created in the autumn of 2003, when the web programmers at the Lawrence Journal-World newspaper, Adrian Holovaty and Simon Willison, began using Python to build applications. Jacob Kaplan-Moss was hired early in Django's development shortly before Willison's internship ended. It was released publicly under a BSD license in July 2005. The framework was named after guitarist Django Reinhardt.Holovaty is a Romani jazz guitar player inspired in part by Reinhardt's music.

In June 2008, it was announced that a newly formed Django Software Foundation (DSF) would maintain Django in the future.

## Feature

---
### Components

Despite having its own nomenclature, such as naming the callable objects generating the HTTP responses "views", the core Django framework can be seen as an MVC architecture.It consists of an object-relational mapper (ORM) that mediates between data models (defined as Python classes) and a relational database ("Model"), a system for processing HTTP requests with a web templating system ("View"), and a regular-expression-based URL dispatcher ("Controller").

Also included in the core framework are:

- a lightweight and standalone web server for development and testing
- a form serialization and validation system that can translate between HTML forms and values suitable for storage in the database
- a template system that utilizes the concept of inheritance borrowed from object-oriented programming
- a caching framework that can use any of several cache methods
support for middleware classes that can intervene at various stages of request processing and carry out custom functions
- an internal dispatcher system that allows components of an application to communicate events to each other via pre-defined signals
- an internationalization system, including translations of Django's own components into a variety of languages
- a serialization system that can produce and read XML and/or JSON representations of Django model instances
- a system for extending the capabilities of the template engine
- an interface to Python's built-in unit test framework

### Bundled applications
- The main Django distribution also bundles a number of applications in its "contrib" package, including:

- an extensible authentication system
- the dynamic administrative interface
- tools for generating RSS and Atom syndication feeds
- a "Sites" framework that allows one Django installation to run multiple websites, each with their own content and applications
- tools for generating Sitemaps
- built-in mitigation for cross-site request forgery, cross-site scripting, SQL injection, password cracking and other typical web attacks, most of them turned on by default

## Extensibility

---
Django's configuration system allows third party code to be plugged into a regular project, provided that it follows the reusable app conventions. More than 5000 packages are available to extend the framework's original behavior, providing solutions to issues the original tool didn't tackle: registration, search, API provision and consumption, CMS, etc.

This extensibility is, however, mitigated by internal components' dependencies. While the Django philosophy implies loose coupling,the template filters and tags assume one engine implementation, and both the auth and admin bundled applications require the use of the internal ORM. None of these filters or bundled apps are mandatory to run a Django project, but reusable apps tend to depend on them, encouraging developers to keep using the official stack in order to benefit fully from the apps ecosystem.

### Server arrangements
Django can be run on ASGI or WSGI-compliant web servers. Django officially supports five database backends: PostgreSQL, MySQL, MariaDB, SQLite, and Oracle.
Microsoft SQL Server can be used with mssql-django.