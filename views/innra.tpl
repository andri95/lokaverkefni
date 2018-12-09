<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>Innra</title>
  </head>
  <body>
      <div>
          <h1>Aðgerðir</h1>
          <form action="/innra" method="post">
              <input type="checkbox" id="breyta" name="breyta" value="breyta">
              <label for="breyta">BREYTA FRÉTT</label>
              <input type="checkbox" id="eyda" name="eyda" value="eyda">
              <label for="eyda">EYÐA FRÉTT</label>
              <input type="checkbox" id="baeta" name="baeta" value="baeta">
              <label for="baeta">NÝ FRÉTT</label>
              <input value="Staðfesta" type="submit" />
          </form>
      </div>
  </body>
</html>