<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link type="text/css" href="/static/style.css" rel="stylesheet"/>
    <title>Eyða frétt</title>
  </head>
  <body>
      <div>
          % for x in result:
              % for key, value in x.items():
                  <p>{{value}}</p>
               % end
        % end
      </div>
      <div>
          <h3>Sláðu inn númer fréttar til að eyða</h3>
          <form action="/eyda" method="post">
            Númer fréttar: <input name="nr_frettar" type="text" /><br>
            <input value="Staðfesta" type="submit" />
          </form>
      % include('footer.tpl')
  </body>
</html>