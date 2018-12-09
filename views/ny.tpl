<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <link type="text/css" href="/static/style.css" rel="stylesheet"/>
    <title>Ný frétt</title>
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
          <h1>Fylltu út í alla reiti</h1>
          <form action="/ny" method="post">
            Númer fréttar (3 tölustafir): <input name="nr_frettar" type="text" /><br>
            Ný fyrirsögn: <input name="nyr_titill" type="text" /><br>
            Nýr texti: <input name="ny_frett" type="text" />
            <input value="Staðfesta" type="submit" />
          </form>
  </body>
</html>