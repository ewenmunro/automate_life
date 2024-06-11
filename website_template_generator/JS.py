#JS
js = '''
// {animation}
const header = document.querySelector(".header-img");
const heading = header.querySelector("h1");

function animateHeading() {{
  const animation = heading.animate(
    [
      {{ transform: "translateX(-100%)", opacity: 0 }},
      {{ transform: "translateX(0)", opacity: 1 }},
    ],
    {{ duration: 2000, easing: "ease-out" }}
  );
  animation.addEventListener("finish", () => {{
    heading.style.color = "#fff";
  }});
}}

animateHeading();
'''

animation = "header"

js_output = js.format(animation=animation)

print(js_output)
