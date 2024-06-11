# CSS
css = '''
/* UTF-8 */
@charset "UTF-8";

* {{
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}}

html {{
  height: 100%;
  scroll-behavior: smooth;
}}

/* body */
body {{
  background-color: {background_color};
  font-family: {font_family};
  color: {color};
}}

/* navabr */
.navbar {{
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  background-color: {background_color};
  color: {color};
  z-index: 9999;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.2);
}}

.navbar ul {{
  margin: 0;
  padding: 0;
  list-style: none;
  display: flex;
  justify-content: center;
}}

.navbar li {{
  margin: 0 10px;
}}

.navbar a {{
  display: block;
  padding: 10px;
  text-decoration: none;
  color: {color};
  font-weight: bold;
  transition: all 0.3s ease-in-out;
}}

/* header */
.header-img {{
  position: relative;
}}

.header-img img {{
  width: 100%;
  height: auto;
}}

.header-img h1 {{
  position: absolute;
  text-align: center;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 10rem;
  color: {color};
}}

/* page headers */
h2 {{
  font-size: 3em;
  text-align: center;
}}

h3 {{
  font-size: 2.5em;
  text-align: center;
}}

h4 {{
  font-size: 2em;
  text-align: center;
}}

/* youtube videos */
iframe {{
  display: block;
  margin: auto;
}}

/* images */
img {{
  display: block;
  margin: auto;
}}

/* social media links */
.social-media {{
  display: flex;
  justify-content: center;
  margin: 20px 0;
  padding: 0 30px;
}}

.social-media a {{
  display: inline-block;
  margin: 0 10px;
  width: 40px;
  height: 40px;
  border-radius: 50%;
  text-align: center;
  font-size: 20px;
  color: #fff;
}}

.social-media a i {{
  margin-top: 10px;
}}

.instagram {{
  background-color: #c13584;
}}

.youtube {{
  background-color: #cd201f;
}}

.facebook {{
  background-color: #3b5998;
}}

.vimeo {{
  background-color: #1ab7ea;
}}

/* main */
main p {{
  font-size: 20px;
  text-align: center;
}}

main p a {{
  cursor: pointer;
  color: {color};
}}

main p a:hover {{
  color: red;
}}

/* footer */
footer p {{
  font-size: 16px;
  text-align: center;
}}

/* portrait mobile phone display with a max-width: 320px */
@media only screen and (max-width: 320px), (orientation: portrait) {{
  .header-img h1 {{
    font-size: 4rem;
  }}

  h2 {{
    font-size: 2em;
  }}

  h3 {{
    font-size: 1.5em;
  }}

  h4 {{
    font-size: 1em;
  }}
}}
'''

background_color = "#fff"
color = "black"
font_family = "Georgia"

css_output = css.format(background_color=background_color, color=color, font_family=font_family)

print(css_output)
