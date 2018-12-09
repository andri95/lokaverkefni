<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Breyta Frétt</title>
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
          <h1>Fylltu út alla reitina</h1>
          <form action="/breyta" method="post">
            Númer fréttar: <input name="nr_frettar" type="text" /><br>
            Ný fyrirsögn: <input name="nyr_titill" type="text" /><br>
            Nýr texti: <input name="ny_frett" type="text" />
            <input value="Staðfesta" type="submit" />
          </form>
  </body>
</html>