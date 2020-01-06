Rekt
====

A Discord bot that moderates images, videos, and links with the help of
AWS Rekognition.


About
-----

Rekt is a typical Discord application, and can be added to a server by
anybody with the appropriate permissions via a generated link.  It will
listen for incoming messages, and perform a variety of checks against
each one.  In cases where there is some form of visual media, Rekt will
send the media to AWS Rekognition, to determine if any moderation action
needs to be taken against the image.

``` message -> checks(message) -> report -> handlers(report) ```

Built With
----------

* [boto3]()
* [moto]()
* [discordpy]()

Contributing
------------

 1. **Fork** the repository
 2. **Clone** the project from your forked repository to your macine
 3. **Commit** changes to your own branch
 4. **Push** your changes on your branch to your forked repository.
 5. Submit a **Pull request** back to our repository for review.

**NOTE**: always merge from latest upstream before submitting pull requests.

Versioning
----------

[Semantic Versioning](https://www.semver.org/) will be used to version this project.
Please consult the [releases](https://github.com/ptdel/Rekt/releases)
page for a complete list of available versions.

Authors
-------

* [Patrick Delaney](https://github.com/ptdel)

License
-------

`soon`