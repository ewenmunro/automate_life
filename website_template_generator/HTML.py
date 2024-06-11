#HTML
html = '''
<!DOCTYPE html>
<html>
  <head>
    <!-- UTF-8 -->
    <meta charset="UTF-8" />
    <!-- responsive web-design -->
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <!-- Internet Explorer compatible -->
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <!-- css worksheet -->
    <link rel="stylesheet" href="{stylesheet}" />
    <!-- javascript worksheet -->
    <script src="{script}" type="text/javascript" defer></script>
    <!-- homepage title -->
    <title>My Website</title>
    <!-- photo icon -->
    <link rel="shortcut icon" href="./images/header.png" type="image/x-icon" />
    <!-- social sharing image -->
    <!-- HAVE TO INSERT 'URL/header.png' into 'content' -->
    <meta property="og:image" content="" />
    <!-- font awesome kit code -->
    <script
      src="https://kit.fontawesome.com/30c8ebe528.js"
      crossorigin="anonymous"
    ></script>
  </head>
  <body>
    <header>
      <nav class="navbar">
        <ul>
          <li><a href="#home-section">Home</a></li>
          <li><a href="#about-section">About</a></li>
          <li><a href="#projects-section">Projects</a></li>
          <li><a href="#services-section">Services</a></li>
          <li><a href="#contact-section">Contact</a></li>
        </ul>
      </nav>
      <div class="header-img">
        <img src="./images/header.png" alt="the ocean" />
        <h1>{title}</h1>
      </div>
    </header>
    <main>
      <section id="home-section">
        <br />
        <!-- INSERT SOCIAL LINKS INTO 'hrefs' -->
        <div class="social-media">
          <a href="" class="youtube" target="_blank"
            ><i class="fab fa-youtube"></i></a
          ><a href="" class="vimeo" target="_blank"
            ><i class="fab fa-vimeo"></i></a
          ><a href="" class="instagram" target="_blank"
            ><i class="fab fa-instagram"></i
          ></a>
          <a href="" class="facebook" target="_blank"
            ><i class="fab fa-facebook-f"></i
          ></a>
        </div>
      </section>
      <section id="about-section">
        <br /><br />
        <h2>About</h2>
        <br />
        <p>Write something about yourself</p>
      </section>
      <section id="projects-section">
        <br /><br />
        <h2>Projects</h2>
        <br />
        <p>Insert projects compeleted & working on</p>
      </section>
      <section id="services-section">
        <br /><br />
        <h2>Services</h2>
        <br />
        <p>Insert services you are offering</p>
      </section>
      <section id="contact-section">
        <br /><br />
        <h2>Contact</h2>
        <br />
        <p>Contact me via socials or email</p>
        <br />
        <!-- INSERT SOCIAL LINKS INTO 'hrefs' -->
        <div class="social-media">
          <a href="" class="youtube" target="_blank"
            ><i class="fab fa-youtube"></i></a
          ><a href="" class="vimeo" target="_blank"
            ><i class="fab fa-vimeo"></i></a
          ><a href="" class="instagram" target="_blank"
            ><i class="fab fa-instagram"></i
          ></a>
          <a href="" class="facebook" target="_blank"
            ><i class="fab fa-facebook-f"></i
          ></a>
        </div>
        <br />
        <!-- INSERT EMAIL NEXT TO 'Email: ' & INTO 'href' -->
        <p>
          Email:
          <a href=""></a>
        </p>
        <br /><br />
      </section>
    </main>
    <footer>
      <p>{footer}</p>
      <br /><br /><br />
    </footer>
  </body>
</html>
'''

title = "My Website"
stylesheet = "style.css"
script = "script.js"
footer = "Copyright © 2023"

html_output = html.format(title=title, stylesheet=stylesheet, script=script, footer=footer)

print(html_output)
