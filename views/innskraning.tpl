<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link type="text/css" href="/static/style.css" rel="stylesheet"/>
    <title>Innskráning</title>
  </head>
  <body>
      <div>
          <h3>Skrá inn sem admin</h3>
          <form action="/login" method="post">
            Notendanafn: <input name="notendanafn" type="text" /><br>
            Lykilorð: <input name="lykilord" type="password" />
            <input value="Innskrá" type="submit" />
          </form>
      </div>
      % include('footer.tpl')
  </body>
</html>