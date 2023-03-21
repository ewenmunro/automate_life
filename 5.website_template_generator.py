#HTML
html = '''
<!DOCTYPE html>
<html>
<head>
    <title>{title}</title>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link rel="stylesheet" href="{stylesheet}">
    <script src="{script}" type="text/javascript" defer></script>
</head>
<body>
    <header>
        <h1>{heading}</h1>
    </header>
    <main>
        <p>{content}</p>
    </main>
    <footer>
        <p>{footer}</p>
    </footer>
</body>
</html>
'''

title = "My Website"
stylesheet = "style.css"
script = "script.js"
heading = "Welcome to my website"
content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
footer = "Copyright © 2023"

html_output = html.format(title=title, stylesheet=stylesheet, script=script, heading=heading, content=content, footer=footer)

print(html_output)

# CSS
css = '''
/* {header} */
/* UTF-8 */
@charset "UTF-8";

* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

html {
  height: 100%;
}

body {{
    background-color: {background_color};
    font-family: {font_family};
}}

h1 {{
    color: {heading_color};
    font-size: {heading_size};
}}
'''

header = "My Website Styles"
background_color = "#f0f0f0"
font_family = "Georgia"
heading_color = "#333"
heading_size = "36px"

css_output = css.format(header=header, background_color=background_color, font_family=font_family, heading_color=heading_color, heading_size=heading_size)

print(css_output)

#JS
js = '''
// {header}

function greet(name) {{
    console.log("Hello, " + name + "!");
}}

var message = "Welcome to my website.";

alert(message);
'''

header = "My Website Scripts"

js_output = js.format(header=header)

print(js_output)
